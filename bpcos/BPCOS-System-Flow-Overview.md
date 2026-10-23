# BPCOS system flow overview (first pass, from the code)

Source: `../ebpls-engineering-oas` (React app in `app/`, Node/Express/Sequelize API with PostgreSQL in `api/`).
Live site: https://bpcos.oas.lguapp.com (API: https://api.bpcos.oas.lguapp.com).
This is a first reading. Items marked (?) need confirmation on the live site.

## Roles (from the route guards, the sidebars and `utils/constant.js`)
| Role | Role id | What its pages show |
|---|---|---|
| Applicant (`user`) | | Building Permit (new), Permit List (List, Draft), Permit For Payment, Occupancy Permit (New, List), Electrical Permit (List), Inquiries, Account |
| Affiliate (`affiliate`) | | Dashboard and a read-only view of a permit (?) |
| Engineering (also called Approver) | 6 | Processed (Building Permit, For Print), Building / Occupancy / Electrical Permits, assessment of fees, printing the permit and the assessment, Inquiries |
| Reviewer | 7 | For Engineering, Processed Permits (building, occupancy, electrical) |
| Fire | 8 | Processed Permits (building and occupancy), assessment and requirements view |
| MPDO | 9 | Approved Permits, assessment and requirements view |
| Treasury | 12 | Paid Bldg Permit, Paid Occupancy Permit, Paid Electrical Permit |
| Requirements Reviewer | 13 | For Engineering, Processed Permits (building, occupancy, electrical) |
| Electrical Reviewer | 14 | Plan review (building plans) |
| Architectural Reviewer | 15 | Plan review |
| Structural Reviewer | 16 | Plan review |
| Plumbing Reviewer | 17 | Plan review |
| Line and Grade reviewer | (?) | Plan review |
| Administrator (`admin`) | | Reports, Payments, Users, Roles, and the setup tables below |

Administrator setup tables: Municipality, Barangay, Application Type, Scope of Work, Form of Ownership, Group Use, Character of Occupancy, Application Status, Fees Type, Fees Account, Grouping of Requirements, List of Requirements.

## Permit lifecycle (what the code shows)
1. **Applicant requests a building permit.** A 4-step form: Owner/Applicant details, Structure profile, Full time inspectors, Summary. A request can be saved as a draft. Scope of work and character of occupancy are chosen in the form.
2. **Applicant uploads the requirements.** Requirements come from the setup lists (grouped), including special requirements per role. There are two versions of the upload page (v1 and v2). The applicant sends the files to the Requirements Reviewer.
3. **Review by the offices.** The application has one approval flag per office in `application_bldg_permit_status_by_office`: requirements reviewer, reviewer, plumbing, electrical, architectural, structural, line and grade, fire, MPDO and engineering. Each office approves or declines with remarks. The permit status code changes with each action (the status table is data in the database: 13 = sent to the office of the building official and under review, 6 = declined; the others are loaded from the Application Status setup table) (?).
4. **Engineering assessment.** Engineering builds the assessment of fees (building, accessory structure and fee, electrical, mechanical, plumbing, electronics, certificate of occupancy, annual inspection) from the active fee rates. A v2 flow can suggest fees by reading the uploaded plans (an AI extraction step: the applicant page "analyze-assessment" and the prompt guide in `api/app/prompt`). Suggested fees stay pending until Engineering accepts or removes them. Engineering prints the assessment.
5. **Payment.** The permit appears in the applicant's Permit For Payment list and in the Treasury For Payment list. Treasury sets it as paid with an OR number. There is also an online payment (Paynamics) and a shared API that other systems (for example eBPLS) use to read unpaid assessments and set them as paid.
6. **Printing the permit.** After payment, Engineering prints the building permit (For Print).
7. **Occupancy permit.** After the building is done, the applicant requests a certificate of occupancy. It has its own requirements, assessment (certificate of occupancy fee rates), fire safety inspection certificate record (FSIC), review, payment and printing.
8. **Electrical permit.** A separate request with its own list, review by the Electrical Reviewer and Engineering, payment and printable form.
9. **Rollback.** A permit can be rolled back to the office of the building official (`rollback/to-obo`).
10. **Inquiries and notifications** work like in eBPLS (a chat per application).

## Open questions
- The order in which the offices review (all at once, or in sequence?) and which statuses the Administrator's Application Status table holds.
- Who sees the Affiliate role and what it is for.
- Whether the AI fee suggestion is on in production.
- Whether the online payment (Paynamics) is on, or payment is on site as in eBPLS.
- The official names of the roles (for example "Office of the Building Official").
