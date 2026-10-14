# eBPLS OAS: System Flow Overview (from code review)

Sources: `full-ebpls-oas/app` (React), `full-ebpls-oas/api` (Node/Express/Sequelize/PostgreSQL), `app/docs/Flow.md`.
App: https://ebpls.oas.lguapp.com · API: https://api.ebpls.oas.lguapp.com
Items marked **[verify]** are inferred from code and must be confirmed on the live site.

---

## 1. Roles and what each can see

| Role (`roles[0].name`) | Landing page | Sidebar |
|---|---|---|
| `user` (business owner / applicant) | `/app/reports/dashboard` | Business list (Companies), Payment History, Mail, Chat, Calendar |
| `permit-evaluator` | `/permit-evaluator/dashboard` | Assessment, Rollback Assessment, Companies, Requirements Lists, Reports (6) |
| `bplo` | `/bplo/dashboard` | Companies, Requirements Lists, Request For Clearances, Holdings, Reports (6), Fees Account, Fees Template |
| `permit-issuance` | `/permit-issuance/dashboard` | Companies, Requirements Lists, Reports (6). The For Assessment page holds the MP tabs |
| `moderator` | `/moderator/dashboard` | Assessment and MP, Business Registration, Companies, Requirements Lists, Rollback Assessment, References (Business Type, Business Category, Barangay, Office, Fees Account, Fees Template), Reports (6) |
| `admin` | `/administrator/dashboard` | Payments, List of Business Transaction, Users Administration, Requirements List, Reports (6), OLAPP (Services, Requirements Group, Requirements List, Announcements) |
| Clearance offices: `fire`, `assessor`, `engineering`, `menro`, `mao`, `mpdo`, `rhu`, `peso`, `barangay-*` (one account per barangay) | `/<role>/dashboard` | Request For Clearances, Holdings, Requirements |
| `affiliate` | `/affiliate/dashboard` | QR scanner result, view Mayor's Permit |

Reports (6): Registered Businesses · Index of Payments · Closed Businesses · Bus Category Per-Account · Business Summary · Summary of Collection per Barangay.

Role-guard behavior: each route is protected by a guard that redirects a wrong-role user to their own dashboard. Not logged in → `/login`.

---

## 2. Account access (applicant)

1. **Register** (`/register`): First Name, Last Name, Email, Password (min 7), Gender, accept policy → a code is emailed.
2. **Verify** (code screen): enter the Verification Code → "Registration completed!" Wrong code → "Code Invalid".
3. **Login** (`/login`): Email Address + Password. There is also `/login/external` (external login).
4. **Recover password**: `/recover/password` → emailed link → `/recover/password/reset-form/:email/:token`.
5. **Account** page: update profile, profile picture, email, password.

---

## 3. Business (holding) records: applicant and staff

- **Applicant**: Companies list (tabs: General Info, Registration, Registered Owner, Miscellaneous) → Create company.
- Company form fields: Business Name, Franchise Name, Category, Type, Owner Type, Business Line, Address (Street, Barangay, Municipality, Province), Phone, Email, Lat/Long, SEC No./Date, DTI No./Date, TIN, PhilHealth, SSS, HDMF, Owner details, Representative, Capitalization, No. of Employees.
- **Enrolling an existing business to a user**: the applicant sends a "Business Registration Request" with attachments. Moderator or permit-evaluator opens **Business Registration → Request for Enrollment** (columns User / Subject / Description; actions View attachments and Set as process), or directly enrolls and removes a business from a user's holdings. The applicant is notified.
- Staff (Moderator, Permit Evaluator, BPLO) also have Companies → New / Edit.

---

## 4. The permit lifecycle (main flow)

Alignment note: `app/docs/Flow.md` describes the "regular" flow. The code shows an extra front step (the sworn/"New Request" step) that Flow.md folds into step 1.

### Step A. Applicant files an Assessment Request
- Path: Companies → business → Assessment → **Request**.
- Request Form fields: Transaction Year, **Transaction Type** (N New / R Renewal / T Transfer / C Closure), Gross Income (renewal) or Capitalization (new), No. of Employees, Total Floor Area, No. of Storey, Contact No, Owner Name, Authorized Representative, **Payment Mode** (Y Annual / S Semi-Annual / Q Quarterly) and the quarter(s).
- Required requirement attachments are uploaded per quarter or per year. A required item with no file blocks submission.
- Backend creates `req_for_assessment` (`sworn = 0`) and attaches the requirement checklist per office (`checklist_per_role`, `checklist_per_assessment`).
- If the DTI registration is expired but within the grace period, BPLO is auto-set to approved with a remark.

### Step B. Permit Evaluator: **New Request** → Approved
- Dashboard → *Assessment Request* → **New Request** (columns: Date, Business, Period, Quarter, Type, Action). Filters: Search business, Year.
- Opens the details form and the evaluator completes/validates: Business Category, Business Type, Transaction Date/Type, Business Year, Owner Type (Corporation, Cooperative, Foundation, Partnership, Sole Proprietor), Capitalization or Gross Sales / Daily Sales ×360, No. of Employees, Years Arrears, CTC Number, Date and Place of Issue, Payment Mode (Annual / Semi-Annual / Quarterly, with quarter choice disabled where already used).
- Action: approve the sworn declaration ("Sworn successfully approve"). Request moves to the **Approved** list on the same dashboard.

### Step C. Permit Evaluator: **For Assessment**
- Page: *For Assessment*. Columns: Date, Business, Period, Quarter, Type, **Assessment Status** (Pending / For Approval), Action. Filter: All / Pending. Tooltip icons include Certificates and view fees.
- Open the request → system computes fees (renewal vs new-business fee lists, local business tax, FSIC, etc.) → "Request successfully added to assessment".
- Evaluator can **add / update / remove fees** (Add Fees, Edit Fees Amount, Remove Fee), view Request Details, and print the assessment (`AssessmentPrintPage`).
- Requirements by office can be reviewed (Requirements Per Assessment).
- To submit: enter **Remarks** (required) and click **For Approval** → state "For Approval", pending BPLO.

### Step D. Offices' clearances (parallel track)
- Each office (Fire, Assessor, Engineering, MENRO, MAO, MPDO, RHU, PESO, Barangay, BPLO) has **Request For Clearances** with Pending / Approved / Disapproved lists, Holdings view, uploaded files and Requirements.
- Action dialog: Approve or Disapprove with Remarks (and optional attachment). Stored as `<office>_action`, `<office>_remarks`, `<office>_trans_date`.
- **[verify]** Whether the live deployment requires all office clearances before BPLO approves, or only BPLO. Code shows office statuses are recorded, but payment gating is on BPLO only.

### Step E. BPLO approval
- BPLO → **Request For Clearances** → Pending list → open request.
- Request Details card sections: Business Information, PSIC Information, Arrears, Assessment Details, Requirements Per Assessment, Moderator Remarks; then Actions (Date, Current Status, Remarks).
- Choose **Approved** or **Disapproved** + Remarks → save. "Request approved successful".
- On approval the system recomputes local tax and current dues and saves them; `bplo_action = 1`. The request moves to **Assessed For Payment** (sworn status 20).
- Disapproved: stays in the Disapproved list. The evaluator can roll it back or fix and re-submit **[verify]**.
- A **Compliant Form** (remarks) exists for BPLO compliance but is now auto-filled on payment.

### Step F. Payment
- **At the cashier (OR path)**: Permit Evaluator → **Assessed For Payment** (columns: Date, Assessment Code, Business, Period, Quarter, Type, OR Number, OR Date, Action). Actions: Certificates, **Rollback request to BPLO**, **Enter OR number and date**.
- Dialog "Assign OR Number": OR number (required) and OR date → "Payment details successfully added."
- System writes `t_payment`, sets `fully_paid = Y`, `bplo_compliant = 1` ("Complaint automatically fillup"). The record appears under **Paid Assessment Request** and goes to **For MP Preparation**.
- **Online (applicant)**: Assessment Details → *Select payment options* → Paynamics (GCash/others), with success/failure redirect pages `/olapp/paynamics/redirects/success|failed`. Payment history under Payment History. **[verify]** whether online payment is enabled in this deployment (code has Paynamics and a commented-out PayMongo path).

### Step G. Permit Issuance: **For MP Preparation**
- Page *For Assessment* → tab **For MP Preparation**. Columns include Date, Business, Period, Quarter, Type, OR Number, Paid Amount, Plate No., **MP Printed**, Action.
- **Assign Plate Number and License Number** (both required; duplicate plate numbers rejected with "Plate number already exists" and the business that owns it).
- Print/preview the Mayor's Permit (`/permit-issuance/assessment/request/permit/:assessment_code`). The print and release buttons stay disabled until a plate number exists.
- Rollback to for-payment is available.

### Step H. **Set MP for release** → tab **MP For Release**
- Click Set MP for release → "Permit successfully set for release." (`is_mayor_permit_printed = 1`). Applicant is notified that the permit is ready for pickup (applicant status label "MP For Pickup").

### Step I. Release to the applicant
- In **MP For Release** (columns: Date, Business, Period, Quarter, Type, Is Released, Receiver, Action): **Add Receivers Information** opens the **Received Form** (receiver's name required, release date, remarks required). Saved to `mp_for_release`.
- After saving, **Remarks And Prints** becomes available to print the release remarks. Applicant status label becomes "MP Released".
- Hint: "Rollback to MP For Release" exists to undo.

### Applicant-visible status labels (Assessment list)
In order of precedence: **MP Paid** (payment recorded) → **MP Released** (received_by set) → **MP For Pickup** (permit printed) → **For payment** (BPLO approved) → otherwise the request's text status. Each opens a remarks popover.

---

## 5. Other transaction types (different handling)

| Type | Code | Behavior |
|---|---|---|
| Quarterly / Semi-annual later installments | `qtrly_yearly = Q / S`, `qtr > 1` | On OR entry the system auto-sets BPLO and moderator actions and marks the permit printed. The permit receiver is copied from the first quarter's release record. Listed under **Semi-Annual/Quarter Transaction** tab. |
| Business Closure | `trans_type = C` | Same auto-handling. Listed under **Closure Transaction** tab. |
| Transfer | `T` | Selectable transaction type. **[verify]** exact rules. |
| Years in arrears | | "Years Arrears" field on the sworn form; Arrears table in the BPLO view. |

Automatic notifications (cron, 9:00 AM): Apr 20 (Q2), Sep 20 (Q3), Oct 20 (Q4 and 2nd semi-annual) remind quarterly/semi-annual payers to renew.

---

## 6. Rollback tools (Moderator / Permit Evaluator)

- **Rollback Assessment** page lists assessments; options:
  - Rollback to **BPLO** (clears moderator/BPLO actions).
  - Rollback to **For Payment**.
  - Rollback to **MP For Preparation**.
  - Rollback to **new request** (deletes sworn, fees, headers, payments, release record; resets to Pending). Destructive; every one is written to the assessment log.
- Assessment log: `req_for_assessment_logs` ("AssessmentLogs" view).

---

## 7. Setup / reference data (Moderator, BPLO, Admin)

- **Moderator** (References): Business Type, Business Category, Barangay, Office (new / edit / details).
- **Fees Account**: fee accounts and amounts. **Fees Template**: fees auto-applied by business category (new business / renewal / installment).
- **Requirements Lists**: checklist items per office; `checklist_per_role` has an `is_default` flag, and `checklist_per_assessment` is a new table (see the build notes).
- **Admin**: Users Administration (create user, assign role, reset password), Requirements, Payments (Paynamics), Email (send message to all users), List of Business Transaction, OLAPP content (Services with steps/fees/forms, Requirements Group/List, Announcements).
- **Inquiries / Chat**: applicant ↔ office messaging per assessment (`/inquiry`, Chat).
- **Notifications**: bell for applicants; staff get action-based notices.

---

## 8. Proposed manual structure

1. Introduction (purpose, audience, system access, roles, glossary, status legend)
2. Getting started (register, verify, login, recover password, account settings)
3. Applicant guide (register business, request assessment, requirements, track status, pay, claim permit, payment history, inquiries)
4. Permit Evaluator guide (New Request, For Assessment and fees, Assessed For Payment / OR, Paid, Rollback)
5. BPLO guide (clearances queue, approve/disapprove, compliant, fees)
6. Permit Issuance guide (MP preparation, plate/license, print, release, quarterly and closure tabs)
7. Clearance Offices guide (Fire, Assessor, Engineering, MENRO, MAO, MPDO, RHU, PESO, Barangay)
8. Moderator guide (business registration, references, fees, rollbacks)
9. Admin guide (users, requirements, OLAPP, payments, email)
10. Reports guide (six reports)
11. Troubleshooting / FAQ, appendices (status codes, error messages)

## 9. Open questions to confirm on the live site
1. Is the applicant (`user`) portal live, or do staff encode everything? Is online payment (Paynamics) enabled?
2. Do all offices have to approve before BPLO, or is BPLO the only gate?
3. What does BPLO "Disapproved" lead to in practice?
4. Is `affiliate` (QR scanner) in use?
5. Which modules are out of scope (Calendar, Kanban, Mail, Projects are template leftovers from the Devias kit and look unused)?
6. Naming: code says "Moderator" and "Permit Evaluator"; the last commit renamed a "BPLO" label to "Assessment". Confirm the official role names for the manual.
