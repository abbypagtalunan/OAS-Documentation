"""Merge the six MediLink role manuals into one PDF with a combined cover, table of contents,
continuous page numbers and bookmarks. Run from this folder: python3 merge.py"""
import os, re, io, json
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (DictionaryObject, NameObject, ArrayObject, NumberObject, NullObject)
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
H = '/home/claude'
PARTS = [  # (role, pdf)
    ('Doctor', f'{H}/ml/manual.pdf'),
    ('Secretary', f'{H}/sec/manual.pdf'),
    ('Patient', f'{H}/pat/manual.pdf'),
    ('Laboratory', f'{H}/lab/manual.pdf'),
    ('Imaging', f'{H}/img/manual.pdf'),
    ('Admin', f'{H}/adm/manual.pdf'),
]
CSS = open(f'{H}/ml/style.css').read().replace('MediLink · Doctor User Manual', 'MediLink · User Manuals')


def outline(r):
    """[(title, page_index, [(subtitle, page_index), ...]), ...] skipping the TOC entry."""
    out = []
    for it in r.outline:
        if isinstance(it, list):
            out[-1][2].extend((s.title, r.get_destination_page_number(s)) for s in it if not isinstance(s, list))
        else:
            out.append([it.title, r.get_destination_page_number(it), []])
    return [o for o in out if o[0] != 'Table of Contents']


# ---- plan: front matter, then per part: its cover + body (from Section 1 to the end) ----
readers = [(role, PdfReader(p)) for role, p in PARTS]
plans = []
for role, r in readers:
    secs = outline(r)
    body_start = secs[0][1]
    plans.append(dict(role=role, r=r, secs=secs, body=list(range(body_start, len(r.pages)))))


def build_front(front_pages):
    """Return (pdf_bytes, n_pages, links) for cover + TOC given the number of front pages assumed."""
    page = front_pages + 1
    rows = []
    for k, pl in enumerate(plans, 1):
        pl['cover_no'] = page
        offset = page + 1 - pl['body'][0]  # new number = old index + offset
        pl['offset'] = offset
        rows.append(f'<div class="tp"><a href="https://p/{page}"><span>Part {k}&nbsp;&nbsp;{pl["role"]} User Manual</span><i></i><em>{page}</em></a></div>')
        n = 0
        for title, idx, subs in pl['secs']:
            n += 1
            lab = 'Appendix A' if title == 'Quick Reference' else f'Section {n}'
            rows.append(f'<div class="t1"><a href="https://p/{idx + offset}"><span>{lab}&nbsp;&nbsp;{title}</span><i></i><em>{idx + offset}</em></a></div>')
            for st, si in subs:
                rows.append(f'<div class="t2"><a href="https://p/{si + offset}"><span>{st}</span><i></i><em>{si + offset}</em></a></div>')
        page += 1 + len(pl['body'])
    roles = ' · '.join(p['role'] for p in plans)
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>MediLink: User Manuals</title><style>{CSS}
.toc .tp {{ margin-top: 6mm; font-weight: 800; color: #fff; background: var(--navy); font-size: 10.6pt; padding: 1.4mm 3mm; border-radius: 3px; break-after: avoid; }}
.toc .tp:first-of-type {{ margin-top: 2mm; }}
.toc .tp a i {{ border-bottom-color: rgba(255,255,255,.5); }}
.toc .t1 {{ break-after: avoid; }}
</style></head><body>
<section class="cover" style="background:#fff">
 <img class="seal" src="file://{H}/ml/fig/seal.png">
 <div class="ct">MediLink<br>Integrated Healthcare System</div>
 <div class="cs">User Manuals for All Roles</div>
 <div class="cu">{roles}</div>
 <div class="cu">medilink.oas.lguapp.com · Municipality of Oas, Albay</div>
 <img class="hero" src="file://{H}/ml/fig/cover.jpg" style="top:142mm">
 <div class="cm">Prepared by iConcept IT Solutions</div>
</section>
<section class="toc"><div class="kick">CONTENTS</div><h1>Table of Contents</h1><div class="rule"></div>{''.join(rows)}</section>
</body></html>'''
    with open(f'{ROOT}/front.html', 'w') as f: f.write(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        pg.goto(f'file://{ROOT}/front.html'); pg.wait_for_load_state('networkidle')
        data = pg.pdf(format='A4', print_background=True, prefer_css_page_size=True)
        b.close()
    return data, len(PdfReader(io.BytesIO(data)).pages)


n = 3
while True:
    front, got = build_front(n)
    if got == n: break
    n = got
front_r = PdfReader(io.BytesIO(front))


def number_overlay(numbers):
    """One overlay page per number: white patch over the old number, new number in the same place."""
    divs = ''.join(f'<section class="o"><span>{x}</span></section>' for x in numbers)
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 0; }} body {{ margin: 0; font-family: Inter, sans-serif; }}
.o {{ width: 210mm; height: 297mm; position: relative; page-break-after: always; }}
.o span {{ position: absolute; right: 17.45mm; bottom: 7.7mm; min-width: 14mm; text-align: right; background: #fff;
  font: 600 8pt Inter, sans-serif; color: #1b4f8a; padding: 0.6mm 0 0.6mm 2mm; line-height: 1; }}
</style></head><body>{divs}</body></html>'''
    with open(f'{ROOT}/overlay.html', 'w') as f: f.write(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        pg.goto(f'file://{ROOT}/overlay.html')
        data = pg.pdf(format='A4', print_background=True, prefer_css_page_size=True)
        b.close()
    return PdfReader(io.BytesIO(data))


w = PdfWriter()
for p in front_r.pages: w.add_page(p)
numbers = []
for pl in plans:
    w.add_page(pl['r'].pages[0])            # part cover (no number)
    numbers.append(None)
    for i in pl['body']:
        w.add_page(pl['r'].pages[i]); numbers.append(i + pl['offset'])
ov = number_overlay([x for x in numbers if x])
k = 0
for j, x in enumerate(numbers):
    if x is None: continue
    w.pages[len(front_r.pages) + j].merge_page(ov.pages[k]); k += 1

# TOC links: turn https://p/N links into jumps to page N
for pi in range(1, len(front_r.pages)):
    pg = w.pages[pi]
    for a in pg.get('/Annots', []) or []:
        a = a.get_object()
        act = a.get('/A')
        if act and act.get('/URI', '').startswith('https://p/'):
            target = int(act['/URI'].rsplit('/', 1)[1]) - 1
            a[NameObject('/A')] = DictionaryObject({
                NameObject('/S'): NameObject('/GoTo'),
                NameObject('/D'): ArrayObject([w.pages[target].indirect_reference, NameObject('/Fit')])})

# Bookmarks
w.add_outline_item('Table of Contents', 1)
for k, pl in enumerate(plans, 1):
    part = w.add_outline_item(f'Part {k}  {pl["role"]} User Manual', pl['cover_no'] - 1)
    for title, idx, subs in pl['secs']:
        s = w.add_outline_item(title, idx + pl['offset'] - 1, parent=part)
        for st, si in subs:
            w.add_outline_item(st, si + pl['offset'] - 1, parent=s)
w.add_metadata({'/Title': 'MediLink User Manuals (All Roles)', '/Author': 'iConcept IT Solutions'})
w.page_mode = '/UseOutlines'
out = f'{ROOT}/MediLink-User-Manuals-All-Roles.pdf'
w.compress_identical_objects(remove_identicals=True, remove_orphans=True)
w.write(out)
print('pages', len(w.pages), 'front', len(front_r.pages), {p['role']: p['cover_no'] for p in plans})
import subprocess
subprocess.run(['qpdf', '--object-streams=generate', '--compress-streams=y', '--recompress-flate', '--compression-level=9', out, '--replace-input'], check=True)
print('size', os.path.getsize(out))
