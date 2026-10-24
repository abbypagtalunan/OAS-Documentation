# MediLink Doctor User Manual

User manual for the **Doctor** role of MediLink, the Integrated Healthcare System of the Municipality of Oas, Albay (`medilink.oas.lguapp.com`). Prepared by iConcept IT Solutions.

**[MediLink-Doctor-User-Manual.pdf](MediLink-Doctor-User-Manual.pdf)** — A4 portrait, 38 pages, 9 sections and a quick-reference appendix.

> All patients, doctors, appointments, results, prices and pharmacies shown are **sample data only**.

## Contents

1. Getting Started — signing in, the Doctor screen, account menu
2. Appointments — Month, Week, Day and Agenda views; appointment details
3. Patient List — searching, the patient record page
4. Appointments, Information and Health Record — completing an appointment, Pre-Lab, Medication, Allergies, Diagnosis, Diet, Pain and Vitals Monitoring
5. Notes, Treatment Plan and Prescriptions
6. Laboratory and Imaging — results, test requests, attachments
7. Services
8. Reports
9. Account Settings
- Appendix A — Quick Reference

## Folder layout

| Path | What it is |
|---|---|
| `MediLink-Doctor-User-Manual.pdf` | The finished manual |
| `raw/` | Screenshots captured from the live system at 2x (2880 px wide), plus `ml-rects.json` with element positions |
| `fig/` | Annotated figures (red numbered boxes) used in the manual |
| `home.png` | MediLink home page screenshot |
| `annotate.py` | Draws the red boxes on `raw/` screenshots and writes `fig/` |
| `content.py` | The manual text: sections, steps, tables, notes |
| `head.py`, `tail.py` | Page helpers, cover and table of contents |
| `style.css` | A4 page layout and styling |
| `build.py` | `head.py` + `content.py` + `tail.py`, renders `manual.html` to PDF with Chromium |
| `pages.py` | Reads the PDF outline to fill in page numbers in the table of contents |

## Rebuilding

Requires Python 3 with Pillow, pypdf and Playwright (Chromium).

```bash
python3 annotate.py                          # redraw figures
cat head.py content.py tail.py > build.py    # after editing the text
python3 build.py && python3 pages.py && python3 build.py   # second pass fills ToC page numbers
```

## Known items to confirm (as of 24 October 2026)

- What happens after **SET COMPLETE** on an appointment (not clicked during capture).
- How changes on the **Allergies** screen are saved (no Save button shown).
- The pain-rating step after clicking the body chart in **Pain Monitoring** (not captured).
- Account › General › **State** list shows Alabama, New York, San Francisco and Philippines.
