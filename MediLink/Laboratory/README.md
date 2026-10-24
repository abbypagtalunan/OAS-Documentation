# MediLink Laboratory User Manual — sources

Builds `../MediLink-Laboratory-User-Manual.pdf` (A4 portrait, 15 pages, 5 sections and a quick-reference appendix).

> All names, tests, rates, results and normal values shown are **sample data only**.

## Contents
1. Getting Started — signing in, the Laboratory screen, account menu
2. Patients — the patient list
3. Laboratory Tests — tests and rates, test values and normal ranges
4. Report — transactions, viewing and printing results
5. Account Settings
- Appendix A — Quick Reference

Screenshots are in `../raw/lab-*.jpg` with element positions in `../raw/lab-rects.json`.

## Rebuilding
```bash
python3 annotate.py
cat head.py content.py tail.py > build.py
python3 build.py && python3 pages.py && python3 build.py
```

## Items to confirm (24 October 2026)
- The Patient List was empty (no pending laboratory request), so opening a patient and entering a result were not captured.
- Nothing was created or saved; PRINT was not clicked.
- Sample result shows "DIFFIRENTIAL COUNT", "NEUROPHIL" and a reversed range "215 - 177"; printable header is "SAMPLE COMPANY".
