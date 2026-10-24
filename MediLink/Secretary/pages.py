import re, json
from pypdf import PdfReader
r=PdfReader('manual.pdf'); flat=[]
def walk(o):
    for it in o:
        if isinstance(it,list): walk(it)
        else: flat.append(r.get_destination_page_number(it)+1)
walk(r.outline)
html=open('manual.html').read()
ids=re.findall(r'<(?:h2|section class="sec")[^>]* id="([^"]+)"|<h2 id="([^"]+)"',html)
ids=[a or b for a,b in ids]
ids=[i for i in re.findall(r'id="(s[0-9ab][^"]*)"',html) if i!='toc']
json.dump(dict(zip(ids,flat[1:])),open('pages.json','w')); print(dict(zip(ids,flat[1:])))
