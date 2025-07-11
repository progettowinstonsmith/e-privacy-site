#!/usr/bin/env /home/pws/miniconda3/bin/python
import cgi, csv, os, smtplib, datetime, html

# 1) Parametri
CSV_PATH = '/home/pws/data/contacts.csv'   # path “assoluto”, fuori dall’output statico
EMAIL_TO  = 'emmanuele@exedre.org'

# 2) Ricevi e sanifica
form = cgi.FieldStorage()
campi = ['nome','email','messaggio']
dati  = {}
for f in campi:
    val = form.getfirst(f, '').strip()
    if not val:
        print("Status: 400 Bad Request")
        print("Content-Type: text/plain\n")
        print(f"Errore: manca il campo {f}")
        exit()
    dati[f] = html.escape(val)

# 3) Scrivi CSV
os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
header = not os.path.exists(CSV_PATH)
with open(CSV_PATH, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if header:
        writer.writerow(campi + ['inviato_il'])
    writer.writerow([dati[f] for f in campi] + [datetime.datetime.now().isoformat()])

# 4) Spedisci email
body = "Hai ricevuto un nuovo messaggio:\n\n" + "\n".join(f"{k}: {dati[k]}" for k in campi)
msg  = f"From: segreteria@winstonsmith.org\r\n" \
       f"To: {EMAIL_TO}\r\n" \
       f"Subject: Nuova richiesta da sito\r\n\r\n" \
       f"{body}"
smtp = smtplib.SMTP('localhost')
smtp.sendmail(f"segreteria@winstonsmith.org", [EMAIL_TO], msg.encode('utf-8'))
smtp.quit()

# 5) Risposta al browser
print("Content-Type: text/html\n")
print("<html><body><h3>Grazie per il messaggio!</h3></body></html>")
