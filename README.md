# e-privacy-site
e-privacy-site


# Workflow sito e-privacy

## Preparazione di una nuova edizione

1. **Crea la struttura dei contenuti**
   - Copia la cartella dell’ultima edizione (ad es. `content/2024/winter/`) nella nuova posizione (`content/2025/winter/`).
   - Aggiorna i Markdown principali: `cfp.md` (call for paper), `arrivare.md`/`come-arrivare.md`, `programma.md`, eventuali `interventi.md`, `proposta.md`, `faq.md`, ecc.
   - Aggiorna i file di supporto (`vars.md`, `mail.md`, template `.md5`, immagini, ...). Mantieni slug e campi Pelican coerenti con l’anno/edizione.

2. **Aggiorna la configurazione** (`pelicanconf.py`)
   - `YEAR`, `EDITION`, `EVENT_PATH`, `SITENAME`, `EPRIVACY_N`, `SESSIONI`, `PROPOSALS_OPEN`, `EVENT_TIME` e voci nel menu `THIS` vanno allineati alla nuova sessione.
   - Aggiorna `SUBMIT_SETTINGS`/`SLIDES_SETTINGS` se cambiano destinatari, percorsi o password, così come `SLIDES_SUBMITTERS` o altri riferimenti specifici.
   - Verifica `EXTRA_PATH_METADATA` se sono stati aggiunti nuovi asset (es. script CGI o file statici).

3. **Genera dati derivati**
   - I plugin in `plugins/` creano asset durante la build (`eprivacy_editions.js`, `submit/slides_config.json`, ecc.). Non serve lanciarli manualmente: vengono eseguiti da Pelican.
   - Se usi script esterni (es. sincronizzazione con fogli di calcolo) assicurati che producano i nuovi `.md` prima della build.

4. **Test locale**
   - Installa le dipendenze (`pip install -r requirements.txt` o usa l’ambiente `environment.yml`).
   - Esegui `make html` (o `pelican content -o output -s pelicanconf.py`) e verifica il risultato in `output/` con un server locale (`python -m http.server` o `make devserver`).
   - Controlla i form: le CGI sono in `content/extra/cgi-bin/` e vengono copiate in `output/cgi-bin/` durante la build.

5. **Pubblicazione**
   - `make upload`, `make rsync_upload` o il target personalizzato che usi per allineare il server copierà `output/` (inclusi i CGI) nella dir di hosting `/home/pws/sites/org.winstonsmith.e-privacy/site/`.
   - Dopo l’upload verifica: `https://e-privacy.winstonsmith.org/` e gli endpoint CGI (`/cgi-bin/submit-*.py`). Per controlli rapidi: `ssh` sul server e guarda i log web/mail.

6. **Manutenzione**
   - Aggiorna le pagine “storiche” (`content/<anno>.md`, `store/`) o la mappa delle edizioni se necessario.
   - Disattiva `PROPOSALS_OPEN` o modifica banner/countdown quando chiudi le call.
   - Ricorda di ruotare le password dei form (es. consegna slide) quando cambi edizione e di riflettere il cambiamento in `SLIDES_SETTINGS`/documentazione inviata ai relatori.

## Note storiche

- (2018-05-03) Aggiunto lo script `sync-sheet.py` per estrarre da Google Sheets programma, interventi e biografie, generando i file `.md` a partire dai template dedicati. Servono credenziali API Google: <https://developers.google.com/sheets/api/quickstart/python>


