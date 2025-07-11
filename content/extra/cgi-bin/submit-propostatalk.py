#!/usr/bin/env /home/pws/miniconda3/bin/python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi, csv, os, smtplib, datetime, html, json, sys

# — CONFIGURAZIONE —
CSV_PATH     = '/home/pws/data/contacts.csv'
SMTP_HOST    = 'localhost'
SENDER_EMAIL = 'noreply@e-privacy.winstonsmith.org'
# URL di ringraziamento
REDIRECT_URL = '/grazie.html'

# Destinatari fissi
STATIC_RECIPIENTS = [
    'segreteria@winstonsmith.org',
    'archivio@winstonsmith.org',
]

# Campi “talk”
TALK_FIELDS = [
    ('email',    'form[email_di_contatto_con_il]', False, False),
    ('nome',     'form[nome_e_cognome]',           False, False),
    ('telefono', 'form[contatto_telefonico]',      False, False),
    ('durata',   'form[proposta_di_durata]',       False, False),
    ('titolo',   'form[titolo]',                   False, False),
    ('descr',    'form[descrizione]',              False, False),
    ('sessioni','form[sessioni][]',                  False, True),
    ('dal_vivo','form[dal_vivo]',                  False, False),
    ('argomenti','form[argomento__aree_di_intere1][]',False, True),
    ('altro_arg', 'form[quale_altro_argomento]',   False, False),
    ('multi_rela','form[saranno_presenti_piu_rela]',False, False),
    ('cons_pub','form[consenso_alla_pubblicazio]', False, False),
    ('cons_reg','form[consenso_alle_registrazio]', False, False),
    ('comm','form[commenti_e_istruzioni]',         True, False),
    ('antispam','form[antispam]',                  False, False),
]

# Campi speaker
SPEAKER_FIELDS = [
    'relatore_o_autore',
    'cognome',
    'nome',
    'organizzazione_o_istituzi',
    'email',
    'numero_di_telefono',
    'breve_ma_non_troppo_prese',
    'telegram1'
]

def get_first(form, key):
    return html.escape(form.getfirst(key, '').strip())

def get_all(form, key):
    return [html.escape(v.strip()) for v in form.getlist(key)]

def bail(status, msg):
    print(f"Status: {status}")
    print("Content-Type: text/plain\n")
    print(f"Errore: {msg}")
    sys.exit(1)

def main():
    form = cgi.FieldStorage()
    talk = {}

    # 1) Raccogli i campi “talk”
    for key, fname, optional, is_list in TALK_FIELDS:
        if is_list:
            vals = get_all(form, fname)
            if not vals and not optional:
                bail("400 Bad Request", f"campo '{key}' mancante")
            talk[key] = vals
        else:
            val = get_first(form, fname)
            if not val and not optional:
                bail("400 Bad Request", f"campo '{key}' mancante")
            talk[key] = val

    # 2) Controlla antispam
    if talk.get('antispam') != '14':
        bail("400 Bad Request", "risposta antispam errata")

    # 3) Raccogli speaker
    # leggiamo array per ogni SPEAKER_FIELDS
    lists = { f: get_all(form, f"form[{f}]") for f in SPEAKER_FIELDS }
    count = len(lists['nome'])
    speakers = []
    for i in range(count):
        sp = { f: lists[f][i] if i < len(lists[f]) else '' for f in SPEAKER_FIELDS }
        if not sp['nome'] or not sp['cognome'] or not sp['email']:
            bail("400 Bad Request", f"relatore #{i+1} incompleto")
        speakers.append(sp)

    # 4) Destinatari
    recipients = STATIC_RECIPIENTS + [talk['email']] + [ s['email'] for s in speakers ]

    # 5) Scrivi CSV
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    header_needed = not os.path.exists(CSV_PATH)
    try:
        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if header_needed:
                header = [k for k, *_ in TALK_FIELDS] + ['speakers_json','timestamp']
                writer.writerow(header)
            row = []
            for k, *_ in TALK_FIELDS:
                v = talk[k]
                row.append(';'.join(v) if isinstance(v, list) else v)
            row.append(json.dumps(speakers, ensure_ascii=False))
            row.append(datetime.datetime.now().isoformat())
            writer.writerow(row)
    except Exception as e:
        bail("500 Internal Server Error", f"scrittura CSV fallita: {e}")

    # 6) Invia email
    headers = [
        f"From: {SENDER_EMAIL}",
        f"To: {', '.join(recipients)}",
        "Subject: Nuova proposta Talk inviata",
        "MIME-Version: 1.0",
        "Content-Type: text/plain; charset=utf-8",
        ""
    ]
    body = ["=== DATI TALK ==="]
    for k, *_ in TALK_FIELDS:
        val = talk[k]
        body.append(f"{k}: {', '.join(val) if isinstance(val, list) else val}")
    body.append("\n=== RELATORI ===")
    for idx, sp in enumerate(speakers,1):
        body.append(f"-- Relatore #{idx} --")
        for f in SPEAKER_FIELDS:
            body.append(f"{f}: {sp[f]}")
    message = "\n".join(headers) + "\n" + "\n".join(body)

    try:
        smtp = smtplib.SMTP(SMTP_HOST)
        smtp.sendmail(SENDER_EMAIL, recipients, message.encode('utf-8'))
        smtp.quit()
    except Exception as e:
        bail("500 Internal Server Error", f"invio email fallito: {e}")

    # 7) Rispondi con script che popola sessionStorage e reindirizza
    payload = {
        'talk': {
            'titolo': talk['titolo'],
            'email': talk['email']
        },
        'speakers': [
            {'nome': s['nome'], 'cognome': s['cognome'], 'email': s['email']}
            for s in speakers
        ]
    }
    payload_json = json.dumps(payload, ensure_ascii=False)

    print("Content-Type: text/html; charset=utf-8\n")
    print(f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Reindirizzamento…</title></head><body>
<script>
  // salva i dati in sessionStorage
  var payload = {payload_json};
  sessionStorage.setItem('lastSubmission', JSON.stringify(payload));
  // reindirizza alla pagina statica di ringraziamento
  window.location.href = '{REDIRECT_URL}';
</script>
<p>Un momento, stiamo lavorando…</p>
</body></html>""")

if __name__ == '__main__':
    main()
