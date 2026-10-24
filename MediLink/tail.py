# ---------- TOC ----------
toc = []
for num, title, sid, subs in SECTIONS:
    lab = f'Section {num}' if isinstance(num, int) else f'Appendix {num}'
    toc.append(f'<div class="t1"><a href="#{sid}"><span>{lab}&nbsp;&nbsp;{title}</span><i></i><em>{pg(sid)}</em></a></div>')
    for n, t, i in subs:
        toc.append(f'<div class="t2"><a href="#{i}"><span>{n}&nbsp;&nbsp;{t}</span><i></i><em>{pg(i)}</em></a></div>')

CSS = open(f'{ROOT}/style.css').read()
html = f'''<!doctype html><html><head><meta charset="utf-8"><title>MediLink: Doctor User Manual</title><style>{CSS}</style></head><body>
<section class="cover">
 <img class="seal" src="fig/seal.png">
 <div class="ct">MediLink<br>Integrated Healthcare System</div>
 <div class="cs">User Manual for Doctors</div>
 <div class="cu">medilink.oas.lguapp.com · Municipality of Oas, Albay</div>
 <img class="hero" src="fig/f-home.jpg">
 <div class="cm">Prepared by iConcept IT Solutions<br>Draft, 24 October 2026<br>All data shown is sample data only</div>
</section>
<section class="toc" id="toc"><div class="kick">CONTENTS</div><h1>Table of Contents</h1><div class="rule"></div>{''.join(toc)}</section>
{''.join(body)}
</body></html>'''
open(f'{ROOT}/manual.html', 'w').write(html)

out = sys.argv[1] if len(sys.argv) > 1 else f'{ROOT}/manual.pdf'
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg_ = b.new_page()
    pg_.goto(f'file://{ROOT}/manual.html')
    pg_.wait_for_load_state('networkidle')
    pg_.pdf(path=out, format='A4', print_background=True, prefer_css_page_size=True, outline=True, tagged=True)
    b.close()
print('built', out)
