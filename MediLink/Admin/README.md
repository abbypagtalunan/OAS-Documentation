# MediLink Admin User Manual — sources

Builds `../MediLink-Admin-User-Manual.pdf` (A4 portrait, 21 pages, 5 sections and a quick-reference appendix).

> All clinics, pharmacies, doctors, staff and contact details shown are **sample data only**.

## Contents
1. Getting Started — signing in, the Admin screen, account menu
2. Clinics — adding, details, editing, assigning doctors, Secretary/Laboratory/Imaging accounts
3. Pharmacy — adding, details, Admin/Assistant/Pharmacist accounts
4. Doctors — adding, details, editing, specializations
5. Account Settings
- Appendix A — Quick Reference

Screenshots are in `../raw/adm-*.jpg` with element positions in `../raw/adm-rects.json`.

## Rebuilding
```bash
python3 annotate.py
cat head.py content.py tail.py > build.py
python3 build.py && python3 pages.py && python3 build.py
```

## Items to confirm (24 October 2026)
- Nothing was created or saved during capture; CREATE, SAVE and UPDATE results were not observed.
- Staff forms show "Invalid Date Format" under Birth Date before anything is typed.
- GET DIRECTION and LOCATION (map) were not tested.
- The Edit Doctor save button was below the captured area.
