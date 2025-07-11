#!/usr/bin/env /home/pws/miniconda3/bin/python
# -*- coding: utf-8 -*-

import cgi
import csv
import os
import smtplib
import datetime
import html
import sys

# — CONFIGURAZIONE — 
CSV_PATH = '/home/pws/data/contacts.csv'
SMTP_HOST = 'localhost'
SENDER_EMAIL = 'noreply@e-privacy.winstonsmith.org'

# Destinatari fissi
STATIC_RECIPIENTS = [
    'segreteria@winstonsmith.org',
    'archivio@winstonsmith.org',
]

# Definizione dei campi: (nome_csv, chiave_form, is_list)
FIELD_SPECS = [
    ('email_talk',                  'mauticform[email_di_contatto_con_il]',   False),
    ('nome_cognome',                'mauticform[nome_e_cognome]',              False),
    ('contatto_telefonico',         'mauticform[contatto_telefonico]',         False),
    ('proposta_di_durata',          'mauticform[proposta_di_durata]',          False),
    ('titolo',                      'mauticform[titolo]',                      False),
    ('descrizione',                 'mauticform[descrizione]',                 False),
    ('sessioni',                    'mauticform[sessioni]',                    True),
    ('dal_vivo',                    'mauticform[dal_vivo]',                    False),
    ('argomenti',                   'mauticform[argomento__aree_di_intere1]',  True),
    ('quale_altro_argomento',       'mauticform[quale_altro_argomento]',       False),
    ('multi_relatori',              'mauticform[saranno_presenti_piu_rela]',   False),
    ('consenso_pubblicazione',      'mauticform[consenso_alla_pubblicazio]',   False),
    ('consenso_registrazione',      'mauticform[consenso_alle_registrazio]',   False),
    ('commenti',                    'mauticform[commenti_e_istruzioni]',       False),
    ('antispam',                    'mauticform[antispam]',                    False),
]

def get_field(form, key):
    return html.escape(form.getfirst(key, '').strip())

def get_list_field(form, key):
    return [html.escape(v.strip()) for v in form.getlist(key)]

def main():
    form = cgi.FieldStorage()
    data = {}

    # 1) Raccogli e valida i campi
    for name, key, is_list in FIELD_SPECS:
        if is_list:
            vals = get_list_field(form, key)
            if name != 'antispam' and not vals:
                print("Status: 400 Bad Request")
                print("Content-Type: text/plain\n")
                print(f"Errore: manca il campo {name}")
                sys.exit(1)
            data[name] = vals
        else:
            val = get_field(form, key)
            if name != 'antispam' and not val:
                print("Status: 400 Bad Request")
                print("Content-Type: text/plain\n")
                print(f"Errore: manca il campo {name}")
                sys.exit(1)
            data[name] = val

    # 2) Antispam: 7 + 7 deve dare “14”
    if data.get('antispam') != '14':
        print("Status: 400 Bad Request")
        print("Content-Type: text/plain\n")
        print("Errore: risposta antispam errata")
        sys.exit(1)

    # 3) Prepara la lista destinatari includendo l’email dal form
    recipients = STATIC_RECIPIENTS + [data['email_talk']]

    # 4) Scrivi (o crea) il CSV
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    header_needed = not os.path.exists(CSV_PATH)
    try:
        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if header_needed:
                writer.writerow([name for name, _, _ in FIELD_SPECS] + ['timestamp'])
            row = []
            for name, _, is_list in FIELD_SPECS:
                if is_list:
                    row.append(';'.join(data[name]))
                else:
                    row.append(data[name])
            row.append(datetime.datetime.now().isoformat())
            writer.writerow(row)
    except Exception as e:
        print("Status: 500 Internal Server Error")
        print("Content-Type: text/plain\n")
        print(f"Errore scrittura CSV: {e}")
        sys.exit(1)

    # 5) Costruisci l’email
    headers = [
        f"From: {SENDER_EMAIL}",
        f"To: {', '.join(recipients)}",
        "Subject: Nuova proposta Talk inviata",
        "MIME-Version: 1.0",
        "Content-Type: text/plain; charset=utf-8",
        ""
    ]
    body_lines = []
    for name, _, is_list in FIELD_SPECS:
        if is_list:
            body_lines.append(f"{name}: {', '.join(data[name])}")
        else:
            body_lines.append(f"{name}: {data[name]}")
    message = "\n".join(headers) + "\n" + "\n".join(body_lines)

    # 6) Invia l’email
    try:
        smtp = smtplib.SMTP(SMTP_HOST)
        smtp.sendmail(SENDER_EMAIL, recipients, message.encode('utf-8'))
        smtp.quit()
    except Exception as e:
        print("Status: 500 Internal Server Error")
        print("Content-Type: text/plain\n")
        print(f"Errore invio mail: {e}")
        sys.exit(1)

    # 7) Risposta al browser
    print("Content-Type: text/html\n")
    print("<html><head><meta charset='UTF-8'></head><body>")
    print("<h3>Grazie! La tua proposta è stata inviata con successo.</h3>")
    print("</body></html>")

if __name__ == '__main__':
    main()
