# Kuä · Kuä bol

A student research prototype for **PLS 419: AI from a Social Science Perspective** (Nazarbayev University, Fall 2026).
Kuä is a proposed eGov service that would let citizens of Kazakhstan see who accesses their records, find contradictions between state registries and get errors corrected.

**This is not an official government website.** It does not connect to eGov, collect data or run live AI. The demo is scripted with fictional data.

## Publish on GitHub Pages

1. Create a new public repository on GitHub (for example `kua`).
2. Upload everything in this folder to the repository root, including the hidden `.nojekyll` file.
   - Website: **Add file → Upload files**, drag in the folder contents, then **Commit changes**.
   - Or from a terminal: `git init && git add . && git commit -m "Kuä site" && git branch -M main && git remote add origin https://github.com/<you>/kua.git && git push -u origin main`
3. Go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then **Save**.
4. After a minute or two the site is live at `https://<you>.github.io/kua/`.

## Structure

| Path | What it is |
|---|---|
| `index.html` … `sources.html` | The nine built pages (each contains English, Kazakh and Russian) |
| `assets/css/site.css` | All styles, including the dark, light and system themes |
| `assets/js/site.js` | Language and theme switching, scroll animations, demo, charts, calculator |
| `assets/fonts/` | Literata and Inter (SIL Open Font License), subset to Latin and Cyrillic, including Kazakh letters |
| `src/` | The sources the pages are built from |

## Editing

Do not edit the built `.html` files directly. Edit the files in `src/` and rebuild:

- Page text: `src/content/<page>.<lang>.html` (`en`, `kk`, `ru`)
- Interface, chart, animation and demo text: `src/strings_<lang>.py`
- Charts, animations and illustrations: `src/components.py`

Rebuild with Python 3 (no packages needed):

```
python3 src/build.py
```

If you change `src/content/sources.en.html`, also run `python3 src/make_sources_i18n.py` before building.

To preview locally, run `python3 -m http.server` in this folder and open `http://localhost:8000`. Opening the files directly with `file://` blocks the fonts.

## Languages

The original is English. The Kazakh and Russian versions are raw draft translations and will be double-checked. A visitor's language and theme choices are stored only in their own browser. A link can force a language with `?lang=kk`, `?lang=ru` or `?lang=en`.
