# ================= CONTENT =================
section(1, 'Getting Started',
 'This section explains what the Admin role does in MediLink, how to sign in, and how the Admin screen is laid out.',
 [('1.1','About the Admin role','s1-1'),('1.2','Signing in','s1-2'),('1.3','The Admin screen','s1-3'),('1.4','Account menu and signing out','s1-4')])
h2('1.1','About the Admin role','s1-1')
p('MediLink, the Integrated Healthcare System of the Municipality of Oas, connects patients, doctors and the clinic\'s service units. The <b>Admin</b> role sets up the system that the other roles work in. As an administrator you can:')
bullets(['add clinics, record their schedule, contact details, map location and photo;',
         'assign doctors to a clinic and create the clinic\'s Secretary, Laboratory and Imaging accounts;',
         'add pharmacies and create their Admin, Assistant and Pharmacist accounts;',
         'add doctors with their license numbers, photo and e-signature, and give them a username and password; and',
         'keep the list of medical specializations up to date.'])
call('IMPORTANT','<b>Sample data only.</b> All clinics, pharmacies, doctors, staff, numbers and contact details shown in this manual are sample data used for training. They are not real records.')
call('NOTE','Screens in this manual were captured from the live system on 24 October 2026 with an admin account. Forms were opened for the screenshots and closed without saving, so nothing was created or changed.')
h2('1.2','Signing in','s1-2')
steps(['Open a web browser and go to <b>medilink.oas.lguapp.com</b>.',
       'On the MediLink home page, click <b>LOGIN</b> at the top right (Figure 1.1).',
       'Sign in with your administrator account.',
       'MediLink opens the <b>Clinics</b> page (Section 2).'])
fig('f-home','The MediLink home page.',['LOGIN button'], size=80, sec='1')
h2('1.3','The Admin screen','s1-3')
fig('f-layout','The Admin screen.',['Top bar','Your photo, name and email','Main menu','Account menu','Work area'], sec='1')
table(['Part','What it does'],[
 ['1 Top bar','Shows that you are signed in with the <b>Admin</b> role.'],
 ['2 Your profile','Your photo, name and email.'],
 ['3 Main menu','<b>Clinics</b> (Section 2), <b>Pharmacy</b> (Section 3) and <b>Doctors</b> (Section 4). The page you are on is shown in blue.'],
 ['4 Account menu','Click it for <b>Account</b> and <b>Logout</b> (1.4).'],
 ['5 Work area','A list on the left and, on the right, either an <b>Add</b> form or the details of the item you clicked.']])
p('Every main page works the same way: the list on the left has a search box, the right side starts with an empty <b>Add</b> form, and clicking an item in the list shows its details in place of the form.')
h2('1.4','Account menu and signing out','s1-4')
fig('f-usermenu','The account menu at the top right.',['Account menu','Account','Logout'], size=60, sec='1')
bullets(['Click <b>Account</b> to change your profile, email or password (Section 5).','Click <b>Logout</b> to sign out. Always sign out when you leave a shared computer.'])
end()

section(2,'Clinics',
 'The Clinics page holds the clinics in MediLink and the staff accounts that work in each one.',
 [('2.1','The clinic list and adding a clinic','s2-1'),('2.2','Clinic details','s2-2'),('2.3','Editing a clinic','s2-3'),('2.4','Assigning a doctor to a clinic','s2-4'),('2.5','Adding Secretary, Laboratory and Imaging accounts','s2-5')])
h2('2.1','The clinic list and adding a clinic','s2-1')
p('Click <b>Clinics</b> in the main menu. The <b>Clinic List</b> on the left shows every clinic (for example <i>CLINIC 1</i> and <i>CLINIC 2</i>). Type in <b>Search clinic</b> to find one. The <b>Add Clinic</b> form is on the right.')
fig('f-addclinic','The Clinics page with the Add Clinic form.',['Search clinic','Location message','Clinic details','Clinic Map Location','Clinic Image','CREATE'], size=68, sec='2')
steps(['Type the <b>Clinic Name</b>, <b>Clinic Contact #</b>, <b>Clinic Days Open</b> (for example <i>MON - SAT</i>), <b>Clinic Time Open</b> (for example <i>10am - 3pm</i>) and <b>Clinic Address</b>.',
       'Under <b>Clinic Map Location</b>, type the place in <b>Search Places…</b> and pick it, or move the map to the clinic. Use <b>+</b> and <b>−</b> to zoom. Until a location is chosen, the red message <b>Location is not yet added</b> stays at the top of the form.',
       'Under <b>Clinic Image</b>, drop a photo of the clinic or click <b>browse</b> to choose one.',
       'Click <b>CREATE</b>.'])
h2('2.2','Clinic details','s2-2',brk=True)
p('Click a clinic in the list. Its details open on the right: the clinic photo, name and address, then <b>Other Info</b> (days and time open, contact number) and the clinic\'s place on the map. Below are the lists of people who work in the clinic.')
fig('f-clinicinfo','Clinic details.',['Edit','Close','Other Info','Location Info','ADD DOCTOR','ADD SECRETARY','ADD LABORATORY','ADD IMAGING'], size=74, sec='2')
table(['List','What it shows'],[
 ['Doctor List','Doctors assigned to the clinic and their specialization (for example <i>Dra. Clarissa Reyes, Gastroenterology</i>). Add with <b>ADD DOCTOR</b> (2.4).'],
 ['Secretary List','Secretary accounts and their addresses. Add with <b>ADD SECRETARY</b> (2.5).'],
 ['Laboratory List','Laboratory accounts. Add with <b>ADD LABORATORY</b> (2.5).'],
 ['Imaging List','Imaging accounts. Add with <b>ADD IMAGING</b> (2.5).']])
p('The map also has a <b>GET DIRECTION</b> button (not tested for this manual). Click the <b>X</b> (2) to close the details and return to the Add Clinic form.')
h2('2.3','Editing a clinic','s2-3',brk=True)
steps(['Open the clinic (2.2) and click the edit icon (1 in Figure 2.2). The <b>Edit Clinic</b> window opens.',
       'Change the name, contact number, days open, time open or address.',
       'To change the map location, click <b>LOCATION</b>.',
       'To change the photo, drop a new one under <b>Clinic Image</b> or click <b>browse</b>.',
       'Click <b>UPDATE</b>.'])
fig('f-clinicedit','The Edit Clinic window.',['LOCATION','Clinic details','Clinic Image','UPDATE'], size=62, sec='2')
h2('2.4','Assigning a doctor to a clinic','s2-4')
steps(['Open the clinic and click <b>ADD DOCTOR</b>. The <b>Add Clinic Doctor</b> window opens.',
       'Choose the doctor in the <b>Doctor</b> list. Doctors must first be added on the Doctors page (4.2).',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-clinicdoctor','The Add Clinic Doctor window.',['Doctor','SAVE'], size=40, sec='2')
h2('2.5','Adding Secretary, Laboratory and Imaging accounts','s2-5',brk=True)
p('Each clinic has its own staff accounts. These are the people who sign in with the Secretary, Laboratory and Imaging roles. The example below is <b>ADD SECRETARY</b>; <b>ADD LABORATORY</b> and <b>ADD IMAGING</b> open the same form with the role in its labels (for example <i>Laboratory Firstname</i>, <i>Imaging Username</i>).')
fig('f-clinicstaff','The Add Clinic Secretary window.',['Personal details','Photo','Contact Number','Username and Password','SAVE'], size=62, sec='2')
steps(['Open the clinic and click <b>ADD SECRETARY</b>.',
       'Under <b>Secretary Information</b>, type the <b>Firstname</b>, <b>Lastname</b> and <b>Address</b>, choose the <b>Gender</b> and set the <b>Birth Date</b>.',
       'Drop a photo in <b>Select secretary\'s image</b> or click <b>browse</b>.',
       'Type the <b>Contact Number</b>.',
       'Type a <b>Username</b> and <b>Password</b> for the new account. Give these to the staff member so they can sign in.',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
call('NOTE','The Birth Date field opens with today\'s date and the red text <b>Invalid Date Format</b> is shown under it before anything is typed. Pick the correct birth date before saving.')
end()

section(3,'Pharmacy',
 'The Pharmacy page holds the partner pharmacies and their staff accounts.',
 [('3.1','The pharmacy list and adding a pharmacy','s3-1'),('3.2','Pharmacy details','s3-2'),('3.3','Adding Admin, Assistant and Pharmacist accounts','s3-3')])
h2('3.1','The pharmacy list and adding a pharmacy','s3-1')
p('Click <b>Pharmacy</b> in the main menu. The <b>Pharmacy List</b> on the left shows every pharmacy (for example <i>TGP</i> and <i>Mabini Pharmacy</i>). Type in <b>Search pharmacy</b> to find one.')
fig('f-addpharmacy','The Pharmacy page with the Add Pharmacy form.',['Search pharmacy','Pharmacy details','Pharmacy Map Location','Pharmacy Image','CREATE'], size=80, sec='3')
steps(['Type the <b>Pharmacy Name</b>, <b>Pharmacy Contact #</b>, <b>Pharmacy Days Open</b>, <b>Pharmacy Time Open</b> and <b>Pharmacy Address</b>.',
       'Under <b>Pharmacy Map Location</b>, search for the place or move the map to it.',
       'Under <b>Pharmacy Image</b>, drop a photo or click <b>browse</b>.',
       'Click <b>CREATE</b>.'])
h2('3.2','Pharmacy details','s3-2',brk=True)
p('Click a pharmacy in the list. The right side shows its name and address, <b>Other Info</b> (for example <i>Days Open: EVERY DAY</i>, <i>Time Open: 24/7</i> and the contact number), its map location, and three staff lists: <b>Admin List</b>, <b>Assistant List</b> and <b>Pharmacist List</b>.')
fig('f-pharmacyinfo','Pharmacy details.',['Edit','Other Info','ADD ADMIN','ADD ASSISTANT','ADD PHARMACIST'], size=85, sec='3')
p('Click the edit icon (1) to open <b>Edit Pharmacy</b>. It works like Edit Clinic (2.3): change the details, use <b>LOCATION</b> for the map and <b>PHARMACY IMAGE</b> for the photo, then click <b>UPDATE</b>.')
h2('3.3','Adding Admin, Assistant and Pharmacist accounts','s3-3',brk=True)
p('Pharmacy staff accounts are added from the pharmacy\'s details. The example below is <b>ADD ADMIN</b>; <b>ADD ASSISTANT</b> and <b>ADD PHARMACIST</b> open the same form with the role in its labels (for example <i>Assistant Firstname</i>, <i>Pharmacist Username</i>).')
fig('f-pharmacystaff','The Add Pharmacy Admin window.',['Personal details','Photo','Contact Number','Username and Password','SAVE'], size=62, sec='3')
steps(['Open the pharmacy and click <b>ADD ADMIN</b>, <b>ADD ASSISTANT</b> or <b>ADD PHARMACIST</b>.',
       'Type the <b>Firstname</b>, <b>Lastname</b> and <b>Address</b>, choose the <b>Gender</b> and set the <b>Birth Date</b>.',
       'Drop a photo or click <b>browse</b>.',
       'Type the <b>Contact Number</b>, then a <b>Username</b> and <b>Password</b> for the account.',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
end()

section(4,'Doctors',
 'The Doctors page holds every doctor in MediLink, their professional numbers and e-signature, and the list of specializations.',
 [('4.1','The doctor list','s4-1'),('4.2','Adding a doctor','s4-2'),('4.3','Doctor details','s4-3'),('4.4','Editing a doctor','s4-4'),('4.5','Specializations','s4-5')])
h2('4.1','The doctor list','s4-1')
p('Click <b>Doctors</b> in the main menu. The <b>Doctor List</b> on the left shows every doctor (for example <i>Dra. Clarissa Reyes</i> and <i>Joseph Manahan</i>). Type in <b>Search doctor</b> to find one. The <b>Add Doctor</b> form is on the right, and the <b>SPECIALIZATION</b> button at the top right opens the specialization list (4.5).')
h2('4.2','Adding a doctor','s4-2')
fig('f-adddoctor','The Doctors page with the Add Doctor form.',['Search doctor','SPECIALIZATION','Doctor Information','Doctor\'s image and signature','Username and Password','CREATE'], size=92, sec='4')
steps(['Under <b>Doctor Information</b>, type the <b>Firstname</b>, <b>Lastname</b> and <b>Address</b>, choose the <b>Gender</b>, set the <b>Birth Date</b> and type the <b>Contact Number</b>.',
       'Choose the <b>Specialization</b> (required). If it is not in the list, add it first (4.5).',
       'Type the <b>License Number</b>, <b>PDEA Number</b>, <b>S2 Number</b> and <b>PTR Number</b>. These appear on the doctor\'s prescriptions.',
       'Drop the doctor\'s photo in <b>Select doctor\'s image</b>, and a picture of the doctor\'s signature in <b>Select doctor\'s signature</b>.',
       'Type the doctor\'s <b>Username</b> and <b>Password</b>.',
       'Click <b>CREATE</b>. To make the doctor available in a clinic, assign them there (2.4).'])
h2('4.3','Doctor details','s4-3',brk=True)
p('Click a doctor in the list. The right side shows the doctor\'s photo, name, address and contact number, then <b>Other Info</b>: gender, birth date and the License, PDEA, PTR and S2 numbers. The doctor\'s <b>E-Signature</b> is shown at the bottom.')
fig('f-doctorinfo','Doctor details.',['Edit','Close','Other Info'], sec='4')
h2('4.4','Editing a doctor','s4-4',brk=True)
steps(['Open the doctor (4.3) and click the edit icon. The <b>Edit Doctor</b> window opens with the doctor\'s current details.',
       'Change any field, the photo or the e-signature.',
       'Scroll to the bottom of the window and click the save button.'])
fig('f-doctoredit','The Edit Doctor window.',['Doctor details'], size=42, sec='4')
h2('4.5','Specializations','s4-5',brk=True)
p('Click <b>SPECIALIZATION</b> on the Doctors page. The list shows every specialization, for example <i>Dermatology</i>, <i>Dentistry</i>, <i>Gastroenterology</i>, <i>Internal Medicine</i> and <i>Urology</i>. Click <b>BACK</b> to return to the Add Doctor form.')
fig('f-spec','The specialization list.',['BACK','ADD SPECIALIZATION','Search specialization','Edit'], size=62, sec='4')
p('<b>To add a specialization:</b>')
steps(['Click <b>ADD SPECIALIZATION</b>.','Type the name in <b>Specialization</b>.','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-addspec','The Add Specialization window.',['Specialization','SAVE'], size=26, sec='4')
p('<b>To rename a specialization:</b>')
steps(['Click the edit icon on its row. The <b>Edit</b> window opens with the current name.','Change the name.','Click <b>UPDATE</b>.'])
fig('f-editspec','The Edit Specialization window.',['Specialization','UPDATE'], size=36, sec='4')
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
 ['Add a clinic','Clinics › Add Clinic › CREATE','2.1'],
 ['Change a clinic\'s details','Clinics › clinic › edit icon › UPDATE','2.3'],
 ['Assign a doctor to a clinic','Clinics › clinic › ADD DOCTOR','2.4'],
 ['Create a secretary, laboratory or imaging account','Clinics › clinic › ADD SECRETARY / LABORATORY / IMAGING','2.5'],
 ['Add a pharmacy','Pharmacy › Add Pharmacy › CREATE','3.1'],
 ['Create pharmacy staff accounts','Pharmacy › pharmacy › ADD ADMIN / ASSISTANT / PHARMACIST','3.3'],
 ['Add a doctor','Doctors › Add Doctor › CREATE','4.2'],
 ['Change a doctor\'s license numbers','Doctors › doctor › edit icon','4.4'],
 ['Add a specialization','Doctors › SPECIALIZATION › ADD SPECIALIZATION','4.5'],
 ['Change my password','Account › SECURITY','5.3']], cls='w3')
end()
