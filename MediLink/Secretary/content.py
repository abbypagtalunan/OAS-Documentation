# ================= CONTENT =================
section(1, 'Getting Started',
 'This section explains what the Secretary does in MediLink, how to sign in, and how the Secretary screen is laid out.',
 [('1.1','About the Secretary role','s1-1'),('1.2','Signing in','s1-2'),('1.3','The Secretary screen','s1-3'),('1.4','Account menu and signing out','s1-4')])
h2('1.1','About the Secretary role','s1-1')
p('MediLink, the Integrated Healthcare System of the Municipality of Oas, connects patients with the Municipal Health Office. The <b>Secretary</b> handles the front desk: patients, appointments, bills and follow-ups. As a Secretary you can:')
bullets(['view upcoming appointments, and reschedule or cancel them;',
         'add new patients and update their profiles;',
         'book an appointment for a patient with a doctor;',
         'upload laboratory and imaging attachments to a patient\'s record;',
         'add bills, correct bill amounts and record payments;',
         'view, filter and print receipts; and',
         'keep track of patients who need a follow-up visit.'])
call('IMPORTANT','<b>Sample data only.</b> All patients, doctors, appointments, bills, receipts and contact details shown in this manual are sample data used for training. They are not real records.')
h2('1.2','Signing in','s1-2')
steps(['Open a web browser and go to <b>medilink.oas.lguapp.com</b>.',
       'On the MediLink home page, click <b>LOGIN</b> at the top right (Figure 1.1).',
       'Sign in with the secretary account given to you by the system administrator.',
       'After signing in, MediLink opens the <b>Appointment</b> page (Section 2).'])
fig('f-home','The MediLink home page.',['LOGIN button'], size=80, sec='1')
h2('1.3','The Secretary screen','s1-3')
fig('f-layout','The Secretary screen.',['Top bar','Your profile (photo, name and email)','Main menu','Account menu','Work area'], sec='1')
table(['Part','What it does'],[
 ['1 Top bar','Shows that you are signed in with the <b>Secretary</b> role.'],
 ['2 Your profile','Your photo, name and email.'],
 ['3 Main menu','<b>Appointment</b> (Section 2), <b>Patient List</b> (Section 3), <b>Billing</b> (Section 4), <b>Reports</b> (Section 5) and <b>Follow Up</b> (Section 6). The page you are on is shown in blue.'],
 ['4 Account menu','Click it for <b>Account</b> and <b>Logout</b> (1.4).'],
 ['5 Work area','The content of the page you opened. Most pages show a list on the left and the details of the selected item on the right.']])
h2('1.4','Account menu and signing out','s1-4')
fig('f-usermenu','The account menu at the top right.',['Account menu','Account','Logout'], size=60, sec='1')
bullets(['Click <b>Account</b> to change your profile, email or password (Section 7).',
         'Click <b>Logout</b> to sign out. Always sign out when you leave a shared computer.'])
end()

section(2,'Appointments',
 'The Appointment page lists patients with booked appointments. From here you can see the details of an appointment, reschedule it or cancel it.',
 [('2.1','The appointment list','s2-1'),('2.2','Viewing an appointment','s2-2'),('2.3','Rescheduling an appointment','s2-3'),('2.4','Cancelling an appointment','s2-4')])
h2('2.1','The appointment list','s2-1')
p('Click <b>Appointment</b> in the main menu. Each row is one appointment, shown by the patient\'s name. A patient with several appointments appears once for each.')
fig('f-appt','The appointment list.',['Search patient','Appointments'], sec='2')
p('To find a patient\'s appointments, type the name in <b>Search patient</b>. The list narrows as you type (Figure 2.2).')
fig('f-apptsearch','Searching the appointment list.',['Search text','Matching appointments'], size=50, sec='2')
call('NOTE','The search matches capital and small letters exactly. <i>David</i> or <i>Cruz</i> finds the patient, but <i>david</i> or <i>cruz</i> does not. Type names with a capital first letter.')
h2('2.2','Viewing an appointment','s2-2')
p('Click a patient in the list. The <b>Appointment Details</b> panel opens on the right.')
fig('f-apptdetails','Appointment details.',['Date and time, reason, service and fee','RESCHEDULE APPOINMENT','CANCEL APPOINTMENT','CLOSE'], sec='2')
table(['Field','What it shows'],[['Appointment Date','The date and time of the appointment.'],['Appointment Reasons','The reason the patient gave when booking.'],['Appointment Service','The service booked, for example <i>check-up</i>.'],['Appointment Fee','The fee for the service, in pesos.']])
h2('2.3','Rescheduling an appointment','s2-3')
steps(['Open the appointment (2.2) and click <b>RESCHEDULE APPOINMENT</b>.',
       'In the <b>Reschedule Appointment</b> window, pick the new date under <b>Date Picker</b>.',
       'Pick the new time under <b>Time Picker</b>.',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to keep the old schedule.'])
fig('f-reschedule','The Reschedule Appointment window.',['Date Picker','Time Picker','SAVE'], size=60, sec='2')
call('NOTE','The message <i>Date should not be before minimal date</i> means the date shown is already past. Choose today or a later date.')
h2('2.4','Cancelling an appointment','s2-4')
steps(['Open the appointment (2.2) and click <b>CANCEL APPOINTMENT</b>.',
       'MediLink asks <i>Are you to remove this appointment?</i> Click <b>YES</b> to cancel the appointment, or <b>NO</b> to keep it.',
       'After <b>YES</b>, a green message confirms the change and the appointment disappears from the list.'])
fig('f-cancelconfirm','Confirming the cancellation.',['CANCEL APPOINTMENT','YES (cancel the appointment)','NO (keep it)'], size=85, sec='2')
fig('f-canceldone','After cancelling: the appointment is no longer listed.',['Appointment list without the cancelled appointment','Confirmation message'], size=46, sec='2')
call('WARNING','Cancel only when the patient asks to cancel. The appointment is removed from the Appointment list right away.')
end()

section(3,'Patient List',
 'The Patient List is where you add patients, update their profiles, book appointments for them and upload their laboratory and imaging files.',
 [('3.1','Finding a patient','s3-1'),('3.2','Adding a new patient','s3-2'),('3.3','Patient details','s3-3'),('3.4','Booking an appointment for a patient','s3-4'),('3.5','Viewing and editing a profile','s3-5'),('3.6','Laboratory and imaging attachments','s3-6')])
h2('3.1','Finding a patient','s3-1')
p('Click <b>Patient List</b> in the main menu. All patients are listed on the left in alphabetical order. Type in <b>Search patient</b> to narrow the list, then click the patient\'s name to open the details (3.3).')
fig('f-patients','The Patient List page with the Add Patient form.',['Search patient','Patients','Add Patient form','SAVE'], sec='3')
h2('3.2','Adding a new patient','s3-2')
p('When no patient is selected, the <b>Add Patient</b> form is shown on the right (Figure 3.1, box 3).')
fig('f-addpatient','A completed Add Patient form.',['Name','Gender, Birth Date and Birth Place','Address','Occupation, Civil Status and Religion','Mobile and Telephone','Email and the account message','Others (health measurements)','SAVE'], size=82, sec='3')
steps(['Type the patient\'s <b>First Name</b>, <b>Last Name</b> and <b>Middle Name</b>.',
       'Choose the <b>Gender</b>, then enter the <b>Birth Date</b> and <b>Birth Place</b>.',
       'Type the address: <b>Street</b>, <b>Barangay</b> and <b>City</b>.',
       'Type the <b>Occupation</b>, choose the <b>Civil Status</b> (Single, Married or Divorced), and type the <b>Religion</b>.',
       'Type the <b>Mobile</b> number, and the <b>Telephone</b> and <b>Email</b> if the patient has them.',
       'Under <b>Others</b>, enter the patient\'s height (cm), weight (kg), pulse, temperature, blood pressure (systolic and diastolic) and choose the <b>Blood Type</b>.',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to clear the form.'])
p('<b>Email and the patient\'s account.</b> The <b>Email</b> field is optional, but filling it in does more than record an address. MediLink shows the message <i>Setting email will create account and the default password will be "hello123"</i> under the field (Figure 3.3).')
fig('f-emailnote','The Email field and its account message.',['Email (becomes the patient\'s username)','Account message with the default password'], size=60, sec='3')
bullets(['When you click <b>SAVE</b> with an email entered, MediLink creates a patient account. The email is the <b>username</b> and the password is the default <b>hello123</b>.',
         'Tell the patient their username and default password, and ask them to sign in and change the password right away (Patient manual, Account Settings).',
         'Check the email carefully before saving. It cannot be changed later, because it is the patient\'s username.',
         'Leave <b>Email</b> blank if the patient does not need to sign in to MediLink.'])
call('IMPORTANT','Every patient account created this way starts with the same password, <b>hello123</b>. Until the patient changes it, anyone who knows the patient\'s email can sign in as that patient.')
h2('3.3','Patient details','s3-3')
p('Click a patient\'s name. The <b>Patient Details</b> panel shows the patient\'s address, contact number, gender, birth date, birth place, religion and civil status. Below it are four tabs.')
fig('f-patientdetails','Patient details.',['Patient information','Tabs: Appointment, Profiles, Laboratory, Imaging','The patient\'s appointments','APPOINTMENT button (book a new appointment)','CLOSE'], sec='3')
table(['Tab','What it shows','See'],[['Appointment','The patient\'s appointments with schedule, reason, service, amount and status.','3.4'],['Profiles','The patient\'s full profile and health measurements.','3.5'],['Laboratory','Laboratory files attached to the patient\'s record.','3.6'],['Imaging','Imaging files attached to the patient\'s record.','3.6']], cls='w3')
h2('3.4','Booking an appointment for a patient','s3-4')
steps(['Open the patient (3.3). On the <b>Appointment</b> tab, click <b>APPOINTMENT</b>.',
       'In <b>Add Appointment</b>, pick the date (<b>Date Picker</b>) and time (<b>Time Picker</b>).',
       'Type the <b>Reason of Appointment</b>.',
       'Choose the <b>Doctor</b>. Each doctor is listed with his or her specialty.',
       'Choose the <b>Service</b>. The services of the chosen doctor appear with their fees, for example <i>check-up - ₱300</i> (Figure 3.6).',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-newappt','The Add Appointment window.',['Date Picker','Time Picker','Reason of Appointment','Doctor','Service','SAVE'], size=58, sec='3')
fig('f-newappt2','After choosing a doctor, the doctor\'s services can be chosen.',['Doctor','Service'], size=58, sec='3')
p('<b>Required fields.</b> <b>Doctor</b> and <b>Service</b> must be chosen before the appointment can be saved. If you click <b>SAVE</b> while either still shows <b>-</b>, the field turns red and <b>Required</b> appears under it, and the appointment is not saved (Figure 3.7). Choose a doctor and a service, then click <b>SAVE</b> again.')
fig('f-apptrequired','Saving without a doctor or service.',['Doctor: Required','Service: Required','SAVE'], size=58, sec='3')
p('The <b>Service</b> list depends on the doctor. Until a doctor is chosen it offers only <i>No service added</i> (Figure 3.8), so choose the <b>Doctor</b> first and then open <b>Service</b> again.')
fig('f-servicenone','The Service list before a doctor is chosen.',['No service added'], size=58, sec='3')
h2('3.5','Viewing and editing a profile','s3-5')
p('The <b>Profiles</b> tab shows the patient\'s personal details and <b>Health Records</b> (height, weight, pulse, temperature, blood pressure and blood type). Fields marked * are required.')
fig('f-profiles','The Profiles tab.',['EDIT','Personal details','Health Records'], size=72, sec='3')
steps(['Click <b>EDIT</b>.','Change the details that need updating.','Click <b>SAVE</b>, or <b>CANCEL</b> to discard your changes.'])
fig('f-profilesedit','Editing a profile.',['CANCEL and SAVE'], size=72, sec='3')
call('NOTE','If the patient has an email, it serves as the patient\'s username and cannot be edited.')
h2('3.6','Laboratory and imaging attachments','s3-6')
p('The <b>Laboratory</b> and <b>Imaging</b> tabs hold result files attached to the patient\'s record, such as scanned laboratory results or X-ray images. Each attachment shows its description, the date and time it was added, and who added it (for example <i>secretary</i>). Click the arrow (›) on a row to show the attached images.')
p('<b>To attach a laboratory result:</b>')
steps(['Open the patient (3.3) and click the <b>LABORATORY</b> tab, then click <b>ADD</b>. The <b>Upload images</b> panel opens on the right.',
       'Type a <b>Description</b>, for example <i>FBS CBC Results</i>.',
       'Drag the file onto the box, or click <b>browse</b> and choose it from your computer. The chosen file is listed with its size; click the bin icon to remove it and choose another.',
       'Click <b>UPLOAD</b>.'])
fig('f-labupload','Uploading a laboratory result.',['Description','File drop area','Chosen file (bin icon removes it)','UPLOAD'], size=62, sec='3')
p('A green message confirms the upload, and the file appears under <b>Laboratory Attachments</b> with the date and <i>Added by: secretary</i>.')
fig('f-labadded','The uploaded result in Laboratory Attachments.',['LABORATORY tab','ADD','New attachment (click › to show the images)'], sec='3')
p('<b>To attach an imaging result:</b> click the <b>IMAGING</b> tab and follow the same steps, for example with the description <i>Xray</i>.')
fig('f-imgupload','Uploading an imaging result.',['Description','File drop area','Chosen file (bin icon removes it)','UPLOAD'], size=62, sec='3')
fig('f-imgadded','The uploaded result in Imaging Attachments.',['IMAGING tab','ADD','New attachment (click › to show the images)'], sec='3')
end()

section(4,'Billing',
 'The Billing page lists patients with unpaid bills. Here you review charges, add bills, correct amounts and record payments.',
 [('4.1','Unpaid bills','s4-1'),('4.2','Correcting a bill amount','s4-2'),('4.3','Adding a bill','s4-3'),('4.4','Recording a payment','s4-4')])
h2('4.1','Unpaid bills','s4-1')
p('Click <b>Billing</b> in the main menu. The <b>Unpaid Bills</b> list shows each patient with a balance. Type in <b>Search patient</b> to find a patient, then click the name.')
fig('f-billing','The Unpaid Bills list.',['Search patient','Patients with unpaid bills'], size=55, sec='4')
p('The <b>Unpaid Bill Details</b> panel lists each charge (order) and amount, and the <b>Total</b>.')
fig('f-bill','Unpaid bill details.',['Charges and total','Edit Amount','NEW BILL','PAYMENT'], size=80, sec='4')
h2('4.2','Correcting a bill amount','s4-2')
steps(['Click the edit icon (Edit Amount) on the charge.','Type the correct <b>Amount</b>.','Type the <b>Reason for edit</b>.','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-editamount','The Edit Bill Amount window.',['Amount','Reason for edit','SAVE'], size=52, sec='4')
call('IMPORTANT','Always give a clear reason when changing an amount, for example a discount or a correction.')
h2('4.3','Adding a bill','s4-3')
steps(['Click <b>NEW BILL</b>.',
       'Under <b>Category</b>, choose <b>service</b> to bill one of the clinic\'s services, or <b>others</b> for any other charge.',
       'For <b>service</b>: choose the <b>Service</b>; its fee is shown in the list, for example <i>Vaccine - ₱700</i>.',
       'For <b>others</b>: type what the charge is for (<i>If others, please specify</i>) and the <b>Amount</b>.',
       'Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-newbill-service','Adding a bill for a service.',['Category: service','Service','SAVE'], size=58, sec='4')
fig('f-newbill-others','Adding another charge.',['Category: others','Description of the charge','Amount','SAVE'], size=58, sec='4')
h2('4.4','Recording a payment','s4-4')
steps(['Click <b>PAYMENT</b>. The <b>Total Cost</b> of the unpaid bills is shown.','Type the <b>Amount</b> the patient paid.','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-payment','The Payment window.',['Total Cost','Amount paid','SAVE'], size=46, sec='4')
call('NOTE','Receipts, with the payment and change, are listed in <b>Reports</b> (Section 5). Saving a payment was not tested while preparing this manual.')
end()

section(5,'Reports',
 'The Reports page lists receipts so you can review collections and reprint a receipt.',
 [('5.1','The receipts list','s5-1'),('5.2','Filtering by date','s5-2'),('5.3','Viewing and printing a receipt','s5-3')])
h2('5.1','The receipts list','s5-1')
p('Click <b>Reports</b> in the main menu. Each row shows the <b>Date</b>, <b>Receipt No.</b>, <b>Patient</b>, <b>Service</b> and <b>Rate</b>. The <b>Total</b> of the listed receipts is shown at the bottom.')
fig('f-reports','The Reports page.',['Search receipt','FILTER','Receipts and total','Details'], sec='5')
h2('5.2','Filtering by date','s5-2')
steps(['Click <b>FILTER</b>.','Set <b>Date & Time From</b> and <b>Date & Time To</b>. Click the calendar icon to pick a date.','Click <b>FILTER</b> in the window. The list shows only receipts in that period.'])
fig('f-filter','The Filter To Display window.',['Date & Time From','Date & Time To','FILTER'], size=60, sec='5')
h2('5.3','Viewing and printing a receipt','s5-3')
steps(['Click the arrow (Details) at the end of a receipt row.','The receipt opens with the clinic\'s name, address, contact number and hours, and the patient\'s name, address and date.','Click <b>PRINT</b> to print it, or <b>CLOSE</b> to return to the list.'])
fig('f-receipt','A receipt.',['Clinic and patient details','Charges, total, payment and change','CLOSE','PRINT'], sec='5')
end()

section(6,'Follow Up',
 'The Follow Up page lists patients whom a doctor asked to come back, so you can contact them.',
 [('6.1','Ongoing follow-ups','s6-1'),('6.2','Done follow-ups','s6-2')])
h2('6.1','Ongoing follow-ups','s6-1')
p('Click <b>Follow Up</b> in the main menu. The list shows the <b>Date</b> of the follow-up, the doctor\'s <b>Description</b>, the <b>Patient</b> and the patient\'s <b>Contact Number</b>.')
fig('f-followup','Ongoing follow-ups.',['Search patient','Ongoing / Done','Follow-ups','Set As Done'], sec='6')
steps(['Call or message the patient using the contact number.','When the follow-up is settled, click the thumbs-up icon (<b>Set As Done</b>) on the row.'])
call('NOTE','<b>Set As Done</b> was not clicked while preparing this manual. Follow-ups already marked done are listed under <b>Done</b> (6.2).')
h2('6.2','Done follow-ups','s6-2')
p('Choose <b>Done</b> in the list at the top right to see follow-ups already marked done. Choose <b>Ongoing</b> to go back.')
fig('f-followupdone','Done follow-ups.',['Ongoing / Done','Done follow-ups'], sec='6')
end()

section(7,'Account Settings',
 'Use Account settings to keep your profile, email and password up to date.',
 [('7.1','Profile','s7-1'),('7.2','Changing your email','s7-2'),('7.3','Changing your password','s7-3')])
h2('7.1','Profile','s7-1')
p('Open <b>Account</b> from the account menu (1.4). The <b>Settings</b> page has three tabs: <b>General</b>, <b>Email</b> and <b>Security</b>.')
fig('f-account','Account settings, General tab.',['GENERAL, EMAIL and SECURITY tabs','Photo and UPLOAD PROFILE','Profile details','SAVE CHANGES'], sec='7')
steps(['To change your photo, click <b>UPLOAD PROFILE</b> and choose an image.','Edit your <b>First Name</b>, <b>Last Name</b>, <b>Phone Number</b>, <b>State</b> and <b>Country</b>. Fields marked * are required.','Click <b>SAVE CHANGES</b>.'])
h2('7.2','Changing your email','s7-2')
fig('f-email','The Email tab.',['Current Email','New Email','CHANGE EMAIL'], sec='7')
steps(['Click the <b>EMAIL</b> tab.','Type your <b>New Email</b>.','Click <b>CHANGE EMAIL</b>.'])
h2('7.3','Changing your password','s7-3')
fig('f-security','The Security tab.',['Password','Password Confirmation','CHANGE PASSWORD'], sec='7')
steps(['Click the <b>SECURITY</b> tab.','Type the new <b>Password</b>, and type it again in <b>Password Confirmation</b>.','Click <b>CHANGE PASSWORD</b>.'])
end()

appendix('A','Quick Reference','Where to go for common tasks.','sa')
table(['I want to…','Go to','See'],[
 ['See a patient\'s appointment','Appointment › patient name','2.2'],
 ['Move an appointment','Appointment › patient › RESCHEDULE APPOINMENT','2.3'],
 ['Register a new patient','Patient List › Add Patient › SAVE','3.2'],
 ['Book an appointment','Patient List › patient › Appointment tab › APPOINTMENT','3.4'],
 ['Update a patient\'s details','Patient List › patient › Profiles › EDIT','3.5'],
 ['Upload a lab or imaging file','Patient List › patient › Laboratory or Imaging › ADD','3.6'],
 ['Add a charge','Billing › patient › NEW BILL','4.3'],
 ['Record a payment','Billing › patient › PAYMENT','4.4'],
 ['Reprint a receipt','Reports › Details › PRINT','5.3'],
 ['See who needs a follow-up','Follow Up › Ongoing','6.1'],
 ['Change my password','Account › SECURITY','7.3']], cls='w3')
end()
