# Items to verify on the live site

Statements in the manual taken from the code, not yet seen on screen.

## Section 2: Getting Started
- [ ] "Email address not found." (red) when an unregistered email is entered on the Recovery page.
- [ ] "Password Successfully Reset" (green) after resetting a password.
- [ ] Behavior of an expired or invalid reset link (code redirects to a not-found page).
- [ ] "Code is not sent. Check your internet connection." when the email cannot be sent.
- [ ] Field messages on Sign up: Must be a valid email / First name is required / Last name is required / Gender is required.
- [ ] Gender dropdown offers only Male and Female.
- [ ] Verification email and reset email may land in Spam or Junk.
- [ ] What happens when the 1-hour verification code expires (is there a resend option?).

## Section 3.1 (to confirm when documenting the Business Holdings page)
- [ ] Add New Company registers a new business; Business Registration sends a request to link an existing business.
- [ ] Watch Guide Video: what it opens.
- [ ] Mail and Calendar in the left menu: used or template leftovers?
- [ ] Account page: update profile, email, password, profile picture.
- [ ] Settings are saved per device only.
- [ ] Theme options (code lists Light, One Dark, Unicorn).

## Project-wide
- [ ] Role names mapped to code roles (Applicant, Engineering, Permit Evaluator, Assessor, Permit Issuance, Administrator).
- [ ] All offices must approve: confirm where this is enforced.

## Section 3.1.5 Payment History
- [ ] The list shows payments recorded for the applicant's businesses after the cashier's OR is encoded (onsite payment).
- [ ] "Export Pdf" in the three-dot menu works and its output.
- [ ] Guide Video opens by itself only on the first visit per browser (code stores this in the browser).

## Section 3.2: Adding a New Business
- [ ] Required fields: besides the asterisk fields, the form also requires Business Category, Owner Type, Barangay and Business Line Desc. (from the code).
- [ ] Validation messages table: only "Business name is required" and "Franchise name is required" were seen on screen; the rest come from the code.
- [ ] Text is converted to capitals automatically (code uses an uppercase handler).
- [ ] What to enter in Franchise Name when the business has no franchise (sample used INDEPENDENT).
- [ ] Meaning of Office Type / Type Of Bank / Type Of Club / Bedroom Type / With AC (numeric fields defaulting to 0), and whether an applicant should touch them.
- [ ] After "Add Company": "Company Created" message and redirect to the Business Holdings list (from the code).
- [ ] SEC Registration No. and SEC Date Issued appear only when Owner Type is not Sole Proprietor.
- [ ] "Area of Signboard" appears when Using Signboard = Yes.
- [ ] DTI No. and DTI Date Issued show an asterisk, but their validation is commented out in the code; confirm whether the form actually blocks saving without them.
- [ ] Business row icons: pencil = Edit Business, numbered 1 = Step One - Display Assessment List (shown while no assessment request exists), pin = Location. Icon is disabled with "Please click Edit to provide the required company details and continue." when details are incomplete (from code).

## Sections 3.3 to 3.6: Requesting a Permit (New Business, Renewal, Closure, Transfer)
- [x] Payment Mode options confirmed: New Business and Closure allow only Annual; Renewal and Transfer allow Annual, Semi-Annual and Quarterly. The system spells the options "Annualy" and "Semi-Annualy"; the manual uses the correct spelling. Consider asking the developers to fix the typo.
- [x] Quarter selector seen: Quarterly shows "Select Quarter Type" (Single Quarter or Multiple Quarter); Semi-Annual shows an "Annual" field (1st Annual).
- [ ] Why 2nd to 4th Quarter are greyed out in Single Quarter (earlier quarter not yet requested? already requested?), and the other Annual choices besides "1st Annual".
- [ ] The system spells "Mutiple Quarter" and "Semi-Annualy" on screen; the manual uses the correct spelling.
- [x] Gross Income is asked instead of Capitalization for a Renewal (confirmed).
- [ ] Requirements differ by transaction type: New Business shows Sketch and Photos of location, DTI, Title or Tax Dec; Renewal shows DTI and Title or Tax Dec. Closure shows only DTI; Transfer shows "No requirements needed." (both seen).
- [ ] Camera tab in the Select Attachment Method window (what it does).
- [ ] "You have no request recorded for this year." appears only when no request exists for the year.
- [ ] Which requirements appear (depends on business type) and whether more than one file per requirement is allowed.
- [ ] Error wording "area must be greater than or equal to 1" and "no_of_storey must be greater than or equal to 1" is shown as raw field names; consider asking the developers to reword.
- [ ] What happens after clicking Request ("Assessment Sent" message, redirect) and whether a required requirement with no file blocks sending.

## Section 3.2.5 Viewing the business details (tabs)
- [ ] DTI Date Issued shows a raw timestamp (2026-10-04T13:18:00.000Z) on the Registration tab; consider asking the developers to format it as a date.
- [ ] Owner Type and Gender appear as letters (S, F); confirm the meanings S = Sole Proprietor, F = Female.
- [ ] "Business Type Code" column shows the type name, not a code.

## Sections 3.3.4 and 3.3.5: after the request is sent
- [x] Upload window, Email Sent, SENT status and picture icon seen on screen. "Email not sent." comes from the code only.
- [ ] The upload box says "Drop files here or click browse thorough your machine" ("thorough" looks like a typo for "through").
- [x] Camera tab: takes a photo directly with the device camera (confirmed by the project owner). The screenshot was taken on a computer without camera access, so it shows the error "Unable to open camera. Please allow camera permission and try again." A capture of the working camera on a phone is still needed.
- [ ] "Attachment On Request" shows the files sent with the request ("Assessment Request Attachments" window; "No attachment found." when none).
- [ ] The eye/picture icon "View uploaded requirements" after a file is sent.
- [ ] Which offices appear (Assessor, Engineering, Fire, Peso, Mao, Menro, Mpdo, Rhu, Bplo and the business's barangay) and whether the list changes by business type.
- [ ] Whether all requirements for all offices must be sent before the request moves forward.
- [x] Requirements List seen on screen: columns Id, Requirement, Required (TRUE), Status (UNSENT red, SENT green), Forms ("No form included." or a downloadable file), Action (Attach File; picture icon after sending); empty offices show "No requirements found."
- [ ] Some requirement names in the sample data look like test data (for example "Sample requirements in fire"); confirm the real names before publishing, or keep the figures generic.
- [ ] The tooltip on the picture icon reads "View uplaoded requirements" on screen (typo for "uploaded"); the manual uses the correct spelling.
- [x] Multiple files can be uploaded for one requirement and viewed in the "Uploaded Requirements Attachment" window (confirmed).

## Sections 3.3.6 to 3.3.8
- [ ] "Business" in the path at the top of the Assessment Requirements page returns to the Assessment Information list (per the project owner); confirm where it goes.
- [ ] Meaning of the dot colors in the status list: red = no action yet; green = approved; orange = not approved (from the code: action null / 1 / 0). Confirm the wording shown to applicants.
- [ ] Icon behavior: Send Inquiry opens the inquiry page; Offices Uploaded Files; View/Sent Attachments (paperclip, replaces the numbered 3 icon after the first file is sent); Assessment Details (print) and View/Print Assessment (arrow) are disabled until the request is approved by BPLO (from the code; tooltips not seen on screen).
- [x] The status popover figure originally showed a second test request (Quarterly, 1st Quarter); the second row was edited out of the figure.

## Section 3.3.9: Wait for the approval of the offices
- [ ] The bell icon shows notifications about the request when offices act.
- [ ] "A request waiting on one office cannot be paid or released" (all offices must approve, per the project owner); confirm the exact rule, including whether BPLO approval alone enables the print icons.

## Section 3.7: Sending an Inquiry (from the code)
- [x] Make Inquiry window and its messages seen on screen: "Inquiry successfully sent." and the error "Inquery is a required field." ("Inquery" looks like a typo for "Inquiry"). "Receiver is a required field." comes from the code only.
- [x] Chat error seen on screen: "message is a required field."
- [ ] Inquiries page: "List Of Inquiries" with Search, "No record found.", unread count, chat panel with live messages.
- [ ] Whether the paper plane icon opens the Make Inquiry window directly (the link is /app/inquiry?new=yes).

## Section 4: Permit Evaluator
- [ ] The paperclip icon in the New Request / Approved list shows "View request on attachments and requirements per office" (tooltip from the code).
- [ ] Account name shown for staff: "eBPLS Permit Evaluator". Confirm the official role name for the manual.
- [ ] The example "Approved Request For Assessment" list shows other applicants' businesses; their names are hidden in the figure.
- [ ] Staff accounts use the same Sign in page and are redirected by role (from the code).

## Section 4.5: Review and approve a new request
- [ ] Required fields on the details form (from the code): Business Category, Business Type, Transaction Type, Owner Type, No. Of Employee, CTC Number, Payment Mode. CTC Number confirmed on screen; the rest from the code (only Business Type shows an asterisk).
- [ ] For a renewal, the details form asks for Gross Sales For Year (and Daily Sales) instead of Capitalization (from the code); screenshot needed.
- [x] After Approve the system runs the assessment automatically; messages "Sworn successfully approve.", "Please wait while we run the assessment process..." and "Assessment process completed successfully" (the last one seen on screen). The error "CTC number is required" was seen on screen.
- [ ] Years Arrears: meaning and when it is filled in.

## Sections 4.7 and 4.8: For Assessment and the assessment
- [x] The document icon in the For Assessment list opens the Files page: files uploaded by the offices (confirmed by the project owner).
- [ ] The Files page: what the Upload button does (who can upload, for which office), the Action column and the Description values once a file exists (screenshot needed).
- [ ] "Amount payable to the BFP" is the amount payable to the Bureau of Fire Protection; confirm the label and meaning.
- [ ] What Current Dues and Annually Dues mean for a new business (both show 0.00 in the example).
- [ ] The Assessment button is greyed out because the assessment was already run on Approve (code: disabled when the assessment header exists).
- [ ] The five lists: For Assessment, Assessed For Payment, Paid Assessment Request, Semi-Annual/Quarter Transaction, Closure Transaction (meanings from the code).

## Section 5: Offices (Engineering used as the example)
- [ ] Full names of the offices: Municipal Assessor's Office, Municipal Engineering Office, Bureau of Fire Protection (BFP), Public Employment Service Office (PESO), Municipal Agriculture Office (MAO), Municipal Environment and Natural Resources Office (MENRO), Municipal Planning and Development Office (MPDO), Rural Health Unit (RHU), Business Permits and Licensing Office (BPLO). Standard Philippine LGU office names assumed; confirm for Oas.
- [ ] Which fees belong to which office (the "In the example" lines are guesses from the fee names and requirements seen in the test request).
- [ ] The office rules in 11.3 come from the code: request appears after assessment; amount needed to act; first-quarter or annual only.
- [ ] Offices can add, change and remove fees in their own assessment section (Add Fee, pencil, trash), seen on screen for Engineering. Confirm this is intended for every office and what it does to the total.
- [ ] "New Requirements" lets an office add requirements for the applicant (the ticked ones are the requirements already asked for; the sample showed "Building Permit / Occupancy Permit" unticked and the mechanical permit ticked). Confirm what Save does for the applicant.
- [x] The Approved window (Remarks required, buttons No and Yes) and the message "Request Approved Successful" were seen on screen; counts on the dashboard change.
- [x] The Disapproved window (Remarks required, No and Yes) seen on screen.
- [ ] After disapproving, the message still reads "Request Approved Successful" (wording in the system; ask the developers to show "Request Disapproved Successful").
- [ ] Changing a decision: the button of the current status is greyed out and the other two stay available (seen on screen). Until when a decision can be changed (for example after BPLO approval or payment) is not confirmed.
- [ ] The Pending window (what the Pending button asks for; code: PENDING REQUEST with remarks).
- [ ] The "Request With Attachment" panel on the office dashboard (what it lists).
- [ ] The Holdings and Requirements pages of an office (not yet documented).

## Section 5.7: Office inquiries
- [ ] The office opens the Inquiries page through the Make Inquiry link in Business Information (the top bar chat icon also lists inquiries; the code links it to /<role>/inquiry).
- [ ] An inquiry sent by an office appears in the list under the name "ENGINEERING" (the office name) while one from the applicant shows the applicant's name; confirm how names are shown.
- [ ] The office can reply in the conversation with the Message box and send icon (cropped out of the screenshot because of a screenshot overlay); a capture of the Message box is needed.

## Sections 5.8 to 5.10: office report, holdings and requirements
- [x] The two icons next to Search Business: download as PDF and download as .xlsx (confirmed by the project owner).
- [ ] The Amount column of Request For Clearances (what it totals; sample rows show 0.00 and 3,560.00).
- [ ] Holdings: the tick boxes and View Map (assumed: tick businesses, then View Map). Link Accounts lock icon opens "Users account users this business." with the name and email of linked accounts (names hidden in the figure).
- [ ] Requirements: meaning of "Is Default" and "Business Type" (empty business type), the Attachments file, and the New / Renewal / Transfer / Closure tick boxes. The page title reads "List Of Requirments" (typo).
- [x] Requirements: the Edit Requirements window seen (same fields as New Requirements, with the tick boxes).
- [ ] Select Business Type is a searchable list (typing narrows it); confirm.
- [ ] Whether adding, changing or removing an office requirement changes what applicants see on new and existing requests.

## Section 4.9 Add or edit fees
- [x] The Edit Fees Amount window seen: Enter Amount, Update, Close.
- [ ] The trash icon removes a fee at once with no confirmation window; confirm on the live site.
- [ ] System typos: "Fee succesfully added to installment.", "Fee succesfully updated.", "Fee succesfully removed." ("succesfully").
- [ ] Rules in the code: amount of 1 or more; for the tax refund fee only negative amounts are allowed. Confirm what the Penalty fee amount rule is.
- [ ] Whether the fee changes also change the totals shown on the Assessment Request page (Total Assessment, Current Dues).

## Section 4.10 For Approval
- [ ] The tip on the For Approval button reads "Approved to enable bplo actions". Confirm what it means for the user.
- [ ] After sending, the Assessment, Add/Edit Fees and For Approval buttons are gray; confirm the evaluator cannot change the assessment until the BPLO acts or a rollback is done.
- [ ] System wording: the success message reads "Request successfully added to assessment" even though the request is sent for approval.
- [ ] Figure with the empty-box error was taken on a request with different totals (3,610.00) than the other figures (1,440.00). Retake with the test request if exact figures matter.

## Section 6 Municipal Treasurer's Office (eBPLS Assessment)
- [ ] Confirm the account eBPLS Assessment (route /bplo, office "bplo") is the Municipal Treasurer's Office, and that Section 5 and 10 should call it that instead of "Business Permits and Licensing Office".
- [ ] Summary of Collection per Barangay: clicking it showed the Registered Businesses page again (address shown was /bplo/report/summary-collection, which has no route in the code). Check what the page does.
- [x] View Map becomes active when a business is ticked; it shows a map with View List to return (confirmed).
- [ ] Index Of Payments: the code has a second page per business (/report/index-of-payments/:busCode). Screenshot needed.
- [ ] Fees Account: what the arrow icon, the edit icon and New Fees Account do. Fees Template: New Fees Template and edit windows.
- [ ] Download Excel and Print Report on the reports: confirm they become active only after Generate.
- [ ] "Registered Businesses" breadcrumb appears on the Business Category per Account page (system wording).
- [ ] What the Mail, Chat and Calendar items open for this account.

## Section 6.6 Review a request (Municipal Treasurer's Office)
- [ ] "Assessment - MTO": MTO is read as Municipal Treasurer's Office; confirm.
- [ ] The Actions panel label reads "CURRRENT STATUS" (three r) in the system.
- [ ] What the Logs link and Add Arrears window do; what Location and Files show.
- [ ] Messages after adding, editing and removing a fee as MTO (not seen). The window titles seen: Add Fees To Installment, EDIT AMOUNT (No/Save), "Are you sure you want to remove this fee?" (Remove/Cancel).
- [ ] Total Fees (MTO list, 1,040.00 in the example) versus Total Assessment on the Permit Evaluator side (1,440.00): confirm what each total covers.
- [ ] Approved and Disapproved windows and messages for this office.
- [ ] Moderator Remarks panel shows "Approved Date" and "Approved Remarks" (the Permit Evaluator's For Approval remarks); confirm.
- [ ] MTO "Total Fees" (1,040.00) vs Assessment Details "Total LGU Fees" (1,440.00): MTO list is likely this office's own fees only; confirm. "Amount payable to the BFP" shows 534.00 here.
- [ ] New Requirements window (MTO): adds requirements to the request; confirm what happens after Save (message, does the applicant see it).
- [ ] Approve/Disapprove/Pending windows (MTO) are titled APPROVED REQUEST, DISAPPROVED REQUEST, PENDING REQUEST, each with a required Remarks box and No/Yes. Messages: "Request approved successful." and "Request disapproved successful." (system wording). Message after Pending: "Request pending successful."
- [ ] After approval, does the request move on to Permit Issuance or to the Permit Evaluator for payment? (The dashboard shows an "For MP Preparation" list for this office.)
- [ ] Files page: what the Action column holds once a file is uploaded; the upload window text says "browse thorough your machine" (typo).
- [ ] Location page: pin comes from the business location the applicant saved.
- [ ] Processed Time (e.g., "38 minutes") appears in Business Information after approval; confirm meaning.
- [ ] The applicant sees this office as "BPLO" in the status list (remarks example "Approved Final 1"); confirm the Municipal Treasurer's Office is the account behind BPLO, and that FOR PAYMENT follows its approval.
- [ ] Orange dot for Engineering in the applicant status list: which action produced it (Pending or Disapproved)?
- [ ] The map after View Map showed the whole region without a pin at the default zoom; confirm that the ticked businesses appear as pins when zoomed in.
- [ ] Request For Clearances (MTO): the column heading reads "Trasaction Type" (system typo). Amount and Total in the example: 3,560.00 (test business), total 12,030.00; confirm what Amount covers (assessment total vs fees).
- [ ] Registered Businesses Excel: sheet "Report"; headings partly cut in the screenshot (Business Tax, Amount Paid, "OR N..."); confirm the exact heading of the last column (OR number?) and that the Excel has the extra columns Capital, Gross, Total Assessment.
- [ ] Print Report opens the browser print window (not a PDF file by itself).
- [ ] Edit Company page (Holdings): screenshot showed only the top part (General Information up to Company Email). Need the rest of the page and the Save message. Business Type was empty for the example business and is marked required.
- [ ] Business Category per Account: only SERVICES appeared for the period (test data has TRADING too); confirm whether categories without collections are left out. Business Summary default start date was January 1st in this screenshot (October 1st on first open).
- [ ] Summary Report: Collections figures (2,890.00 new, 3,460.00 renewed) vs totals elsewhere; confirm they are amounts paid.
- [ ] Fees Account: "Account - 1" label above the account code (meaning?). The window for adding an amount is titled "New Fees Account" like the one for a new account (system naming). Type Of Charging is grayed (Fixed Amount); other types exist in the New Fees Account window (list not seen).
- [ ] Fees Account: windows for the edit icon of a fee and of an amount, the trash icon, and messages after saving not seen.
- [ ] Fees Template: the window for a new template is titled "New Business Category" (system naming) and has Business Type, Fees Account, Fees Type. Confirm that the edit window (same title, filled with SERVICES and Regulatory Fee, Fees Account empty) is the one opened by the edit icon.
- [ ] Fees Template: meaning and use of a template (does the assessment use it to choose fees per category?). Trash confirmation and messages not seen.

## Section 3.9 Approved request: assessment details and payment
- [ ] The page opened by the arrow icon of a FOR PAYMENT request: the screenshot showed only the totals (Total Assessment 1,440.00, Current Dues 3,560.00, Annually Dues 0.00, Amount payable to the BFP 534.00). Need the whole page and the list of fees, and which amount the applicant pays (Current Dues?).
- [x] The print icon opens the assessment form "Application For Mayor's Permit" with a Print Assessment button (seen). Whether the applicant must bring the printout to the municipal hall is still to confirm.
- [ ] After payment: confirm the staff record it (OR number, Section 4 onward) and the request moves to Permit Issuance.

## Section 3.10 After payment: MP Preparation and MP for Pickup
- [ ] Statuses on the applicant list seen: "MP PREPARATION" and "PERMIT IS READY FOR PICKUP" (the pickup label differs from the "MP for Pickup" wording first given).
- [x] MP for Pickup: the applicant opens the permit with the second icon, View File, and downloads the PDF (seen). Still to confirm: whether a printed copy is also released at the municipal hall, and what to bring.
- [ ] Section for the Permit Issuance staff (For MP Preparation, print, set for release) still to be written.

## Section 7 Permit Issuance
- [ ] What the refresh, document and paperclip icons do in For MP Preparation, and the MP Printed tick box.
- [ ] The Print Permit button (print window not seen) and when the request moves to MP For Release; how a request is set for release and how the Receiver is recorded; the three-dot menu.
- [ ] Semi-Annual/Quarter Transaction and Closure Transaction lists were not seen.
- [ ] The message "Plate number and license number successfully added." was captured while the MP For Release list was open; confirm the usual place of the message.
- [ ] Applicant status changes: MP Preparation after the MTO processes payment, MP for Pickup after the permit is uploaded (to confirm on the applicant list).

## Reports (shared by Permit Evaluator, Permit Issuance and Municipal Treasurer's Office)
- [ ] Reports are documented once in Section 6.4. Confirm that the three accounts (and any other that shows Reports) really have the same reports and rights.
- [ ] The system message for an empty Requirement reads "Requeirement is required" (typo, seen on the Permit Issuance account).
- [ ] Index Of Payments rows end with an arrow icon; the page it opens has not been seen.
- [ ] Summary of Collection per Barangay: page title is "Summary Report" (same as Business Summary).
