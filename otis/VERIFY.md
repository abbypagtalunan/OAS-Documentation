# OTIS manual: items to verify

Section 1 (Admin) was written from the code in TIS-OAS and from the live site at tis.oas.lguapp.com (view only, nothing saved).

- Name: the cover and text use "Treasury Information System (TIS)" from the landing page. The team also calls it OTIS; confirm which to print.
- Search on Users: the code compares the typed text without changing its case, so capital letters may not match. The manual says to type in small letters. Not tested live.
- Add User > Role: the list shows the first role by default, but the form value starts empty. If the role is not picked, the form may say Required. Not tested (it would need a save attempt).
- A new role has no sidebar menu: from the code (the menu is chosen by exact role name). Not tested live.
- Assigned personnel are loaded at sign in (login payload). The manual tells the admin to ask the user to sign in again. Not tested live.
- Public OR Template: no screen uses the groups; the assign function is commented out in the code. Ask what the groups are for.
- Success messages (User created/updated, Role created/updated, Group template created/updated, RPT user assigned, Personnel added/deleted, Assigned RPT deleted) are from the code. They were not triggered live because the work was view only.
- Seen live and captured: the Role, RPT User, Personnel Officer and List drop-downs, the Required messages of Add User, and the two delete questions (closed with No, nothing removed).
- Screenshots: names, emails and officer names are covered. The two group names (GROUP 1s, GROUP 2x) are test data and are shown.

## Section 2 (Referential)

Captured live, view only (windows opened and closed with Esc, delete questions opened but never confirmed).

- The delete question was opened live only on Fund Group. The other delete questions and all success messages (created / updated / deleted successfully) come from the code.
- Accountable Forms: the Delete icon shows only when `ticket_status === 'nothing'` (code). No row with a Delete icon was seen live.
- Accountable Forms and Check Booklets: Start No. fills End No. (+49), Quantity 50 and Balance, and Amount = Unit Value x Quantity (code and live form). The save error "O.R already exist in the system" is from the code.
- Account Code: the two-step Add (Account Code + Check, then the full form) is from the code and the live first step. The full Add form was not opened live (it needs a new unused code); the Edit window shows the same boxes.
- The window "Edit Account Code" is taller than a small screen; the Update button is below the visible area unless the window is scrolled (seen at a 1149 px wide pane).
- FPP Code, Seq/Sub Seq/Group/Sub Group Code: their lists show only the dash at present.
- Program Code, Accountant and Mayor have no records, so their Edit windows were not captured. Check Booklets has one record but no Edit or Delete icon.
- SL Code list (1011, 1016) and the Liquidating Officer list were read from the page, not captured as figures.
- Spelling as shown by the system: "ACCOUTANTABLE OFFICER", "TO PROVICIAL GOVERNMENT".
- Blurred in figures: officer and payee names, the bank account number, the Signatory, the user name and email.
- Section 2.6.10 (OR Template and Collection Type): the sample (006 Amusement and its eight OR template lines) was read live by typing the word in the two Search boxes (a filter only). "Where the cashier sees it" comes from the code (the issuance screen loads the OR template lines of the chosen collection type, `get/template-by-id`); it was not shown live. Confirm when the Transaction section is written.
- Section 1.2.5 / 1.2.6 relationship blocks (assigned RPT and assigned personnel) are from the code, not tested live: the Encoded By list of the RCD import window is built from the user's assigned RPT users; the permit receipt pages accept a receipt only if its collector is one of the user's assigned personnel (message "You are not allowed to proccess this personnel."); RCD Processing lists only assigned personnel of type COLLECTOR. Checked for Building Permit; Business Permit and Burial Permit use the same assigned-personnel list. Confirm when the Transaction section is written.

- Accountable Forms: the manual states that the OR number range is always 50 (as instructed). In the code the End No. box can be edited, so a different range is technically possible; the manual tells the reader to keep the End No. that the system fills in.
- Check Booklets: the one record on the page was first described as "no record" by mistake; corrected.

## Section 3 (Transaction)

Viewed live without saving. Buttons that change a receipt were not pressed (the browser safety check also blocked the Erase button).

- From the code only (not opened live): the template question and Add Template; Add Check window; Save, Print OR, Edit, Erase, Mark As Cancelled (no confirmation question in the code for Mark As Cancelled); Business Permit and Building Permit search results (Filter, Retrieve) and the marking of the assessment as paid; the CTC Corp and Burial Permit forms (no open booklet number was found live); Set Payment and Upload Attachment windows; Query Result tab and the Query filter window; the DV Create and status toggle; the messages of RCI.
- Seen live: the menu, the entry screens, Select OR To Print, an open receipt number (form and booklet panel), the Gender and Collection Type lists, "O.R # NOT FOUND!", "O.R # ALREADY USED!" with a saved receipt, Filter To Display (Business and Building), the CTC Ind form, the Online Request list and details, the DV list, Add Record, Type list, Checks Entry, Query, RCI, Preview Print; Source and Report tabs are empty.
- "Online Request" origin (people request online) is inferred from the customer pages in the code; the record shown is a test record.
- DV signatories come from the ACTIVE accountant, treasurer and mayor (code: get/*/active).
- The CTC "x 12" boxes: shown as on screen; the exact tax computation was not checked.

- Business Permit Filter was tried live with a business name search ("store", "a") and returned no list on screen, so the result list could not be shown. Retrieve was NOT pressed: in the code, Retrieve calls get/api-assessment-list, which writes the assessment lines to the receipt number (bulkCreate into issuance_or). The text about Retrieve comes from the code.

## Section 4 (Process)

- Seen live: both pages, the Process RCD and Process RCLO windows, the Collector and Form Code lists, the RCD and RCLO lists, and Retrieve (a read only lookup) on both pages.
- NOT pressed (from the code): Process and Remove on both pages. Process writes the RCD/RCLO number onto all receipts of the range; Remove frees them. The number formats (fund + collector code + date + running number) are from the code and from the numbers on the lists.
- The Collector list showing only assigned collectors is from the code (assigned personnel of type COLLECTOR); the live list showed three collectors for this admin user.
- "Balance = 50 minus Qty sold" is read from the table values (49 sold gives balance 1).
- Collector and officer names are blurred in the figures.

## Section 5 (Reports)

- Seen live: the menu, all five reports, their filter windows, and the read only filters (Filter, Search, Retrieve) for each; the Import RPT window and the Add Deposit window (opened, nothing created).
- NOT done: Print (and the printed form pages), Export To Excel (downloads a file), Import (saves RPT receipts), Create deposit.
- Messages (Collector required!, Fund required!, date errors, Encoded by is required, No rpt permit OR records found, No OR records to import, RCLO deposits created successfully) are from the code.
- The RCD report amount of RCD 100(01)JRR09102026022 shows 14,880.00 on its page and 14,970.00 in the RCD No. List and in RCLO Processing. Not explained; ask the treasury.
- Names (payees, officers, collectors, treasurer) are blurred.
