## Where we left off (Permit Evaluator, Section 4)
Section 4 covers: sign in, the dashboard, New Request (details form, CTC number, Approve), the Approved Request For Assessment list, and the For Assessment list with Assessment Status PENDING.
Still to document, in this order (send screenshots):
- [ ] Add/Edit Fees on the assessment (the screen and its messages).
- [ ] The For Approval remarks window, its message, and the Assessment Status after sending.
- [ ] Then the BPLO approval, Assessed For Payment (entering the OR number and date), Permit Issuance (For MP Preparation, Received Form), and an Administrator section.

# Screenshots needed

Use a dummy business and dummy owner. Capture the full browser window. Tick items off as they are sent.

## Section 3.3: Requesting a Permit, New Business (current focus). Renewal, Closure and Transfer are Sections 6 to 8.
From the code, the applicant flow has three marked steps: Step One (Display Assessment List), Step Two (Create Assessment Request), Step Three (Sent Attachment Per Office).

### 5.1 Open the assessment list
- [x] 1. Business Holdings page, hovering over or clicking the numbered 1 icon on the business row.
- [x] 2. The Assessments page for the new business, empty. It shows "No assessment found." and the Request button with the "Step Two - Create Assessment Request" label.

### 5.2 Fill out the request form (click Request)
- [x] 3. Top of the Request Form (Business Name through Transaction Type).
- [x] 4. Transaction Type dropdown open (New, Renewal, Transfer, Closure).
- [x] 5. Form with Transaction Type = New (shows Capitalization).
- [x] 6. Form with Transaction Type = Renewal (shows Gross Income).
- [x] 7a. Payment Mode dropdown open (done).
- [x] 7b. The quarter selector (appears for Semi-Annual or Quarterly).
- [x] 8. The requirements upload area (list of required files, upload buttons).
- [x] 9. Bottom of the form with its buttons.
- [x] 10. The form with a required field left empty (red messages).
- [x] 11. The success message after sending ("Assessment Sent").

### After the request is sent (New Business; new Section 3.3.4 onward)
- [ ] 12. The Assessments page with the new request in the list (all columns, and the row icons).
- [ ] 13. The "Step Three - Sent Attachment Per Office" icon label.
- [ ] 14. The Sent Attachment Per Office page (upload per office).
- [ ] 15. The status popover (click the status label): the office list with colored dots, and one office expanded to show remarks.

### 5.4 Other row icons
- [ ] 16. Send Inquiry (opens the inquiry page).
- [ ] 17. Offices Uploaded Files.
- [ ] 18. Assessment Details.
- [ ] 19. View/Print Assessment (the details page with the payment options).

## Still pending from earlier
- [ ] Business Registration: the video window it opens (and the video title if shown).
- [ ] Business Holdings with a record: the Registration, Registered Owner and Miscellaneous tabs.
- [ ] Edit Business page.
- [ ] Location page (pin icon).
- [ ] Account page (Account in the account menu).
- [ ] Notifications (bell) and Chat panels.
- [ ] Sign up validation messages: submit an empty Sign up form.

## New Business, Section 3.3.5 (Assessment Requirements page)
- [x] An office opened (for example Assessor) showing its Requirements List (Id, Requirement, Required, Status, Forms, Action).
- [x] The Forms column with a downloadable form, if any.
- [x] The "Upload Requirements Attachment" window (empty, then with files chosen).
- [x] The "Email Sent" message after uploading.
- [x] A requirement after it was sent: the Status and the "View uploaded requirements" icon, and the window it opens.
- [-] The "Attachment On Request" window (skipped by the project owner).
- [x] The Assessments list with the new request (status PENDING, row icons).
- [ ] The status popover (click the PENDING label) with the per-office dots.

## Section 3.7: Sending an Inquiry (next; opened from the paper plane icon)
Applicant side. From the code: the Inquiries page has "Make Inquiry", a "List Of Inquiries" panel with Search, and a chat panel for the selected inquiry. The Make Inquiry window has Select Business, Select Office, Enter message inquiry.
- [x] 1. The Assessment Information list with the Send Inquiry (paper plane) icon highlighted or its tooltip showing.
- [x] 2. The page that opens after clicking it (Inquiries page; it may open the Make Inquiry window by itself).
- [x] 3. The Inquiries page with no inquiries yet ("No record found.").
- [x] 4. The Make Inquiry window, empty.
- [x] 5. The Select Office list open (offices and barangay).
- [x] 6. The Make Inquiry window filled in.
- [x] 7. The message after sending ("Inquiry successfully sent.").
- [ ] 8. The error when a field is empty ("Receiver is a required field." / "Inquery is a required field.").
- [x] 9. The Inquiries page with the new inquiry in the list.
- [x] 10. The inquiry opened: the chat panel with the message box and send icon.
- [ ] 11. Sending another message in the chat, and the error "message is a required field." if you click send with an empty box.
- [ ] 12. An office reply, if one can be arranged (log in as an office), and how the applicant sees it.
- [ ] 13. The chat icon in the top bar (what it shows) and the bell notification for a reply.

## Staff side, step 1: Offices review the request (proposed Section 4)
From the code: an office (for example Assessor) sees "Request For Clearances" with three lists (Pending, Disapproved, Approved), each with Search, Year and Request Type filters. Opening a request shows Business Information, "Assessment - <OFFICE>", Assessment Details, Assessment Requirements, Requirements Per Assessment and an Actions card (DATE, CURRENT STATUS, REMARKS and the buttons Pending, Disapproved, Approved, Location, Files). IMPORTANT: the action buttons stay hidden ("Action buttons are hidden due to Assessment - ASSESSOR amount not set.") until the Permit Evaluator has set an amount for that office in the assessment. So the test request must be assessed first before an office can approve.

Part A: what the office sees before it can act
- [ ] 1. The office login and the page it lands on (Request For Clearances).
- [ ] 2. The sidebar of the office account.
- [ ] 3. The Pending list with the test request, and the filters (Search, Year, Request Type).
- [ ] 4. The request opened: Business Information and the accordions (Assessment - OFFICE, Assessment Details, Assessment Requirements, Requirements Per Assessment).
- [ ] 5. The Assessment Requirements accordion open: the files the applicant sent to this office, and viewing a file.
- [ ] 6. The Actions card with the message "Action buttons are hidden due to Assessment - ... amount not set."
- [ ] 7. The Files and Location pages.

Part B: after the Permit Evaluator has set the office amount
- [ ] 8. The Actions card with the buttons Pending, Disapproved, Approved, Location, Files.
- [ ] 9. The Approved dialog (Remarks is required) and the message after saving.
- [ ] 10. The Disapproved dialog and the message after saving.
- [ ] 11. The request in the Approved list and in the Disapproved list.
- [ ] 12. The Holdings and Requirements pages of the office.
- [ ] 13. Answering an applicant inquiry (the office Inquiry page) and the reply.
- [ ] 14. Back on the applicant side: the status popover with a green dot (approved), an orange dot (not approved) and an office remark opened.
