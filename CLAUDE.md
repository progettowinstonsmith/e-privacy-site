# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Pelican-based static site generator** for the e-privacy conference series. The project generates a multi-edition event website with support for conference schedules, speaker submissions, slide submissions, and historical event data.

## Build & Development

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Build
```bash
make html              # Build to output/
make DEBUG=1 html      # Build with debug output
make clean             # Remove generated output/
```

### Local Development Server
```bash
make devserver [PORT=8000]    # Start Pelican with autoreload + HTTP server
make stopserver               # Stop background development server
```

The development server listens on `localhost:8000` and rebuilds on content changes.

### Publish to Production
```bash
make publish           # Build with publishconf.py settings
make upload            # Publish + rsync to production server
make rsync_upload      # Publish + rsync with SSH options
```

## Architecture

### Core Structure
- **`pelicanconf.py`** — Main Pelican configuration. Contains event metadata, submission settings, partner/sponsor data, and plugin settings. **This is where to update YEAR, EDITION, EVENT_PATH, SITENAME, EPRIVACY_N for new events.**
- **`content/YYYY/SEASON/`** — Event content organized by year and season (summer/winter). Each event has:
  - `vars.md` — Metadata (city, location, theme, dates, etc.)
  - `programma.md` — Main event page with schedule
  - `cfp.md` — Call for Papers
  - `arrivare.md` — Travel/venue instructions
  - `speakers.md` — Speaker list
  - `interventi.md` — Talk abstracts and speaker bios
  - Other pages like `faq.md`, `proposta.md`, etc.
- **`output/`** — Generated static site (build output, do not commit)
- **`plugins/`** — Custom Pelican plugins:
  - `gened.py` — Generates `eprivacy_editions.js` from `ALL_EDIZIONI` config (maps all event locations)
  - `submitter.py` — Exports submission form configs (`submit_config.json`, `slides_config.json`) to `output/assets/`

### Content Frontmatter
Event markdown files use Pelican metadata headers:
```yaml
Template: event
Date: YYYY-MM-DD HH:MM:SS
Title: Event title
Year: YYYY
Season: summer/winter
Slug: e-privacy-XXXVIII-programma
Status: published
Category: YYYY
[... other custom fields like When, Where, Num, Eprivacy_N, etc.]
```

### Key Configuration Variables
In `pelicanconf.py`:
- **`EDITION`** — Event edition number
- **`YEAR`** & **`EDITION`** — Year and season slug (e.g., "2026", "summer")
- **`EVENT_PATH`** — Path to current event content (`content/YYYY/SEASON/`)
- **`SITENAME`** — Page title
- **`EPRIVACY_N`** — Roman numeral for edition number
- **`PROPOSALS_OPEN`** — Whether CFP is accepting submissions
- **`COUNTDOWN`**, **`EVENT_TIME`** — Countdown timer settings
- **`SUBMIT_SETTINGS`**, **`SLIDES_SETTINGS`**, **`SLIDES_SUBMITTERS`** — Form submission configuration

## Preparing a New Edition

1. **Create content structure** — Copy previous edition folder: `cp -r content/YYYY/season content/YYYY+1/season`
2. **Update pelicanconf.py** — Change YEAR, EDITION, EVENT_PATH, SITENAME, EPRIVACY_N, EVENT_TIME, COUNTDOWN
3. **Update SUBMIT_SETTINGS/SLIDES_SETTINGS** if submission endpoints or passwords change
4. **Update content files** — Edit markdown in the new event folder (cfp.md, programma.md, arrivare.md, etc.)
5. **Build & test** — `make devserver` to preview locally
6. **Deploy** — `make upload` to push to production

Note: Plugins run automatically during build and generate derived assets (eprivacy_editions.js, submit form configs). Don't run them manually.

## Deploy Configuration

Deployment destinations in Makefile:
- **`SSH_HOST`** — `aaron.winstonsmith.org` (production server)
- **`SSH_TARGET_DIR`** — `/home/pws/sites/org.winstonsmith.e-privacy/site/`
- Custom symlink: slides from `/home/pws/sites/org.winstonsmith.urna/site/materiali/` are linked into the e-privacy site

## Historical Data

- **`store/`** — Markdown files for past events (used for archive pages)
- **`moderatori.md`** — Moderator list
- **`ending.md`** — Site-wide closing message/footer

## Debugging

- Enable verbose Pelican output: `make DEBUG=1 html`
- Check `pelican.pid` and `srv.pid` for process IDs if background server is stuck
- Generated assets (submit configs, editions map) are in `output/assets/`
