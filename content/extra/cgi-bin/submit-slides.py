#!/usr/bin/env /home/pws/miniconda3/bin/python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CGI handler that receives slide uploads from speakers."""

import cgi
import datetime
import json
import logging
import mimetypes
import os
import smtplib
import sys
import unicodedata

from email.message import EmailMessage


CONFIG_PATH = '/home/pws/sites/org.winstonsmith.e-privacy/site/assets/slides_config.json'
LOG_PATH = '/home/pws/sites/org.winstonsmith.e-privacy/logs/slides.log'


def load_config():
    try:
        with open(CONFIG_PATH, encoding='utf-8') as fh:
            return json.load(fh)
    except FileNotFoundError:
        bail('500 Internal Server Error', 'Configurazione mancante, contattare il webmaster.')
    except json.JSONDecodeError as exc:
        bail('500 Internal Server Error', f'Configurazione non valida: {exc}')


def setup_logging():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def bail(status, message):
    logging.error('Errore %s: %s', status, message)
    print(f'Status: {status}')
    print('Content-Type: text/plain\n')
    print(message)
    sys.exit(1)


def get_field(form, name, required=False):
    value = form.getfirst(name, '').strip()
    if required and not value:
        bail('400 Bad Request', f"Campo '{name}' mancante")
    return value


def parse_submitter(cfg, submitter_id):
    for entry in cfg.get('SUBMITTERS', []):
        if entry.get('id') == submitter_id:
            return entry
    bail('400 Bad Request', 'Relatore non valido')


def safe_filename(name):
    base = os.path.basename(name or '')
    if not base:
        return 'file'
    normalised = unicodedata.normalize('NFKD', base)
    ascii_only = normalised.encode('ascii', 'ignore').decode('ascii')
    ascii_only = ascii_only.replace(' ', '_')
    allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
    cleaned = ''.join((c if c in allowed else '_') for c in ascii_only)
    cleaned = cleaned.strip('._')
    return cleaned or 'file'


def ensure_allowed(filename):
    allowed_extensions = {
        '.pdf', '.doc', '.docx', '.odt', '.rtf', '.txt', '.md',
        '.html', '.htm', '.ppt', '.pptx', '.odp', '.key', '.zip',
        '.mp3', '.wav', '.ogg', '.flac', '.mp4', '.mov', '.m4v', '.mkv', '.avi'
    }
    ext = os.path.splitext(filename.lower())[1]
    if ext and ext in allowed_extensions:
        return True
    # fallback to MIME family for audio/video
    mime, _ = mimetypes.guess_type(filename)
    if mime and (mime.startswith('audio/') or mime.startswith('video/')):
        return True
    bail('400 Bad Request', f"Estensione file non supportata: {filename}")


def next_counter(base_path, prefix):
    current = 0
    for entry in os.listdir(base_path):
        if not entry.startswith(prefix + '-'):
            continue
        suffix = entry[len(prefix) + 1 :]
        digits = ''
        for char in suffix:
            if char.isdigit():
                digits += char
            else:
                break
        if digits:
            try:
                current = max(current, int(digits))
            except ValueError:
                continue
    return current + 1


def collect_files(form):
    field = form['files'] if 'files' in form else []
    if isinstance(field, list):
        items = field
    else:
        items = [field]
    filtered = [item for item in items if getattr(item, 'filename', '')]
    if not filtered:
        bail('400 Bad Request', 'Nessun file allegato')
    return filtered


def read_size(fileobj):
    position = fileobj.tell()
    fileobj.seek(0, os.SEEK_END)
    size = fileobj.tell()
    fileobj.seek(0, os.SEEK_SET)
    if position:
        fileobj.seek(position)
    return size


def main():
    setup_logging()
    cfg = load_config()

    storage_root = os.path.expanduser(cfg.get('STORAGE_PATH', '~/data/inbound'))
    os.makedirs(storage_root, exist_ok=True)

    form = cgi.FieldStorage(keep_blank_values=True)
    logging.info('Ricevuta consegna da %s', os.environ.get('REMOTE_ADDR', '-'))

    submitter_id = get_field(form, 'submitter', required=True)
    submitter = parse_submitter(cfg, submitter_id)
    submitter_label = submitter['label']
    submitter_email = get_field(form, 'email', required=True)
    notes = get_field(form, 'note', required=False)

    password = get_field(form, 'password', required=True)
    if password != cfg.get('PASSWORD'):
        bail('403 Forbidden', 'Password non valida')

    try:
        challenge_a = int(get_field(form, 'captcha_a', required=True))
        challenge_b = int(get_field(form, 'captcha_b', required=True))
        challenge_answer = int(get_field(form, 'captcha_answer', required=True))
    except ValueError:
        bail('400 Bad Request', 'Il risultato del calcolo non è valido')

    if challenge_a + challenge_b != challenge_answer:
        bail('400 Bad Request', 'Risultato del calcolo aritmetico errato')

    files = collect_files(form)

    prefix = submitter_id
    counter = next_counter(storage_root, prefix)
    while True:
        submission_id = f"{prefix}-{counter:04d}"
        submission_dir = os.path.join(storage_root, submission_id)
        if not os.path.exists(submission_dir):
            break
        counter += 1
    os.makedirs(submission_dir, exist_ok=False)

    stored_files = []
    total_size = 0
    for idx, item in enumerate(files, start=1):
        original_name = safe_filename(item.filename)
        ensure_allowed(original_name)
        file_obj = item.file
        size = read_size(file_obj)
        total_size += size

        target_name = original_name
        target_path = os.path.join(submission_dir, target_name)
        suffix = 1
        while os.path.exists(target_path):
            stem, ext = os.path.splitext(original_name)
            target_name = f"{stem}_{suffix}{ext}"
            target_path = os.path.join(submission_dir, target_name)
            suffix += 1

        file_obj.seek(0)
        with open(target_path, 'wb') as destination:
            while True:
                chunk = file_obj.read(1024 * 1024)
                if not chunk:
                    break
                destination.write(chunk)

        stored_files.append({
            'original': item.filename,
            'saved_as': target_name,
            'size': size,
            'path': target_path,
        })

    metadata = {
        'submission_id': submission_id,
        'submitter_id': submitter_id,
        'submitter_label': submitter_label,
        'email': submitter_email,
        'notes': notes,
        'files': stored_files,
        'timestamp': datetime.datetime.now().isoformat(),
        'ip': os.environ.get('REMOTE_ADDR', '-'),
        'user_agent': os.environ.get('HTTP_USER_AGENT', '-'),
    }

    metadata_path = os.path.join(submission_dir, 'metadata.json')
    with open(metadata_path, 'w', encoding='utf-8') as fh:
        json.dump(metadata, fh, indent=2, ensure_ascii=False)

    recipients = list(dict.fromkeys(cfg.get('STATIC_RECIPIENTS', []) + [submitter_email]))

    message = EmailMessage()
    message['From'] = cfg.get('SENDER_EMAIL', 'noreply@winstonsmith.org')
    message['To'] = ', '.join(recipients)
    message['Subject'] = f"Consegna materiale: {submitter_label} ({submission_id})"

    lines = [
        f"Ciao {submitter_label},",
        '',
        'abbiamo ricevuto i file consegnati tramite il portale e-privacy.',
        f"Identificativo consegna: {submission_id}",
        f"Data/Ora: {metadata['timestamp']}",
        '',
        'Materiale ricevuto:',
    ]
    for entry in stored_files:
        lines.append(f" - {entry['original']} -> {entry['saved_as']} ({entry['size']} byte)")

    if notes:
        lines.extend(['', 'Note inviate:', notes])

    attachments = []
    max_inline = int(cfg.get('MAX_INLINE_SIZE', 1024 * 1024 * 1024))
    if total_size <= max_inline:
        for entry in stored_files:
            try:
                with open(entry['path'], 'rb') as fh:
                    data = fh.read()
                guessed_type, _ = mimetypes.guess_type(entry['saved_as'])
                maintype, subtype = (guessed_type or 'application/octet-stream').split('/', 1)
                attachments.append((data, maintype, subtype, entry['saved_as']))
            except Exception as exc:
                logging.exception('Allegato %s non aggiunto: %s', entry['path'], exc)
                attachments = []
                break

    if not attachments:
        lines.extend([
            '',
            'Gli allegati non sono stati inclusi nella mail (dimensioni elevate o errore durante la lettura).',
            f'Sono disponibili sul server in {submission_dir}.',
        ])

    lines.extend([
        '',
        'Grazie!',
        '--',
        'Segreteria e-privacy',
    ])

    message.set_content('\n'.join(lines))

    for data, maintype, subtype, filename in attachments:
        message.add_attachment(data, maintype=maintype, subtype=subtype, filename=filename)

    try:
        smtp = smtplib.SMTP(cfg.get('SMTP_HOST', 'localhost'))
        smtp.send_message(message)
        smtp.quit()
    except Exception as exc:
        logging.exception('Invio email fallito: %s', exc)
        bail('500 Internal Server Error', f'Invio email fallito: {exc}')

    logging.info('Consegna %s completata (%d file, %d byte)', submission_id, len(stored_files), total_size)

    payload = {
        'submission_id': submission_id,
        'label': submitter_label,
        'files': [{'name': f['saved_as'], 'size': f['size']} for f in stored_files],
    }

    redirect_url = cfg.get('REDIRECT_URL', '/grazie-consegna-slides.html')
    payload_json = json.dumps(payload, ensure_ascii=False)

    print('Content-Type: text/html; charset=utf-8\n')
    print(f"""<!DOCTYPE html>
<html><head><meta charset=\"utf-8\"><title>Reindirizzamento…</title></head><body>
<script>
  var payload = {payload_json};
  sessionStorage.setItem('lastSlidesSubmission', JSON.stringify(payload));
  window.location.href = '{redirect_url}';
</script>
<p>Invio completato, un momento…</p>
</body></html>""")


if __name__ == '__main__':
    main()
