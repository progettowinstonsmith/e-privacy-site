# Elenchi Relatori e-privacy

Questi file contengono l'elenco completo dei relatori che hanno partecipato alle varie edizioni del convegno e-privacy dal 2002 ad oggi.

## File generati

### relatori-eprivacy.org (2015-2025)
- **Periodo**: Dal 2015 al 2025
- **Formato sorgente**: File Markdown strutturati (speakers.md)
- **Relatori estratti**: 179 relatori unici
- **Edizioni**: 22 edizioni (summer/winter/autumn)

### relatori-eprivacy-2002-2014.org (2002-2014)
- **Periodo**: Dal 2002 al 2014
- **Formato sorgente**: Tabelle dei programmi in Markdown
- **Relatori estratti**: 200 relatori unici
- **Edizioni**: 16 edizioni analizzate

## Formato dei file

I file sono in formato Org-mode con la seguente struttura:

```org
#+TITLE: Relatori e-privacy
#+AUTHOR: Progetto Winston Smith
#+DATE: [2025-01-09]

* Elenco Relatori per Cognome

- Nome Cognome (anno, anno/stagione, ...)
- ...

* Statistiche
- Totale relatori unici: N
- Periodo: ...
```

## Note tecniche

- I relatori sono ordinati alfabeticamente per cognome
- Gli anni sono indicati come:
  - `YYYY` per edizioni annuali (2002-2011)
  - `YYYY/summer` per edizioni estive
  - `YYYY/winter` per edizioni invernali
  - `YYYY/autumn` per edizioni autunnali
- Possono esserci duplicati tra i due file per relatori che hanno partecipato in entrambi i periodi
- Alcuni nomi possono apparire con variazioni (es. "Avv. Nome Cognome" vs "Nome Cognome")

## Generazione

I file sono stati generati automaticamente tramite script Python che:
1. Analizza i file Markdown delle edizioni storiche
2. Estrae i nomi dei relatori dalle tabelle dei programmi e dalle pagine dedicate
3. Normalizza e pulisce i nomi
4. Elimina duplicati e voci spurie
5. Genera file Org-mode ordinati per cognome

Data di generazione: 2025-01-09
