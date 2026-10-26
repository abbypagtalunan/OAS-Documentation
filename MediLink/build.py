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
 'This section explains what MediLink is, how a doctor signs in, and how the Doctor screen is laid out.',
 [('1.1','About MediLink','s1-1'),('1.2','Signing in','s1-2'),('1.3','The Doctor screen','s1-3'),('1.4','Account menu and signing out','s1-4')])
h2('1.1','About MediLink','s1-1')
p('MediLink, the Integrated Healthcare System of the Municipality of Oas, connects patients with the Municipal Health Office. Residents book appointments online; doctors use MediLink to see their schedule, open each patient\'s record, and write findings, orders and prescriptions in one place.')
p('As a <b>Doctor</b> you can:')
bullets(['see your appointments in a calendar (month, week, day or agenda list);',
         'find a patient and open the patient\'s full record;',
         'record vital signs, medication, allergies, diagnosis, diet advice, pain areas, notes and treatment plans;',
         'write prescriptions, and request laboratory and imaging tests;',
         'view laboratory and imaging results and attachments;',
         'mark an appointment as complete;',
         'manage the list of services you offer and their fees; and',
         'view a report of your consultations.'])
call('IMPORTANT','<b>Sample data only.</b> All patients, doctors, appointments, results, prices and pharmacies shown in this manual are sample data used for training. They are not real records.')
h2('1.2','Signing in','s1-2')
steps(['Open a web browser and go to <b>medilink.oas.lguapp.com</b>.',
       'The MediLink home page opens. Click <b>LOGIN</b> at the top right (Figure 1.1).',
       'Sign in with the doctor account given to you by the system administrator.',
       'After signing in, MediLink opens the <b>Appointment</b> calendar (see Section 2).'])
fig('f-home','The MediLink home page.',['LOGIN button'], sec='1')
call('IMPORTANT','Keep your password private. Each doctor must sign in with his or her own account so that every record shows who entered it.')
h2('1.3','The Doctor screen','s1-3')
p('Every page for the doctor has the same frame (Figure 1.2).')
fig('f-layout','The Doctor screen, showing the Appointment calendar.',['Top bar','Your profile (photo, name and email)','Main menu','Account menu','Work area'], sec='1')
table(['Part','What it does'],[
 ['1 Top bar','Shows that you are signed in with the <b>Doctor</b> role.'],
 ['2 Your profile','Your photo, name and email. Click your photo or name to open your account settings (Section 9).'],
 ['3 Main menu','<b>Appointment</b> (Section 2), <b>Patient List</b> (Section 3), <b>Services</b> (Section 7) and <b>Reports</b> (Section 8). The page you are on is shown in blue.'],
 ['4 Account menu','Your name at the top right. Click it for <b>Account</b> and <b>Logout</b> (1.4).'],
 ['5 Work area','The content of the page you opened.']])
h2('1.4','Account menu and signing out','s1-4')
fig('f-usermenu','The account menu at the top right.',['Your name (click to open the menu)','Account','Logout'], size=60, sec='1')
bullets(['Click <b>Account</b> to change your profile, email or password (Section 9).',
         'Click <b>Logout</b> to sign out. Always sign out when you leave a shared computer.'])
end()

section(2,'Appointments',
 'The Appointment page is a calendar of the consultations booked with you. From an appointment you can open the patient\'s record.',
 [('2.1','The appointment calendar','s2-1'),('2.2','Week, Day and Agenda views','s2-2'),('2.3','Viewing an appointment','s2-3')])
h2('2.1','The appointment calendar','s2-1')
p('Click <b>Appointment</b> in the main menu. The calendar opens on the current month. Each appointment appears on its date as a blue bar with the time, the service and the patient\'s name.')
fig('f-month','The calendar in Month view.',['PREV, TODAY and NEXT buttons','Month shown','View buttons: Month, Week, Day, Agenda','Appointments'], sec='2')
bullets(['Click <b>PREV</b> or <b>NEXT</b> to move to the previous or next month (or week or day, depending on the view).',
         'Click <b>TODAY</b> to return to the current date. Today is shaded in the calendar.',
         'Click an appointment to see its details (2.3).'])
h2('2.2','Week, Day and Agenda views','s2-2')
p('Use the four buttons at the top right of the calendar to change the view.')
table(['Button','View','Use it to'],[
 ['First','Month','See the whole month at a glance (Figure 2.1).'],
 ['Second','Week','See one week by hour, Sunday to Saturday (Figure 2.2).'],
 ['Third','Day','See one day by hour (Figure 2.3).'],
 ['Fourth','Agenda','See a list of the month\'s appointments grouped by date, with the time of each (Figure 2.4).']], cls='w3')
fig('f-week','Week view.',['Week button','Appointments placed at their time'], size=88, sec='2')
fig('f-day','Day view.',['Day button','Appointment'], size=88, sec='2')
fig('f-agenda','Agenda view.',['Agenda button','Appointments listed by date'], size=88, sec='2')
call('NOTE','In Week and Day views, scroll inside the calendar to see earlier or later hours.')
h2('2.3','Viewing an appointment','s2-3')
p('Click an appointment in any view. A <b>Details</b> panel opens on the right.')
fig('f-apptdetails','Appointment details.',['Patient first and last name, service, reason and status','VIEW PATIENT PROFILE','Close (X)'], sec='2')
table(['Field','What it shows'],[['Firstname / Lastname','The patient who booked the appointment.'],['Service','The service booked, for example <i>check-up</i>.'],['Reason','The reason the patient gave when booking.'],['Status','<b>Incomplete</b> until you mark the appointment complete (4.1).']])
steps(['Click <b>VIEW PATIENT PROFILE</b> to open the patient\'s record (3.2).','Or click <b>X</b> to close the panel.'])
end()

section(3,'Patient List',
 'The Patient List shows all of your patients. From here you open a patient\'s record.',
 [('3.1','Finding a patient','s3-1'),('3.2','The patient record page','s3-2')])
h2('3.1','Finding a patient','s3-1')
p('Click <b>Patient List</b> in the main menu.')
fig('f-patients','The Patients page.',['Search box','Patient list (name, address, gender)','DETAILS button'], sec='3')
steps(['To find a patient quickly, type part of the patient\'s name in the <b>Search</b> box. The list narrows as you type (Figure 3.2).',
       'Click <b>DETAILS</b> on the patient\'s row to open the patient record.'])
fig('f-patientsearch','Searching for a patient by name.',['Search text','Matching patients'], sec='3')
h2('3.2','The patient record page','s3-2')
p('The patient record page is where you do most of your work. It opens from <b>DETAILS</b> in the Patient List or from <b>VIEW PATIENT PROFILE</b> on an appointment.')
fig('f-profile','The patient record page.',['Patient card: name, birth date, sex, contact number','BACK button','Record tabs','Contents of the open tab','Next Action button'], size=88, sec='3')
p('The tabs across the page give you each part of the record. If not all tabs fit, click the arrow (›) at the end of the row to see the rest.')
table(['Tab','What it is for','See'],[
 ['Appointments','The patient\'s appointments with you, and marking them complete.','4.1'],
 ['Information','The patient\'s personal details.','4.2'],
 ['Health Record','Vital signs, medication, allergies, diagnosis, diet, pain and vitals monitoring.','4.3 – 4.9'],
 ['Notes','Consultation notes with the initial diagnosis.','5.1'],
 ['Prescriptions','Writing and viewing prescriptions.','5.3'],
 ['Treatment Plan','Scheduled treatment plans.','5.2'],
 ['Laboratory','Laboratory requests and results.','Section 6'],
 ['Imaging','Imaging requests (for example ECG, X-ray) and results.','Section 6']], cls='w3')
p('Click <b>BACK</b> to return to the previous page.')
end()

section(4,'Appointments, Information and Health Record',
 'These tabs hold the patient\'s visits, personal details and health record.',
 [('4.1','Appointments tab and completing an appointment','s4-1'),('4.2','Information tab','s4-2'),('4.3','Health Record and Pre-Lab','s4-3'),('4.4','Medication','s4-4'),('4.5','Allergies','s4-5'),('4.6','Diagnosis','s4-6'),('4.7','Diet','s4-7'),('4.8','Pain Monitoring','s4-8'),('4.9','Vitals Monitoring','s4-9')])
h2('4.1','Appointments tab and completing an appointment','s4-1')
p('The <b>Appointments</b> tab lists the patient\'s appointments with the date and time, service and status (Figure 3.3). When you finish a consultation, mark it complete:')
steps(['On the appointment row, click the arrow under <b>Next Action</b>.',
       'A <b>Details</b> panel shows the service, its amount (fee) and the reason for the visit.',
       'Click <b>SET COMPLETE</b> to mark the consultation as done.'])
fig('f-nextaction','Completing an appointment.',['Service, amount and reason','SET COMPLETE button'], size=82, sec='4')
p('Clicking <b>SET COMPLETE</b> opens the <b>Set Complete</b> window. Choose whether the patient needs a follow-up in <b>Select Option</b> (required).')
fig('f-sc-options','The Select Option list.',['NO FOLLOW-UP or SET FOLLOW-UP'], size=50, sec='4')
p('<b>No follow-up needed:</b>')
steps(['Choose <b>NO FOLLOW-UP</b>.','Click <b>SET COMPLETE</b>.'])
fig('f-sc-none','Completing without a follow-up.',['Select Option: NO FOLLOW-UP','SET COMPLETE'], size=50, sec='4')
p('<b>Patient should come back:</b>')
steps(['Choose <b>SET FOLLOW-UP</b>. A <b>Description</b> box and a calendar appear.',
       'Type the reason in <b>Description</b> (required), for example <i>New Prescription</i>.',
       'Pick the follow-up date on the calendar. Use the arrows to change the month.',
       'Click <b>SET COMPLETE</b>.'])
fig('f-sc-follow','Completing with a follow-up.',['Select Option: SET FOLLOW-UP','Description','Follow-up date','SET COMPLETE'], size=48, sec='4')
p('A green message <i>Appointment successfully updated.</i> confirms it, and the appointment\'s status changes to <b>COMPLETED</b> on the Appointments tab.')
fig('f-sc-done','The completed appointments.',['Status: COMPLETED','Next Action'], sec='4')
call('WARNING','Click <b>SET COMPLETE</b> only after the consultation is finished.')
h2('4.2','Information tab','s4-2')
p('The <b>Information</b> tab shows the patient\'s personal details: first name, last name, middle name, civil status, street, barangay, city, contact number and religion. You can view these details but not change them here.')
fig('f-info','The Information tab.',['Patient details'], sec='4')
h2('4.3','Health Record and Pre-Lab','s4-3')
p('The <b>Health Record</b> tab has its own menu on the left: <b>Pre-Lab</b>, <b>Medication</b>, <b>Allergies</b>, <b>Diagnosis</b>, <b>Diet</b>, <b>Pain Monitoring</b> and <b>Vitals Monitoring</b>. It opens on <b>Pre-Lab</b>, which shows the patient\'s current health record.')
fig('f-hr','Health Record, Pre-Lab.',['Health Record menu','Current health record','UPDATE button'], sec='4')
p('The current health record shows temperature (℃), weight (kg), blood pressure systolic and diastolic (mmHg), glucose, heart rate, uric acid, respiratory rate and cholesterol. <b>None</b> means no value has been entered. To record new readings:')
steps(['Click <b>UPDATE</b>. The <b>Update Health Records</b> panel opens with the current values.',
       'Type the new readings in the fields you measured.',
       'Click <b>UPDATE</b> to save, or <b>CLOSE</b> to leave without saving.'])
fig('f-hrupdate','The Update Health Records panel.',['Readings','CLOSE and UPDATE buttons'], size=55, sec='4')
h2('4.4','Medication','s4-4')
p('<b>Medication</b> lists the medicines the patient should take and when.')
fig('f-med','Medication.',['NEW MEDICATION button','Medication list'], sec='4')
steps(['Click <b>NEW MEDICATION</b>.',
       'Under <b>Meals</b>, choose when the medicine is taken: Before or After Breakfast, Lunch or Dinner.',
       'Under <b>Description</b>, type the medicine and dose. Use the toolbar for bold, italic, underline, links and lists.',
       'Click <b>ADD</b>, or <b>CLOSE</b> to cancel.'])
fig('f-mednew','The New Medication panel.',['Meals','Description','ADD button'], size=62, sec='4')
h2('4.5','Allergies','s4-5')
p('<b>Allergies</b> shows the patient\'s known allergies, for example <i>Penicillin</i>, in a text box with a formatting toolbar. Check this before prescribing.')
fig('f-allergy','Allergies.',['Allergies','Formatting toolbar'], sec='4')
call('NOTE','No Save button was shown on the Allergies screen when this manual was prepared. Confirm with the administrator how changes to allergies are saved.')
h2('4.6','Diagnosis','s4-6')
p('<b>Diagnosis</b> lists the diagnoses recorded for the patient, for example <i>Urinary Tract Infection</i>.')
fig('f-diag','Diagnosis.',['NEW DIAGNOSIS button','View','Edit','Delete'], sec='4')
steps(['To add a diagnosis, click <b>NEW DIAGNOSIS</b>, type the <b>Diagnosis</b> and any <b>Remarks</b>, then click <b>ADD</b>.',
       'To read a diagnosis in full, click the view icon (2).',
       'To correct one, click the edit icon (3), change the text and click <b>SAVE</b>.',
       'The bin icon (4) deletes the diagnosis.'])
fig('f-diagnew','The Add diagnosis panel.',['Diagnosis','Remarks','ADD button'], size=62, sec='4')
call('WARNING','Deleting a diagnosis removes it from the patient\'s record. Delete only an entry made by mistake.')
h2('4.7','Diet','s4-7')
p('<b>Diet</b> holds the diet you suggest for the patient.')
steps(['Click <b>NEW DIET</b>.',
       'Under <b>Meals</b>, choose <i>Breakfast</i>, <i>Lunch</i>, <i>Dinner</i> or <i>Snacks</i>.',
       'Type the advice under <b>Description</b>.',
       'Click <b>ADD</b>, or <b>CLOSE</b> to cancel.'])
fig('f-dietnew','The New diet panel.',['Meals','Description','ADD button'], size=62, sec='4')
h2('4.8','Pain Monitoring','s4-8')
p('<b>Pain Monitoring</b> shows a body chart and a list of the pain the patient reported, with the date, description, pain level and whether the area is on the front or back of the body.')
fig('f-pain','Pain Monitoring in add mode.',['ADD button','Body chart','BACK / FRONT switch','CLOSE and SAVE buttons','Pain records'], sec='4')
steps(['Click <b>ADD</b>. The message <i>Select part of the body which is in pain and rate it by saving it</i> appears above the chart.',
       'Click <b>BACK</b> to show the back of the body, or <b>FRONT</b> to return to the front.',
       'Click the part of the body where the patient feels pain and rate it.',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
call('NOTE','The rating step after clicking the body was not tested for this manual, so the screen that asks for the pain level is not shown.')
h2('4.9','Vitals Monitoring','s4-9')
p('<b>Vitals Monitoring</b> charts the patient\'s readings over time. Choose a reading at the top: <b>BP</b>, <b>Temperature</b>, <b>Weight</b>, <b>Cholesterol</b>, <b>Glucose</b>, <b>Heart Pulse</b>, <b>Uric Acid</b> or <b>Respiratory</b>. The chart title shows how many tests are recorded.')
fig('f-vitals','Vitals Monitoring.',['Readings','Chart'], sec='4')
end()

section(5,'Notes, Treatment Plan and Prescriptions',
 'Use these tabs to write consultation notes, plan treatment and prescribe medicines.',
 [('5.1','Notes','s5-1'),('5.2','Treatment Plan','s5-2'),('5.3','Prescriptions','s5-3')])
h2('5.1','Notes','s5-1')
p('The <b>Notes</b> tab lists your consultation notes by date with the initial diagnosis.')
fig('f-notes','The Notes tab.',['NEW NOTES button','Notes list'], sec='5')
steps(['Click <b>NEW NOTES</b>.','Type the <b>Initial Diagnosis</b>.','Type your findings under <b>Notes</b>.','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-notesnew','The New notes panel.',['Initial Diagnosis','Notes','SAVE button'], size=62, sec='5')
h2('5.2','Treatment Plan','s5-2')
p('The <b>Treatment Plan</b> tab lists planned treatments with their schedule.')
fig('f-tp','The Treatment Plan tab.',['NEW TREATMENT PLAN button','Treatment plans'], sec='5')
steps(['Click <b>NEW TREATMENT PLAN</b>.','Check the <b>Schedule Date</b>. It starts with the current date and time; change it to the planned date.','Type the plan under <b>Treatment Plan</b>.','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-tpnew','The New treatment plan panel.',['Schedule Date','Treatment Plan','SAVE button'], size=62, sec='5')
h2('5.3','Prescriptions','s5-3')
p('The <b>Prescriptions</b> tab has three parts on the left:')
table(['Part','What it is for'],[['LIST','Saved prescriptions, with date and prescription number.'],['CLINIC','A prescription for a pharmacy chosen from the list (for example TGP or Malolos Pharmacy).'],['UNSAVED','A prescription you are still building. Add products, then save it.']])
fig('f-rx','The Prescriptions tab, LIST.',['LIST, CLINIC and UNSAVED','Saved prescriptions'], sec='5')
p('<b>To write a prescription:</b>')
steps(['Click <b>UNSAVED</b>.',
       'Click <b>ADD PRODUCT</b>. Type the <b>Product Name</b>, choose the <b>Type</b> (Bottle, Box, Can, Capsule, Liniment, Sachet, Suspension, Powder or Tablet), type the <b>Quantity</b> and the <b>Instruction</b> (sig), then click <b>ADD TO UNSAVE</b>.',
       'Repeat for each medicine. Each one appears in the list with its quantity, type and sig.',
       'Click <b>SAVE PRESCRIPTION</b>. Saved prescriptions are listed under <b>LIST</b>.'])
fig('f-rxunsaved','Building a prescription (UNSAVED).',['Products added so far','ADD PRODUCT','SAVE PRESCRIPTION'], sec='5')
fig('f-rxadd','The Set Product To Unsave window.',['Product Name','Type','Quantity','Instruction (sig)','ADD TO UNSAVE'], size=46, sec='5')
p('<b>For a pharmacy:</b> click <b>CLINIC</b>, choose the pharmacy under <b>Select Pharmacy</b>, then add products and save the same way.')
fig('f-rxclinic','A prescription for a pharmacy (CLINIC).',['Select Pharmacy','ADD PRODUCT','SAVE PRESCRIPTION'], sec='5')
call('NOTE','<b>SAVE PRESCRIPTION</b> stays grey until at least one product has been added.')
end()

section(6,'Laboratory and Imaging',
 'The Laboratory and Imaging tabs work the same way: request tests, then view the results and attached files.',
 [('6.1','Viewing results','s6-1'),('6.2','Requesting tests','s6-2'),('6.3','Attachments','s6-3')])
h2('6.1','Viewing results','s6-1')
p('Open the <b>Laboratory</b> or <b>Imaging</b> tab (use the › arrow on the tab row if needed). <b>LIST</b> shows each result with its date and ID.')
fig('f-lab','The Laboratory tab, LIST.',['LIST, UNSAVED and ATTACHMENTS','Results','Open result'], sec='6')
steps(['Click the document icon under <b>Action</b> on a row.',
       'The result opens. Laboratory results show each test (for example Hematology or CBC) with its description, result and normal values. Imaging results (for example ECG) show the result and impression.',
       'Click <b>DETAILS</b> to see the printable copy, then <b>PRINT</b> to print it.',
       'Click outside the window to close it.'])
fig('f-labresult','A laboratory result.',['Test with result and normal values','DETAILS button'], size=80, sec='6')
fig('f-imgresult','An imaging result (ECG).',['DETAILS button'], size=80, sec='6')
fig('f-imgprint','The printable result.',['PRINT button'], size=80, sec='6')
h2('6.2','Requesting tests','s6-2')
steps(['In the Laboratory or Imaging tab, click <b>UNSAVED</b>.',
       'Click <b>ADD TEST</b>.',
       'Under <b>Select Test</b>, choose the test. Each test shows its rate, for example <i>CBC - 120</i> or <i>Hematology - 300</i> in Laboratory, and <i>ECG - 120</i> or <i>X-ray - 220</i> in Imaging.',
       'Click <b>ADD TO UNSAVE</b>. The test appears in the list with its rate.',
       'Add more tests if needed, then click <b>CONFIRM ALL</b> to confirm the requests.'])
fig('f-unsaved','Requesting tests (UNSAVED).',['UNSAVED','Tests added so far','ADD TEST','CONFIRM ALL'], sec='6')
fig('f-addtest','The Set Test To Unsave window.',['Select Test','ADD TO UNSAVE'], size=46, sec='6')
call('NOTE','<b>CONFIRM ALL</b> stays grey until at least one test has been added.')
h2('6.3','Attachments','s6-3')
p('<b>ATTACHMENTS</b> lists files attached to the patient\'s laboratory or imaging record, with the date and who added them (for example <i>patient</i>, <i>imaging</i> or <i>secretary</i>). Use the arrows at the bottom to page through the list and <b>List</b> to choose how many rows to show.')
fig('f-attach','Imaging attachments.',['ATTACHMENTS','Attached files'], sec='6')
end()

section(7,'Services',
 'The Services page lists the services you offer to patients and their fees.',
 [('7.1','Viewing and searching services','s7-1'),('7.2','Adding or changing a service','s7-2'),('7.3','Removing a service','s7-3')])
h2('7.1','Viewing and searching services','s7-1')
p('Click <b>Services</b> in the main menu.')
fig('f-services','The Services page.',['Search service','NEW SERVICE','View','Edit','Delete'], size=88, sec='7')
bullets(['Type in <b>Search service</b> to find a service by name.',
         'Click the view icon (3) to see a service\'s name and amount. A <b>Details</b> panel opens on the right; click <b>X</b> to close it.'])
fig('f-svc-details','The service Details panel.',['Service and Amount','Close (X)'], size=55, sec='7')
h2('7.2','Adding or changing a service','s7-2')
steps(['Click <b>NEW SERVICE</b>, or the edit icon (4) on a service.',
       'Type the <b>Service</b> name and the <b>Amount</b> (fee).',
       'Click <b>SAVE</b> (or <b>UPDATE SERVICE</b> when editing). Click <b>CLOSE</b> to cancel.'])
fig('f-servicenew','The New service panel.',['Service','Amount','SAVE button'], size=48, sec='7')
p('<b>To change a service:</b> click the edit icon (4). The <b>Edit</b> panel opens with the current name and amount. Change them and click <b>UPDATE SERVICE</b>, or <b>CLOSE</b> to cancel.')
fig('f-svc-edit','The Edit panel.',['SERVICE','AMOUNT','CLOSE and UPDATE SERVICE'], size=55, sec='7')
h2('7.3','Removing a service','s7-3')
p('Click the bin icon (5) on the service. A green message <i>Service successfully removed.</i> confirms it, and the service is no longer listed. In the example below, <i>check-up</i> was removed and only <i>physical examination</i> is left.')
fig('f-svc-removed','The Services list after removing a service.',['Remaining services','View, Edit and Delete icons'], sec='7')
call('WARNING','Delete only a service you no longer offer.')
end()

section(8,'Reports',
 'The Reports page lists your consultations with the service and rate, so you can review your work.',
 [('8.1','Viewing the report','s8-1')])
h2('8.1','Viewing the report','s8-1')
p('Click <b>Reports</b> in the main menu. Each row shows the <b>Date</b>, <b>Patient</b>, <b>Service</b> and <b>Rate</b>.')
fig('f-reports','The Reports page.',['Search report','Consultations'], sec='8')
p('Type in <b>Search report</b> to filter the list. The search matches the patient\'s name or the service; for example, <i>physical</i> shows only physical examinations.')
end()

section(9,'Account Settings',
 'Use Account settings to keep your profile, email and password up to date.',
 [('9.1','Profile','s9-1'),('9.2','Changing your email','s9-2'),('9.3','Changing your password','s9-3')])
h2('9.1','Profile','s9-1')
p('Open <b>Account</b> from the account menu (1.4), or click your photo or name in the profile area. The <b>Settings</b> page has three tabs: <b>General</b>, <b>Email</b> and <b>Security</b>.')
fig('f-account','Account settings, General tab.',['GENERAL, EMAIL and SECURITY tabs','Photo and UPLOAD PROFILE','Profile details','SAVE CHANGES'], sec='9')
steps(['To change your photo, click <b>UPLOAD PROFILE</b> and choose an image.',
       'Edit your <b>First Name</b>, <b>Last Name</b>, <b>Phone Number</b>, <b>State</b> and <b>Country</b>. Fields marked * are required.',
       'Click <b>SAVE CHANGES</b>.'])
h2('9.2','Changing your email','s9-2')
fig('f-email','The Email tab.',['Current Email','New Email','CHANGE EMAIL'], sec='9')
steps(['Click the <b>EMAIL</b> tab. Your current email is shown.','Type your <b>New Email</b>.','Click <b>CHANGE EMAIL</b>.'])
h2('9.3','Changing your password','s9-3')
fig('f-security','The Security tab.',['Password','Password Confirmation','CHANGE PASSWORD'], sec='9')
steps(['Click the <b>SECURITY</b> tab.','Type the new <b>Password</b>, and type it again in <b>Password Confirmation</b>.','Click <b>CHANGE PASSWORD</b>.'])
call('IMPORTANT','Use a password that others cannot guess, and change it right away if you think someone else knows it.')
end()

appendix('A','Quick Reference','Where to go for common tasks.','sa')
table(['I want to…','Go to','See'],[
 ['See today\'s appointments','Appointment › TODAY › Day view','2.1, 2.2'],
 ['Open a patient\'s record','Patient List › DETAILS, or an appointment › VIEW PATIENT PROFILE','3.1, 2.3'],
 ['Record vital signs','Health Record › Pre-Lab › UPDATE','4.3'],
 ['Add a diagnosis','Health Record › Diagnosis › NEW DIAGNOSIS','4.6'],
 ['Write consultation notes','Notes › NEW NOTES','5.1'],
 ['Write a prescription','Prescriptions › UNSAVED › ADD PRODUCT › SAVE PRESCRIPTION','5.3'],
 ['Request a laboratory or imaging test','Laboratory or Imaging › UNSAVED › ADD TEST › CONFIRM ALL','6.2'],
 ['View a test result','Laboratory or Imaging › LIST › document icon','6.1'],
 ['Finish a consultation','Appointments tab › Next Action › SET COMPLETE','4.1'],
 ['Change a service fee','Services › edit icon','7.2'],
 ['Change my password','Account › SECURITY','9.3']], cls='w3')
end()
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
