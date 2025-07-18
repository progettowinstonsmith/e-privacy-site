print(">>> PLUGIN PER GENERARE il file di configurazione per il SUBMIT")

import os, json
from pelican import signals

def export_submit_settings(pelican):
    cfg = pelican.settings.get('SUBMIT_SETTINGS', {})
    out = os.path.join(pelican.settings['OUTPUT_PATH'], 'assets', 'submit_config.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, indent=2)

def register():
    signals.finalized.connect(export_submit_settings)


