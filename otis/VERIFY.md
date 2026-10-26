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
- Program Code, Accountant, Mayor and Check Booklets have no records, so their Edit windows were not captured.
- SL Code list (1011, 1016) and the Liquidating Officer list were read from the page, not captured as figures.
- Spelling as shown by the system: "ACCOUTANTABLE OFFICER", "TO PROVICIAL GOVERNMENT".
- Blurred in figures: officer and payee names, the bank account number, the Signatory, the user name and email.
- Section 2.6.10 (OR Template and Collection Type): the sample (006 Amusement and its eight OR template lines) was read live by typing the word in the two Search boxes (a filter only). "Where the cashier sees it" comes from the code (the issuance screen loads the OR template lines of the chosen collection type, `get/template-by-id`); it was not shown live. Confirm when the Transaction section is written.
- Section 1.2.5 / 1.2.6 relationship blocks (assigned RPT and assigned personnel) are from the code, not tested live: the Encoded By list of the RCD import window is built from the user's assigned RPT users; the permit receipt pages accept a receipt only if its collector is one of the user's assigned personnel (message "You are not allowed to proccess this personnel."); RCD Processing lists only assigned personnel of type COLLECTOR. Checked for Building Permit; Business Permit and Burial Permit use the same assigned-personnel list. Confirm when the Transaction section is written.
