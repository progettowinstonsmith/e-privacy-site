print(">>> PLUGIN PER GENERARE il file di configurazione per il SUBMIT")

import os
import json
from pelican import signals


def _normalise_submitters(raw_submitters):
    normalised = []
    for item in raw_submitters or []:
        if isinstance(item, dict):
            entry = {
                'id': item.get('id') or item.get('slug') or item.get('value'),
                'label': item.get('label') or item.get('name') or item.get('title', ''),
            }
            email = item.get('email')
            if email:
                entry['email'] = email
        elif isinstance(item, (list, tuple)):
            if len(item) == 3:
                entry = {'id': item[0], 'label': item[1], 'email': item[2]}
            elif len(item) == 2:
                entry = {'id': item[0], 'label': item[1]}
            else:
                continue
        else:
            continue

        if not entry.get('id') or not entry.get('label'):
            continue
        normalised.append(entry)
    return normalised


def export_submit_settings(pelican):
    output_dir = os.path.join(pelican.settings['OUTPUT_PATH'], 'assets')
    os.makedirs(output_dir, exist_ok=True)

    submit_cfg = pelican.settings.get('SUBMIT_SETTINGS')
    if submit_cfg:
        submit_path = os.path.join(output_dir, 'submit_config.json')
        with open(submit_path, 'w', encoding='utf-8') as fh:
            json.dump(submit_cfg, fh, indent=2)

    slides_cfg = pelican.settings.get('SLIDES_SETTINGS')
    slides_submitters = pelican.settings.get('SLIDES_SUBMITTERS')
    if slides_cfg and slides_submitters:
        payload = dict(slides_cfg)
        payload['SUBMITTERS'] = _normalise_submitters(slides_submitters)
        slides_path = os.path.join(output_dir, 'slides_config.json')
        with open(slides_path, 'w', encoding='utf-8') as fh:
            json.dump(payload, fh, indent=2)


def register():
    signals.finalized.connect(export_submit_settings)

