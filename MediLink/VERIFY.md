# Items to verify on the live site (MediLink)

Things seen while preparing the MediLink user manuals that need checking or fixing. They are kept out of the manual text.

## Secretary
- [ ] Laboratory and Imaging attachments (3.6): when a row was opened with the arrow (›), the attached images showed as broken image icons. Check that uploaded images display.
- [ ] Upload images panel says "Select imaging raw result" on the Laboratory tab too. Should read "Select laboratory result" (or similar) there.
- [ ] After an upload the message reads "Updated test successfully". Suggest "Attachment uploaded successfully".
- [ ] Cancel confirmation reads "Are you to remove this appointment?" (missing "sure").
- [ ] After cancelling, the message reads "Appointment followup updated successfully" (the same message as Set As Done on Follow Up). Suggest "Appointment cancelled".
- [ ] Can a cancelled appointment be restored?
- [ ] "RESCHEDULE APPOINMENT" button label typo.
- [ ] Appointment and patient search is case-sensitive ("david" finds nothing).
- [ ] Add Patient: every account created with an email gets the same default password "hello123", and the message shows it on screen. Consider a random password or a forced change on first sign-in.
- [ ] Add Patient: Birth Date accepted the year 0002 (04/06/0002). Add a date check.
- [ ] Account › General › State list shows Alabama, New York, San Francisco and Philippines.

## Doctor
- [ ] Services: does the bin icon ask for confirmation before removing a service? Can a removed service be restored?
- [ ] Set Complete with SET FOLLOW-UP: confirm the follow-up appears on the Secretary's Follow Up list.
- [ ] How changes on the Allergies screen are saved (no Save button shown).
- [ ] Pain Monitoring: the rating step after clicking the body chart.
- [ ] "Hearth Pulse" label typo.

## Imaging and Laboratory
- [ ] Patient List was empty for both roles, so opening a patient and entering a result are not yet documented. Needs a pending request from a doctor.
- [ ] Laboratory sample result: "DIFFIRENTIAL COUNT", "NEUROPHIL", and the reversed range "215 - 177".
- [ ] Printable result header shows "SAMPLE COMPANY" / "SAMPLE COMPANY ADDRESS" instead of the clinic.

## Admin
- [ ] Staff forms show "Invalid Date Format" under Birth Date before anything is typed.
- [ ] GET DIRECTION and LOCATION (map) not tested.
- [ ] Results of CREATE, SAVE and UPDATE not observed (nothing was saved during capture).
