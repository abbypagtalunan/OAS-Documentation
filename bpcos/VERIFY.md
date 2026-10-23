# Items to verify on the live site (BPCOS)

## Project-wide
- [ ] Official system name: "Building Permit & Certificate of Occupancy System" (from the OAS home page card). Confirm spelling and the short name BPCOS.
- [ ] Roles of the system (applicant, engineers, building official, etc.) and what each role does.
- [ ] Is there a test account for each role and a dummy applicant to use in the figures?
- [ ] Payment: online or on site?

## Section 1 / 2
- [ ] The login page says "Sign in on the internal platform" (wording of the system). Confirm whether applicants use the same page.
- [ ] "How to's (Guide)" link on the login page: what it opens.
- [ ] Cookie notice and the "Settings Updated" message that appear on first visit.

## From the code (first pass)
- [ ] Order of the offices' review and the list of statuses (Administrator, Application Status page).
- [ ] The Affiliate role: what it sees and who uses it.
- [ ] Online payment (Paynamics) or on site? Is the AI fee suggestion (analyze plans) on?
- [ ] Domain typo in `update guide.txt` (lguap.com vs lguapp.com).

## From the building permit form screenshots (Section 3.5)
- Summary step shows "Total Estimated Cost NaN" even though 3,000,000 was typed (bug?). The Summary figure showing the costs was left out of the manual.
- System typos corrected in the manual text: "For contruction own by an enterprises", "Form of owership", "Proposed date of contruction", "LICENSE ARCHITECT OR CIVL ENGINEER", "This portion is need to be notarize" (kept as quoted).
- Confirm: the final step button reads "Save As Draft" but it submits the request ("Request successfully sent.") and opens the Requirements List. Is the application a draft at that point, and what status does it have?
- Confirm: "Proceed to Permitting" is enabled only when all required files are attached (from code).
- Confirm what "Save As Draft" on the Requirements List does (code only opens the Permit List).
- Status "DRAFT" is code 1 (from code). Edit is enabled only for status 1; Assessments is dimmed for status 1; Apply For Electrical is enabled only for status code 9 (which label is that?); View Permit shows for approved applications.
- Details window: "Update Details" is always dimmed (the code's disabled condition is always true). Bug? Edit is the way to change an application.
- Does the Remarks window show remarks from every office, and which statuses appear?
- Proceed to Permitting is dimmed in the screenshots although every requirement shown is OPTIONAL. In code it needs all required requirements to have files and the status to be draft or declined. Which requirements are required, and is that why it is dimmed?
- What does OBO stand for in the status SENT TO OBO (Office of the Building Official)? And who reviews the requirements first: the requirements reviewer or the OBO?
- Analyze for Assessment: which file types can be analyzed, and is the AI fee suggestion switched on in production? Does the applicant see its result?
- Upload Requirement: the Remarks box is required (from code). Which file types and sizes are accepted?

## Reviewer (Section 4)
- The signed-in role reads "Reviewer" (sidebar: For Engineering, Processed Permits, Processed Permits For Occupancy, Processed Permits For Electrical). Is it the same as the Requirements Reviewer role (id 13) or the Reviewer (id 7)? The code sets "review started" with is_review_started_by 'reviewer' and status_code 13 (comment: Application under review), while the applicant's submit also sets 13 (sent to OBO). Is that right?
- For the Reviewer role the second button (set as reviewed) is hidden in code. Who does the actual review of the requirements, and how does an application reach For Engineering?
- What the icons of Processed Permits open (chevron, paperclip, arrow) and what Assessment shows for the Reviewer.
- What View Reviews shows and which offices write the remarks.
- Typos on screen kept out of the manual text: "Application Requirements" fine; "CIVL ENGINEER" in the form.

## Building Official (Section 5)
- Icons of the Building Permit card come from the code tooltips: Remarks, Attachments, Assessments, Approve Permit, Disapproved Permit. Confirm what each opens.
- Building Permit For Print: what the Status tags NOT-SET and APPROVED FOR PAYMENT mean (print status or payment status?), and what Print produces. FSEC button opens "New FSEC" (FSEC No. and date issued) per code.
- The Approved Permits card shows rows without a Building Permit No. (May 26 and May 21 rows). Is the number assigned at printing?
- Building Official, Application Requirements: Proceed For Printing is dimmed until the fees are assessed (from code). Confirm that it is what sends the application to payment/printing, and what View Reviews shows.
- The Building Official's decision on a requirement (Approve/Decline with required remarks): does the applicant see the remarks and status? A declined requirement: does the applicant re-upload, and does the application return to the applicant?
- Order of Payment (from code, not seen on screen): which fee category is amount-only ("Enter amount", code 4-02-01-010-20-10), and what the edit icon of an assessed fee opens. The fee category "Filing Fees" shows on screen as "Filling Fees" (typo); corrected in the manual text.
- Pending Assessment Fees: confirm the AI suggestion feature is on in production (the code notes OPENAI_API_KEY must be configured) and who sees the suggestions (Engineering only).
- The Assessments check box icon in Actions opens the assessment directly (from the code tooltip). Confirm.
- Approve Permit: the Building Official types the Building Permit No. by hand. Is it free text or must it follow a numbering rule? After approval, what happens next in the flow: payment by the applicant (Permit For Payment), then For Print?
- Decline Permit (the button reads "Declined"): does the applicant see the reason and can they correct and resubmit? What status does the applicant see?
- Applicant, Approved: does View Permit appear in the menu (from code) and what does it show?
- View Permit (applicant): the permit shows "BUILDING PERMIT NO.: 108" (the reference number) while the list shows Building Permit No 112233. Which is right? FSEC No. and its date show None. The permit can be viewed before payment (Official Receipt No. and Date Paid are N/A).
- Applicant remarks after approval show "Approved" and "Approved For Printing" from Approver: the second comes from Proceed For Printing? Confirm.
- After approval the applicant menu enables Assessments and View Permit; "Permit For Payment" still to be shown.

## Payment (from the code)
- Online Payment (Paynamics): the code exists, but the applicant's "Online Payment" button has its click action commented out and shows a tooltip to contact the permit office email. Treat online payment as OFF. Confirm.
- Treasury "Set as paid" (POST /api/treasury/building/permit/set-aspaid) creates the payment record, sets treasury_approved = 1 and status_code = 9, and logs to LGU OAS. Status 9 is also the status at which "Apply For Electrical" is enabled.
- A shared API (api.bpcos.oas.lguapp.com/api/shared/building-permit/assessments and set-assessments-as-paid, headers x-ebpls-apicode / x-ebpls-apisecret) lets another system read unpaid assessments and mark them paid, with the same effect as Treasury. Which system calls it (eBPLS Municipal Treasurer's Office?) is not in the repos I have.
- LGU OAS (api.oas.lguapp.com) receives transaction logs and supplies the applicant's registered email.
- SECURITY: api/app/config/auth.config.js in the repo holds credentials in plain text (JWT secret, LGU OAS API secret, AWS keys, SMTP login, OpenAI key). They should be moved to environment variables and rotated. Do not copy them into the manual.
