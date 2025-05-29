print(">>> PLUGIN PER GENERARE il file eprivacy_editions.js")

from pelican import signals
import json
import os

def genera_mappa_edizioni(edizioni, output_path):
    entries = []
    for year, stagioni in edizioni:
        for when, info in stagioni.items():
            entries.append({
                "year": str(year),
                "when": when.capitalize(),
                "city": info["city"],
                "where": info["location"],
                "link": f"https://e-privacy.winstonsmith.org{info['link']}",
                "lat": info["lat"],
                "lon": info["lon"],
            })
    js = "// FILE GENERATO AUTOMATICAMENTE \n\n// NON MODIFICARE QUESTO FILE: USARE LA VARIABILE ALL_EDITIONS IN pelicanconf.py\n\nconst eprivacyLocations = " + json.dumps(entries, indent=2, ensure_ascii=False) + ";"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js)
 
def write_editions_js(pelican):
    settings = pelican.settings
    edizioni = settings.get("ALL_EDIZIONI", None)
    if not edizioni:
        return
    output_path = os.path.join(settings["PATH"],
                               "extra", "js", "eprivacy_editions.js")
    genera_mappa_edizioni(edizioni, output_path)
    print(">>> File eprivacy_editions.js generato correttamente")

def register():
    signals.initialized.connect(write_editions_js)

