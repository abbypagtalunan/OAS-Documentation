import json, os, re, subprocess, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = json.load(open(f'{ROOT}/pages.json')) if os.path.exists(f'{ROOT}/pages.json') else {}

def pg(aid):
    return str(PAGES.get(aid, '')) if PAGES else ''

# ---------- content helpers ----------
SECTIONS = []   # (num, title, id, [(sub_num, sub_title, sub_id)])
body = []

def section(num, title, intro, subs):
    sid = f's{num}'
    SECTIONS.append((num, title, sid, subs))
    lis = ''.join(f'<li><a href="#{i}">{n} {t}</a></li>' for n, t, i in subs)
    body.append(f'''<section class="sec" id="{sid}">
<div class="kick">SECTION {num}</div><h1>{title}</h1><div class="rule"></div>
<p class="lead">{intro}</p>
<div class="inthis"><div class="ih">In this section</div><ul>{lis}</ul></div>''')

def appendix(letter, title, intro, sid):
    SECTIONS.append((letter, title, sid, []))
    body.append(f'''<section class="sec" id="{sid}"><div class="kick">APPENDIX {letter}</div><h1>{title}</h1><div class="rule"></div><p class="lead">{intro}</p>''')

def end(): body.append('</section>')

def h2(num, title, sid, brk=False):
    body.append(f'<h2 id="{sid}"{" class=brk" if brk else ""}>{num} {title}</h2>')

def p(t): body.append(f'<p>{t}</p>')

def steps(items): body.append('<ol class="steps">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>')

def bullets(items): body.append('<ul class="bul">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>')

FIGN = {}
def fig(name, cap, legend=None, size='full', sec=None):
    k = sec.split('.')[0]
    FIGN[k] = FIGN.get(k, 0) + 1
    n = f'{k}.{FIGN[k]}'
    leg = ''
    if legend:
        leg = '<div class="legend">' + ''.join(f'<span><b>{i+1}</b>{l}</span>' for i, l in enumerate(legend)) + '</div>'
    st = f' style="width:{size}%"' if isinstance(size,int) else ''
    body.append(f'<figure class="{size if not isinstance(size,int) else ""}"><img src="fig/{name}.jpg"{st}><figcaption><b>Figure {n}.</b> {cap}</figcaption>{leg}</figure>')

def table(head, rows, cls=''):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    body.append(f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>')

def call(kind, text):
    body.append(f'<div class="call {kind.lower()}"><b>{kind}</b> {text}</div>')

B = lambda t: f'<b>{t}</b>'

