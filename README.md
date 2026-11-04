# English Mass · St. Joseph Convent

Static site (GitHub Pages, no build step) for the English Mass at St. Joseph Convent.
Two pages, one set of data:

| Page | What it shows |
|---|---|
| `index.html` | **Mass texts**: the whole Order of Mass with the day's readings and prayers, each song and sung Mass part in its place (sheet music opens in place) |
| `songs.html` | **Songs & practice**: sheet music with IPA, the recording (play button), for learning the songs |

Both pages read `data.js`, so a song changed there changes on both. Each song on the texts page has
"Listen & practise", which opens the same song on `songs.html`; each week on `songs.html` has "Texts".

## Files
- `data.js` – `SITE.updated` + `WEEKS`: date, feast, songs (entrance, offertory, communion?, recessional), sung Mass parts (`mass`)
- `texts.js` – `TEXTS["YYYY-MM-DD"]`: readings, Gospel acclamation verse, proper prayers, Gloria/Creed (see the comment at the top)
- `sheets/` – sheet music cut from the ICLA Song Book (`<song-title>.png`, `-ipa` with IPA, `-narrow` for phones)
- `icons/` – Dominican seal
- `tools/crop.py`, `tools/icla-index.json`, `tools/book-index.json` – cutting songs from the ICLA PDF; `tools/ipa/` – IPA overlay

## Weekly update
1. Songs: add the Mass at the top of `WEEKS` in `data.js` (numbers follow the community's printed ICLA book).
2. Texts: add the same date in `texts.js` (a reading not yet typed: `{ kind, cite, tba: true }`).
3. Change `SITE.updated` (Vietnam time), commit and push.

A Mass stays at the top until 12:00 noon (Vietnam time) on its day, then the next Mass opens (both pages).
Past Masses appear on the texts page only when their texts were entered.

`index.html#2026-11-07` opens that Mass; `songs.html#2026-11-07-entrance` opens that song.
