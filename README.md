# English Mass · St. Joseph Convent

Static site (GitHub Pages, no build step) for the English Mass at St. Joseph Convent.
Two pages, one content file, one editor:

| File | What it is |
|---|---|
| `index.html` | **Mass texts**: the whole Order of Mass with the day's readings and prayers, each song and sung Mass part in its place |
| `songs.html` | **Songs & practice**: sheet music with IPA, the recording (play button), for learning the songs |
| `mass-data.js` | **All the content** of both pages: days → celebrations → blocks (readings, songs, prayers, rubrics…) |
| `editor.html` | **The editor**: change, add or remove days, songs, readings, prayers and any part of the Mass, preview, and save straight to GitHub |

## Weekly update (with the editor)
1. Open `https://cantate-domino.github.io/english-mass/editor.html` (first time on a computer/phone: ⋯ → *Mã truy cập GitHub*).
2. **＋ Thêm ngày** → date, name of the day, colour, "based on" a similar day (a Saturday, a memorial, a feast…);
   the readings, songs and proper prayers of that day are cleared.
3. In **Phần hay sửa**: choose the songs (ICLA number of the printed book, YouTube link, start second, sheet image),
   paste the readings (one blank line between paragraphs; *Làm sạch văn bản dán từ USCCB*), the Alleluia verse, the prayers.
4. **Xem trước** to check, then **Lưu lên web**. "Updated …" changes by itself; the pages show it within a minute.

Anything else (Gloria, Creed, Universal Prayer, a rubric, a whole section): **Toàn bộ** → add / move / delete blocks,
or *Chép phần từ ngày khác*. Every save is a commit: older versions stay in the GitHub history.

## Notes
- Song numbers follow the community's printed (older) ICLA book; `num` → "ICLA No. …".
- A day marked *Chỉ hiện ở trang tập hát* (`songsOnly`) is on `songs.html` only.
- A Mass stays at the top until 12:00 noon (Vietnam time) on its day, then the next Mass opens (both pages).
- `index.html#2026-11-07` opens that Mass; `songs.html#2026-11-07-entrance` opens that song.
- `sheets/` sheet music (`<song-title>-ipa.png`, `-narrow` for phones), `icons/` Dominican seal,
  `tools/` cutting songs from the ICLA PDF and the IPA overlay.
- Until 05/11/2026 the content was in `data.js` + `texts.js` and built by the page; those two files are no longer used.
