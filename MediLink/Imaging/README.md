# MediLink Imaging User Manual — sources

- `../MediLink-Imaging-User-Manual.pdf` — the finished manual (A4 portrait, 13 pages)
- `../raw/img-*.jpg` — screenshots captured from the live system (2x); `../raw/img-rects.json` holds element positions
- `fig/` — annotated figures used in the manual
- `annotate.py` — draws the red boxes (`python3 annotate.py` from this folder)
- `content.py` — manual text; `head.py` / `tail.py` — helpers, cover and contents; `style.css` — A4 layout
- Rebuild: `cat head.py content.py tail.py > build.py && python3 build.py && python3 pages.py && python3 build.py`

All data shown is sample data only.
