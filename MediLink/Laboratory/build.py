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

# ================= CONTENT =================
section(1, 'Getting Started',
 'This section explains what the Laboratory role does in MediLink, how to sign in, and how the Laboratory screen is laid out.',
 [('1.1','About the Laboratory role','s1-1'),('1.2','Signing in','s1-2'),('1.3','The Laboratory screen','s1-3'),('1.4','Account menu and signing out','s1-4')])
h2('1.1','About the Laboratory role','s1-1')
p('MediLink, the Integrated Healthcare System of the Municipality of Oas, connects patients, doctors and the clinic\'s service units. The <b>Laboratory</b> role is used by the clinic laboratory (for example CBC and hematology tests). As laboratory staff you can:')
bullets(['find patients with laboratory requests;',
         'keep the list of laboratory tests and their rates up to date;',
         'set the items measured in each test and their normal values; and',
         'view the laboratory transactions, open a result and print it.'])
call('IMPORTANT','<b>Sample data only.</b> All names, tests, rates, results, normal values and contact details shown in this manual are sample data used for training. They are not real records or reference ranges.')
h2('1.2','Signing in','s1-2')
steps(['Open a web browser and go to <b>medilink.oas.lguapp.com</b>.',
       'On the MediLink home page, click <b>LOGIN</b> at the top right (Figure 1.1).',
       'Sign in with the laboratory account given to you by the system administrator.',
       'MediLink opens the <b>Patients</b> page (Section 2).'])
fig('f-home','The MediLink home page.',['LOGIN button'], size=80, sec='1')
h2('1.3','The Laboratory screen','s1-3')
fig('f-layout','The Laboratory screen.',['Top bar','Your photo, name and email','Main menu','Account menu','Work area'], sec='1')
table(['Part','What it does'],[
 ['1 Top bar','Shows that you are signed in with the <b>Laboratory</b> role.'],
 ['2 Your profile','Your photo, name and email.'],
 ['3 Main menu','<b>Patients</b> (Section 2), <b>Test</b> (Section 3) and <b>Report</b> (Section 4). The page you are on is shown in blue.'],
 ['4 Account menu','Click it for <b>Account</b> and <b>Logout</b> (1.4).'],
 ['5 Work area','The content of the page you opened.']])
h2('1.4','Account menu and signing out','s1-4')
fig('f-usermenu','The account menu at the top right.',['Account menu','Account','Logout'], size=60, sec='1')
bullets(['Click <b>Account</b> to change your profile, email or password (Section 5).','Click <b>Logout</b> to sign out. Always sign out when you leave a shared computer.'])
end()

section(2,'Patients',
 'The Patients page is where laboratory staff find the patients they need to serve.',
 [('2.1','The patient list','s2-1')])
h2('2.1','The patient list','s2-1')
p('Click <b>Patients</b> in the main menu. Type a patient\'s name in <b>Search patient</b> to find the patient in the <b>Patient List</b>.')
fig('f-patients','The Patient List.',['Patient List','Search patient'], size=55, sec='2')
end()

section(3,'Laboratory Tests',
 'The Test page lists the laboratory tests the clinic offers, their rates, and the normal values for each item a test measures. Doctors choose from this list when they request a test.',
 [('3.1','The test list','s3-1'),('3.2','Adding a test','s3-2'),('3.3','Changing a test or rate','s3-3'),('3.4','Test values and normal ranges','s3-4'),('3.5','Adding and changing a value','s3-5')])
h2('3.1','The test list','s3-1')
p('Click <b>Test</b> in the main menu. Each row shows the <b>Test</b> name and its <b>Rate</b> in pesos, for example <i>CBC</i> at 120 and <i>HEMATOLOGY</i> at 300. Each row has two action icons: <b>Edit</b> (3.3) and <b>Values</b> (3.4).')
fig('f-test','The Test page.',['New Test','Tests and rates','Edit','Values'], size=85, sec='3')
h2('3.2','Adding a test','s3-2')
steps(['Click <b>New Test</b>. The <b>Add Lab Test</b> panel opens on the right.','Type the <b>Test</b> name.','Type the <b>Rate</b>.','Click <b>CREATE</b>, or the <b>X</b> to close without saving.'])
fig('f-newtest','The Add Lab Test panel.',['Test','Rate','CREATE','Close'], size=50, sec='3')
h2('3.3','Changing a test or rate','s3-3')
steps(['Click the <b>Edit</b> icon on the test\'s row. The <b>Update Lab Test</b> panel opens with the current name and rate.','Change the <b>Test</b> name or the <b>Rate</b>.','Click <b>UPDATE</b>.'])
fig('f-edittest','The Update Lab Test panel.',['Test','Rate','UPDATE'], size=55, sec='3')
call('IMPORTANT','Doctors see the test name and rate when they request a test, so check new rates with the clinic before saving.')
h2('3.4','Test values and normal ranges','s3-4',brk=True)
p('A test can measure several items. For each item you record a <b>Description</b> and its <b>Normal Values</b>. These appear beside the patient\'s result (4.2), so the reader can compare the result with the normal range.')
steps(['Click the <b>Values</b> icon on the test\'s row. A <b>Values</b> table opens below the test list, for example <b>CBC Values</b> with <i>CBC 140 - 160</i> and <i>WBC 120 - 123</i>.',
       'Click <b>ADD NEW</b> to add an item (3.5), or the edit icon on an item to change it.',
       'Click <b>CLOSE</b> to hide the table.'])
fig('f-values','The Values table for CBC.',['Values icon','Items and normal values','ADD NEW','CLOSE','Edit value'], sec='3')
h2('3.5','Adding and changing a value','s3-5',brk=True)
p('<b>To add an item:</b>')
steps(['In the Values table, click <b>ADD NEW</b>. The <b>Add Values</b> panel opens on the right.','Type the <b>Description</b> (for example <i>WBC</i>).','Type the <b>Normal Values</b> range (for example <i>120 - 123</i>).','Click <b>CREATE</b>, or the <b>X</b> to close without saving.'])
fig('f-addvalue','The Add Values panel.',['Description','Normal Values','CREATE','Close'], size=50, sec='3')
p('<b>To change an item:</b>')
steps(['Click the edit icon on the item\'s row. The <b>Update Lab Value</b> panel opens with the current description and range.','Change the <b>Description</b> or <b>Normal Values</b>.','Click <b>UPDATE</b>.'])
fig('f-editvalue','The Update Lab Value panel.',['Description','Normal Values','UPDATE'], size=50, sec='3')
end()

section(4,'Report',
 'The Report page lists laboratory transactions so you can review collections and reprint results.',
 [('4.1','The transaction list','s4-1'),('4.2','Viewing and printing a result','s4-2')])
h2('4.1','The transaction list','s4-1')
p('Click <b>Report</b> in the main menu. Each row shows the <b>Date</b>, <b>Transaction ID</b> and <b>Amount</b>. The <b>Total</b> of all listed amounts is shown at the bottom (in the sample, four transactions of 420 for a total of 1680).')
fig('f-report','The Reports page.',['Transactions','Print (open the result)','Total'], sec='4')
h2('4.2','Viewing and printing a result','s4-2',brk=True)
steps(['Click the printer icon on a transaction. The result opens with one block per test, for example <i>HEMATOLOGY</i> and <i>CBC</i>. Each block lists the <b>Description</b>, the patient\'s <b>Result</b> and the <b>Normal Values</b>.',
       'Click <b>DETAILS</b> under a test to see its printable copy, headed with the clinic\'s name and address.',
       'Click <b>PRINT</b> to print it.',
       'Press <b>Esc</b> or click outside the window to close it.'])
fig('f-result','A result with two tests.',['Hematology results','DETAILS','CBC results'], size=72, sec='4')
fig('f-resultprint','The printable result.',['Printable copy','PRINT'], size=72, sec='4')
end()

section(5,'Account Settings',
 'Use Account settings to keep your profile, email and password up to date.',
 [('5.1','Profile','s5-1'),('5.2','Changing your email','s5-2'),('5.3','Changing your password','s5-3')])
h2('5.1','Profile','s5-1')
p('Open <b>Account</b> from the account menu (1.4). The <b>Settings</b> page has three tabs: <b>General</b>, <b>Email</b> and <b>Security</b>.')
fig('f-account','Account settings, General tab.',['GENERAL, EMAIL and SECURITY tabs','Photo and UPLOAD PROFILE','Profile details','SAVE CHANGES'], sec='5')
steps(['To change your photo, click <b>UPLOAD PROFILE</b> and choose an image.','Edit your <b>First Name</b>, <b>Last Name</b>, <b>Phone Number</b>, <b>State</b> and <b>Country</b>.','Click <b>SAVE CHANGES</b>.'])
h2('5.2','Changing your email','s5-2')
fig('f-email','The Email tab.',['Current Email','New Email','CHANGE EMAIL'], sec='5')
steps(['Click the <b>EMAIL</b> tab.','Type your <b>New Email</b>.','Click <b>CHANGE EMAIL</b>.'])
h2('5.3','Changing your password','s5-3')
fig('f-security','The Security tab.',['Password','Password Confirmation','CHANGE PASSWORD'], sec='5')
steps(['Click the <b>SECURITY</b> tab.','Type the new <b>Password</b>, and type it again in <b>Password Confirmation</b>.','Click <b>CHANGE PASSWORD</b>.'])
end()

appendix('A','Quick Reference','Where to go for common tasks.','sa')
table(['I want to…','Go to','See'],[
 ['Find a patient','Patients › Search patient','2.1'],
 ['Add a laboratory test','Test › New Test › CREATE','3.2'],
 ['Change a test rate','Test › Edit icon › UPDATE','3.3'],
 ['See a test\'s normal values','Test › Values icon','3.4'],
 ['Add a normal value','Test › Values icon › ADD NEW › CREATE','3.5'],
 ['Change a normal value','Test › Values icon › edit icon › UPDATE','3.5'],
 ['See collections','Report','4.1'],
 ['Reprint a result','Report › printer icon › DETAILS › PRINT','4.2'],
 ['Change my password','Account › SECURITY','5.3']], cls='w3')
end()
# ---------- TOC ----------
toc = []
for num, title, sid, subs in SECTIONS:
    lab = f'Section {num}' if isinstance(num, int) else f'Appendix {num}'
    toc.append(f'<div class="t1"><a href="#{sid}"><span>{lab}&nbsp;&nbsp;{title}</span><i></i><em>{pg(sid)}</em></a></div>')
    for n, t, i in subs:
        toc.append(f'<div class="t2"><a href="#{i}"><span>{n}&nbsp;&nbsp;{t}</span><i></i><em>{pg(i)}</em></a></div>')

CSS = open(f'{ROOT}/style.css').read()
html = f'''<!doctype html><html><head><meta charset="utf-8"><title>MediLink: Laboratory User Manual</title><style>{CSS}</style></head><body>
<section class="cover">
 <img class="seal" src="fig/seal.png">
 <div class="ct">MediLink<br>Integrated Healthcare System</div>
 <div class="cs">User Manual for Laboratory Staff</div>
 <div class="cu">medilink.oas.lguapp.com · Municipality of Oas, Albay</div>
 <img class="hero" src="fig/cover.jpg">
 <div class="cm">Prepared by iConcept IT Solutions</div>
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
