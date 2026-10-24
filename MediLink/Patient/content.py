# ================= CONTENT =================
section(1, 'Getting Started',
 'This section explains what a patient can do in MediLink, how to sign in, and how the Patient screen is laid out.',
 [('1.1','About MediLink for patients','s1-1'),('1.2','Signing in','s1-2'),('1.3','The Patient screen','s1-3'),('1.4','Account menu and signing out','s1-4')])
h2('1.1','About MediLink for patients','s1-1')
p('MediLink, the Integrated Healthcare System of the Municipality of Oas, keeps your health record in one place and connects you with the Municipal Health Office. As a <b>Patient</b> you can:')
bullets(['keep your personal profile and vital signs up to date, and check your BMI;',
         'see the allergies, diagnoses, medication and diet advice your doctor recorded;',
         'add your own diet plan and family health history;',
         'view and upload your laboratory and imaging files;',
         'follow your readings over time in the Health Graph;',
         'find clinics, their schedules and their doctors; and',
         'see which doctors have permission to view your record.'])
call('IMPORTANT','<b>Sample data only.</b> All patients, doctors, clinics, results and contact details shown in this manual are sample data used for training. They are not real records.')
call('NOTE','Screens in this manual were captured from the live system on 24 October 2026 with a patient account. The patient screens did not show an option to book an appointment; appointments are booked at the clinic by the Secretary.')
h2('1.2','Signing in','s1-2')
p('Your account is created when the clinic registers you with your email address. Your email is your username.')
steps(['Open a web browser and go to <b>medilink.oas.lguapp.com</b>.',
       'On the MediLink home page, click <b>LOGIN</b> at the top right (Figure 1.1).',
       'Sign in with your email and password.',
       'MediLink opens your <b>Profile</b> (Section 2).'])
fig('f-home','The MediLink home page.',['LOGIN button'], size=80, sec='1')
call('IMPORTANT','If the clinic gave you a default password, change it the first time you sign in (Section 7.3).')
h2('1.3','The Patient screen','s1-3')
fig('f-layout','The Patient screen.',['Top bar','Your photo, name and email','Main menu','Account menu','Work area'], sec='1')
table(['Menu','What you will find','See'],[
 ['Profile','Your personal details.','2.1'],
 ['Vitals','Your vital signs and the BMI calculator.','2.2'],
 ['Allergies, Diagnosis, Medication','Records from your doctor.','3.1 – 3.3'],
 ['Diet','Diet advice from your doctor and your own diet plan.','3.4'],
 ['Family History','Health history of your parents and children.','3.5'],
 ['Laboratory, Imaging','Your test result files.','Section 4'],
 ['Health Graph','Charts of your readings over time.','Section 5'],
 ['Clinic List','Clinics, their schedule, location and doctors.','6.1'],
 ['Permissions','Doctors with access to your record.','6.2']], cls='w3')
h2('1.4','Account menu and signing out','s1-4')
fig('f-usermenu','The account menu at the top right.',['Account menu','Account','Logout'], size=60, sec='1')
bullets(['Click <b>Account</b> to change your profile photo, email or password (Section 7).',
         'Click <b>Logout</b> to sign out. Always sign out on a shared computer or phone.'])
end()

section(2,'Profile and Vitals',
 'Keep your personal details and vital signs up to date so your doctor sees correct information.',
 [('2.1','Your profile','s2-1'),('2.2','Vital signs','s2-2'),('2.3','BMI calculator','s2-3')])
h2('2.1','Your profile','s2-1')
p('Click <b>Profile</b> in the main menu. Your profile shows your name, gender, birthday, birthplace, address, civil status, occupation, religion, mobile and telephone numbers, and under <b>Other Information</b> your height, weight and blood type.')
fig('f-profile','Your profile.',['UPDATE','Personal details','Other Information'], sec='2')
steps(['Click <b>UPDATE</b>. The fields can now be changed.','Correct the details that need updating. Fields marked * are required.','Click <b>SAVE</b>, or <b>NO</b> to discard your changes.'])
fig('f-profileupdate','Updating your profile.',['Editable details','NO and SAVE'], size=80, sec='2')
h2('2.2','Vital signs','s2-2')
p('Click <b>Vitals</b>. The page shows your latest temperature (℃), blood pressure (systolic and diastolic, mmHg), heart pulse, weight (kg), height (cm), glucose, uric acid, respiratory rate, cholesterol and hepatitis status.')
steps(['Click <b>UPDATE</b>.','Type the readings you measured. For <b>Hepatitis</b>, choose Positive or Negative.','Click <b>SAVE</b>, or <b>CANCEL</b> to discard your changes.'])
fig('f-vitalsupdate','Updating your vital signs.',['Readings','CANCEL and SAVE'], sec='2')
h2('2.3','BMI calculator','s2-3')
p('The <b>BMI Calculator</b> on the Vitals page uses your weight and height to work out your Body Mass Index.')
steps(['Check or change your <b>Weight (kg)</b> and <b>Height (cm)</b>.','Click <b>CALCULATE</b>. Your BMI appears under <b>Result</b>, for example <i>22.04</i> for 60 kg and 165 cm.','Compare the result with the <b>BMI Assessment</b> table: below 18.5 underweight, 18.5 – 25 healthy, 25 – 30 overweight, 30 – 40 obese, 40+ morbidly obese.'])
fig('f-bmi','The Vitals page with the BMI calculator.',['UPDATE','Vital signs','BMI result','Weight and height','CALCULATE','BMI Assessment'], sec='2')
end()

section(3,'Records from Your Doctor',
 'These pages show what your doctor recorded, and let you add your own diet plan and family history.',
 [('3.1','Allergies','s3-1'),('3.2','Diagnosis','s3-2'),('3.3','Medication','s3-3'),('3.4','Diet','s3-4'),('3.5','Family History','s3-5')])
h2('3.1','Allergies','s3-1')
p('Click <b>Allergies</b> to see your known allergies, for example <i>Penicillin</i>. Only your doctor can add allergies. Tell your doctor if an allergy is missing.')
fig('f-allergies','Allergies.',['Your allergies'], sec='3')
h2('3.2','Diagnosis','s3-2')
p('Click <b>Diagnosis</b> to see your doctor\'s diagnoses with their dates. Click the arrow on a row to show or hide the full diagnosis. Only your doctor can add a diagnosis.')
fig('f-diagnosis','Diagnosis, with one row opened.',['Show or hide the details'], sec='3')
h2('3.3','Medication','s3-3')
p('Click <b>Medication</b> to see the medicines your doctor listed for you. Use the arrows at the bottom to page through a long list.')
fig('f-medication','Medication.',['Medications from your doctor'], sec='3')
h2('3.4','Diet','s3-4')
p('Click <b>Diet</b>. <b>Suggested Diet</b> on the left shows the diet advice from your doctor. <b>Personal Diet</b> on the right is your own plan.')
fig('f-diet','Diet.',['Suggested Diet (from your doctor)','Personal Diet (your own)','ADD'], sec='3')
steps(['Click <b>ADD</b> under Personal Diet.','Choose the <b>Meals</b>: Breakfast, Lunch or Dinner.','Type what you eat under <b>Description</b> (required).','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-dietadd','The Add New Diet window.',['Meals','Description','SAVE'], size=58, sec='3')
h2('3.5','Family History','s3-5')
p('Click <b>Family History</b> to record the health of your family. This helps your doctor spot conditions that run in families.')
fig('f-family','Family History.',['ADD','Family members'], sec='3')
steps(['Click <b>ADD</b>.','Choose the <b>Category</b>: Father, Mother or Children.','Type the family member\'s <b>Full name</b>, <b>Address</b>, <b>Birthday</b> and <b>Occupation</b>.','Describe his or her <b>Health Condition</b>, and choose the <b>Current Status</b>: Alive or Deceased.','Click <b>SAVE</b>, or <b>CLOSE</b> to cancel.'])
fig('f-familyadd','The Add New Family History window.',['Category','Full name','Address','Birthday','Occupation','Health Condition','Current Status','SAVE'], size=72, sec='3')
end()

section(4,'Laboratory and Imaging',
 'The Laboratory and Imaging pages hold your test result files. You, the clinic and the laboratory or imaging staff can add files.',
 [('4.1','Viewing your files','s4-1'),('4.2','Uploading a file','s4-2')])
h2('4.1','Viewing your files','s4-1')
p('Click <b>Laboratory</b> or <b>Imaging</b>. Each row shows the description, the date and who added it (for example <i>patient</i>, <i>secretary</i> or <i>imaging</i>). Click the arrow on a row to show or hide its images.')
fig('f-lab','Laboratory attachments.',['ADD','Attachments','Show or hide the images'], sec='4')
fig('f-imaging','Imaging attachments.',[], sec='4')
h2('4.2','Uploading a file','s4-2')
steps(['Click <b>ADD</b>. The <b>Upload images</b> panel opens.','Type a <b>Description</b>, for example the test name and date.','Drag your file onto the box, or click <b>browse</b> and choose it.','Click <b>UPLOAD</b>.'])
fig('f-labadd','The Upload images panel.',['Description','File drop area','UPLOAD'], size=58, sec='4')
call('NOTE','When this manual was prepared, opened rows showed broken image icons, and the panel says <i>Select imaging raw result</i> on the Laboratory page too.')
end()

section(5,'Health Graph',
 'The Health Graph turns your readings into charts so you and your doctor can see how they change over time.',
 [('5.1','Choosing a reading','s5-1'),('5.2','Reading a chart','s5-2')])
h2('5.1','Choosing a reading','s5-1')
p('Click <b>Health Graph</b>. Each card explains one reading: Pain, Respiratory, Uric Acid, HDL, Potassium, Temperature, Weight, Calcium, LDL, Protein, Blood Pressure, Glucose, Chloride, Lithium, Sodium, Pulse, Cholesterol, Creatinine and Magnesium. Click <b>DETAILS</b> on a card to open its chart.')
fig('f-healthgraph','The Health Graph.',['A reading card','DETAILS','Blood Pressure card'], size=82, sec='5')
h2('5.2','Reading a chart','s5-2')
p('The chart plots your recorded values over time. <i>No record</i> under the chart means no values have been saved for that reading yet. Use your browser\'s Back button to return to the cards.')
fig('f-graphdetails','The Blood Pressure chart.',['Chart'], sec='5')
end()

section(6,'Clinics and Permissions',
 'Find a clinic and its doctors, and see which doctors can view your record.',
 [('6.1','Clinic List','s6-1'),('6.2','Permissions','s6-2')])
h2('6.1','Clinic List','s6-1')
p('Click <b>Clinic List</b>. Type in <b>Search clinic</b> to find a clinic, then click its name.')
fig('f-clinics','The Clinic List.',['Search clinic','Clinics'], size=55, sec='6')
fig('f-clinicinfo','Clinic information.',['Search clinic','Clinic name and address','Days and time open, contact number','Location map and GET DIRECTION','Doctors at the clinic','Close'], sec='6')
bullets(['<b>Other Info</b> shows the days and hours the clinic is open and its contact number.',
         '<b>Location Info</b> shows the clinic on a map. Use + and − to zoom. <b>GET DIRECTION</b> is for directions to the clinic (not tested for this manual).',
         '<b>Doctor List</b> shows the doctors at the clinic and their specialty.',
         'Click <b>X</b> to close the clinic information.'])
h2('6.2','Permissions','s6-2')
p('Click <b>Permissions</b>. The table lists doctors with the <b>Date</b> and <b>Status</b> of their permission to view your record. Type in <b>Search doctor</b> to find a doctor.')
fig('f-permissions','Permissions.',['Search doctor','Doctors, dates and status'], sec='6')
call('NOTE','No permissions were listed for the sample patient, so the actions on this page could not be shown.')
end()

section(7,'Account Settings',
 'Use Account settings to keep your profile photo, email and password up to date.',
 [('7.1','Profile','s7-1'),('7.2','Changing your email','s7-2'),('7.3','Changing your password','s7-3')])
h2('7.1','Profile','s7-1')
p('Open <b>Account</b> from the account menu (1.4). The <b>Settings</b> page has three tabs: <b>General</b>, <b>Email</b> and <b>Security</b>.')
fig('f-account','Account settings, General tab.',['GENERAL, EMAIL and SECURITY tabs','Photo and UPLOAD PROFILE','Profile details','SAVE CHANGES'], sec='7')
steps(['To change your photo, click <b>UPLOAD PROFILE</b> and choose an image.','Edit your <b>First Name</b>, <b>Last Name</b>, <b>Phone Number</b>, <b>State</b> and <b>Country</b>.','Click <b>SAVE CHANGES</b>.'])
h2('7.2','Changing your email','s7-2')
fig('f-email','The Email tab.',['Current Email','New Email','CHANGE EMAIL'], sec='7')
steps(['Click the <b>EMAIL</b> tab.','Type your <b>New Email</b>.','Click <b>CHANGE EMAIL</b>.'])
h2('7.3','Changing your password','s7-3')
fig('f-security','The Security tab.',['Password','Password Confirmation','CHANGE PASSWORD'], sec='7')
steps(['Click the <b>SECURITY</b> tab.','Type the new <b>Password</b>, and type it again in <b>Password Confirmation</b>.','Click <b>CHANGE PASSWORD</b>.'])
call('IMPORTANT','Use a password that others cannot guess, and never share it.')
end()

appendix('A','Quick Reference','Where to go for common tasks.','sa')
table(['I want to…','Go to','See'],[
 ['Correct my personal details','Profile › UPDATE','2.1'],
 ['Record my blood pressure or weight','Vitals › UPDATE','2.2'],
 ['Check my BMI','Vitals › BMI Calculator › CALCULATE','2.3'],
 ['See my doctor\'s diagnosis','Diagnosis','3.2'],
 ['See my medicines','Medication','3.3'],
 ['Add my own meal plan','Diet › Personal Diet › ADD','3.4'],
 ['Record family health history','Family History › ADD','3.5'],
 ['Upload a lab result','Laboratory › ADD','4.2'],
 ['See my readings over time','Health Graph › DETAILS','Section 5'],
 ['Find a clinic\'s schedule','Clinic List › clinic','6.1'],
 ['Change my password','Account › SECURITY','7.3']], cls='w3')
end()
