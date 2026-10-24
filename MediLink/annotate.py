from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, os, re
R = json.load(open('raw/ml-rects.json'))
O = 'fig'; os.makedirs(O, exist_ok=True)
FB = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
RED = (214, 40, 40); BLUE = (31, 90, 200)
PII = re.compile(r"Clarissa|clarissa|Reyes|David|Juancho|Cruz|0974655|0912|May 12, 0002|Secosana|Bulihan|Manila|Guitterez|Hans|Maria|Santos|Ronquillo|Alejandro|Pagtalunan|Allan|Agdao|Davao|Cristo|Malolos|Bago|Gallera|Evangelical|Single")

def load(n): return Image.open(f'raw/ml-{n}.jpg').convert('RGB')

def pii_rects(key):
    out = []
    for e in R.get(key, []):
        if e['w'] <= 0 or e['h'] <= 0 or e['h'] > 70 or e['w'] > 760: continue
        if e['t'] in ('TABLE', 'TR', 'TBODY'): continue
        if PII.search(e['s']):
            out.append((e['x'], e['y'], e['w'], e['h']))
    return out

def blur(img, rects, s=2, pad=3):
    return img
    for x, y, w, h in rects:
        b = (max(0, int((x - pad) * s)), max(0, int((y - pad) * s)), min(img.width, int((x + w + pad) * s)), min(img.height, int((y + h + pad) * s)))
        if b[2] <= b[0] or b[3] <= b[1]: continue
        reg = img.crop(b).filter(ImageFilter.GaussianBlur(9 * s / 2))
        img.paste(reg, b)
    return img

def boxes(img, items, s=2, ox=0, oy=0, lw=9, r=40):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(FB, int(r * 1.15))
    for it in items:
        n, x, y, w, h = it[:5]; col = it[5] if len(it) > 5 else RED
        X = (x - ox) * s; Y = (y - oy) * s
        d.rounded_rectangle([X, Y, X + w * s, Y + h * s], radius=8, outline=col, width=lw)
        if n is None: continue
        if w < 70 and Y - 2 * r - 6 >= 0: cx = X + w * s / 2; cy = Y - r - 4
        elif X - 2 * r - 8 >= 0: cx = X - r - 6; cy = Y + r
        else: cx = max(r + 2, X); cy = max(r + 2, Y)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline='white', width=3)
        t = str(n); bb = d.textbbox((0, 0), t, font=f)
        d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]), t, fill='white', font=f)
    return img

def save(img, name, crop=None, s=2, maxw=2000):
    if crop:
        x, y, w, h = crop; img = img.crop((x * s, y * s, (x + w) * s, (y + h) * s))
    if img.width > maxw: img = img.resize((maxw, round(img.height * maxw / img.width)), Image.LANCZOS)
    img.save(f'{O}/{name}.jpg', quality=88)

def fig(src, key, name, bx, crop=None, extra_blur=(), keep=None):
    im = load(src)
    orig = im.copy()
    blur(im, pii_rects(key) + list(extra_blur))
    if keep:
        x, y, w, h = keep; b = (x * 2, y * 2, (x + w) * 2, (y + h) * 2); im.paste(orig.crop(b), b[:2])
    boxes(im, bx)
    save(im, name, crop)

SIDEBAR = pii_rects('04-patient-appointments')
side = [r for r in SIDEBAR if r[0] < 256 or r[1] < 64]

# 1 homepage (user's own screenshot, 1:1 px, crop browser bar)
home = Image.open('home.png').convert('RGB').crop((0, 66, 2940, 1912))
boxes(home, [(1, 2715, 30, 140, 66)], s=1, lw=9, r=40)
home = home.resize((2000, round(home.height * 2000 / home.width)), Image.LANCZOS)
home.save(f'{O}/f-home.jpg', quality=88)

# 1.3 layout (October month)
fig('01-calendar-month', None, 'f-layout', [(1, 2, 2, 1436, 60), (2, 4, 70, 248, 160), (3, 12, 230, 231, 186), (4, 1293, 12, 127, 40), (5, 262, 70, 1172, 770)], extra_blur=side)
# 1.4 user menu
fig('70-user-menu', '70-user-menu', 'f-usermenu', [(1, 1293, 12, 127, 40), (2, 1224, 56, 200, 36), (3, 1224, 92, 200, 36)], crop=(840, 0, 600, 300), extra_blur=side)

# 2.1 month view
ev2 = [(604, 521, 159, 26), (768, 521, 159, 26), (933, 521, 159, 26)]
fig('02-calendar-july', None, 'f-month', [(1, 268, 83, 176, 39), (2, 786, 84, 117, 36), (3, 1244, 76, 184, 52), (4, 600, 516, 496, 36)], extra_blur=side + [(x + 50, y + 2, w - 52, h - 4) for x, y, w, h in ev2])
# 2.2 views
fig('80-cal-week', '80-cal-week', 'f-week', [(1, 1288, 76, 52, 52), (2, 635, 374, 470, 200)], extra_blur=side)
fig('82b-cal-day', '82-cal-day', 'f-day', [(1, 1332, 76, 52, 52), (2, 322, 374, 1072, 57)], extra_blur=side)
fig('81-cal-agenda', '81-cal-agenda', 'f-agenda', [(1, 1376, 76, 52, 52), (2, 270, 122, 1156, 246)], extra_blur=side, crop=(0, 0, 1440, 520))
# 2.3 details drawer
fig('03-appt-details', None, 'f-apptdetails', [(1, 952, 84, 476, 322), (2, 1243, 409, 181, 45), (3, 1370, 18, 52, 52)], extra_blur=side + [(960, 109, 300, 24), (960, 174, 300, 24)] + [(x + 50, y + 2, w - 52, h - 4) for x, y, w, h in ev2])

# 3 patient list
fig('40-patient-list', '40-patient-list', 'f-patients', [(1, 1145, 92, 189, 48), (2, 332, 168, 1032, 373), (3, 1231, 245, 117, 45)], crop=(256, 64, 1184, 520))
fig('41-patient-search', '41-patient-search', 'f-patientsearch', [(1, 1145, 92, 189, 48), (2, 332, 168, 1032, 220)], crop=(256, 64, 1184, 360))
# 3.2 profile
fig('04-patient-appointments', '04-patient-appointments', 'f-profile', [(1, 316, 166, 1064, 168), (2, 1282, 92, 98, 45), (3, 316, 346, 1064, 56), (4, 316, 414, 1064, 308), (5, 1193, 487, 56, 56)])

# 4.1 next action
fig('33-appt-next-action', '33-appt-next-action', 'f-nextaction', [(1, 952, 84, 476, 190), (2, 957, 283, 466, 45)])
# 4.2 information
fig('05-patient-information', '05-patient-information', 'f-info', [(1, 316, 414, 1064, 240)], crop=(256, 64, 1184, 640))
# 4.3 health record
fig('25-hr-7-pre-lab', '25-hr-7-pre-lab', 'f-hr', [(1, 316, 414, 260, 424), (2, 584, 414, 796, 446), (3, 1282, 437, 78, 45)], crop=(256, 330, 1184, 560))
fig('24-hr-update', '24-hr-update', 'f-hrupdate', [(1, 952, 84, 476, 660), (2, 956, 757, 173, 45)], crop=(720, 0, 720, 900))
# 4.4 medication
fig('25-hr-1-medication', '25-hr-1-medication', 'f-med', [(1, 1214, 434, 146, 45), (2, 584, 414, 796, 268)], crop=(256, 330, 1184, 520))
fig('26-new-medication', '26-new-medication', 'f-mednew', [(1, 956, 84, 468, 80), (2, 956, 176, 468, 230), (3, 1035, 418, 72, 45)], crop=(720, 0, 720, 520))
# 4.5 allergies
fig('25-hr-2-allergies', '25-hr-2-allergies', 'f-allergy', [(1, 584, 414, 796, 177), (2, 725, 483, 234, 32)], crop=(256, 330, 1184, 520))
# 4.6 diagnosis
fig('25-hr-3-diagnosis', '25-hr-3-diagnosis', 'f-diag', [(1, 1225, 434, 135, 45), (2, 1055, 486, 56, 56), (3, 1103, 486, 56, 56), (4, 1151, 486, 56, 56)], crop=(256, 330, 1184, 520))
fig('26-new-diagnosis', '26-new-diagnosis', 'f-diagnew', [(1, 960, 84, 460, 150), (2, 960, 262, 460, 106), (3, 1035, 394, 72, 45)], crop=(720, 0, 720, 500))
# 4.7 diet
fig('26-new-diet', '26-new-diet', 'f-dietnew', [(1, 956, 84, 468, 80), (2, 956, 176, 468, 230), (3, 1035, 418, 72, 45)], crop=(720, 0, 720, 520))
# 4.8 pain (tall viewport 1320)
fig('29-pain-add', '29-pain-add', 'f-pain', [(1, 655, 502, 85, 40), (2, 359, 560, 360, 610), (3, 489, 1167, 102, 45), (4, 456, 1219, 168, 45), (5, 764, 486, 608, 204)], crop=(256, 400, 1184, 900))
# 4.9 vitals
fig('31-vitals', '31-vitals', 'f-vitals', [(1, 316, 478, 1059, 56), (2, 316, 546, 1059, 560)], crop=(256, 400, 1184, 760))

# 5.1 notes
fig('07-notes', '07-notes', 'f-notes', [(1, 1255, 434, 105, 45), (2, 336, 470, 1024, 248)], crop=(256, 330, 1184, 430))
fig('22-notes-new', '22-notes-new', 'f-notesnew', [(1, 956, 84, 468, 80), (2, 956, 176, 468, 230), (3, 1035, 418, 76, 45)], crop=(720, 0, 720, 520))
# 5.2 treatment plan
fig('09-treatment-plan', '09-treatment-plan', 'f-tp', [(1, 1176, 434, 184, 45), (2, 336, 470, 1024, 248)], crop=(256, 330, 1184, 430))
fig('23b-tp-new', '23-tp-new', 'f-tpnew', [(1, 956, 84, 468, 80), (2, 956, 176, 468, 230), (3, 1035, 418, 76, 45)], crop=(720, 0, 720, 520))
# 5.3 prescriptions
fig('08-prescriptions', '08-prescriptions', 'f-rx', [(1, 316, 414, 260, 232), (2, 584, 414, 796, 288)], crop=(256, 330, 1184, 420))
fig('19-rx-unsaved', '19-rx-unsaved', 'f-rxunsaved', [(1, 604, 434, 756, 248), (2, 604, 704, 139, 45), (3, 755, 704, 181, 45)], crop=(256, 330, 1184, 470))
fig('20-rx-addproduct', '20-rx-addproduct', 'f-rxadd', [(1, 552, 256, 336, 82), (2, 552, 347, 336, 64), (3, 552, 419, 336, 64), (4, 552, 492, 336, 130), (5, 552, 644, 336, 45)], crop=(470, 180, 470, 540), keep=(540, 199, 360, 502))
fig('21-rx-clinic-products', '21-rx-clinic-products', 'f-rxclinic', [(1, 604, 434, 756, 64), (2, 604, 802, 139, 45), (3, 755, 802, 181, 45)], crop=(256, 330, 1184, 560))

# 6 lab & imaging
fig('10-laboratory', '10-laboratory', 'f-lab', [(1, 316, 414, 260, 232), (2, 604, 434, 756, 308), (3, 1188, 507, 56, 56)], crop=(256, 330, 1184, 450))
fig('17-lab-result', '10-laboratory', 'f-labresult', [(1, 244, 108, 952, 330), (2, 1071, 442, 125, 45)], crop=(220, 90, 1000, 720), keep=(240, 104, 960, 693))
fig('12-imaging-result', None, 'f-imgresult', [(1, 1071, 533, 125, 45)], crop=(220, 285, 1000, 330))
fig('13-imaging-print', None, 'f-imgprint', [(1, 1082, 584, 106, 45)], crop=(220, 240, 1000, 420))
fig('14-imaging-unsaved', '14-imaging-unsaved', 'f-unsaved', [(1, 316, 502, 260, 52), (2, 604, 434, 756, 248), (3, 604, 704, 107, 45), (4, 723, 704, 134, 45)], crop=(256, 330, 1184, 450))
fig('16-imaging-addtest', '14-imaging-unsaved', 'f-addtest', [(1, 552, 412, 336, 64), (2, 552, 484, 336, 45)], crop=(470, 330, 470, 240), keep=(540, 360, 360, 181))
fig('15-imaging-attachments', '15-imaging-attachments', 'f-attach', [(1, 316, 550, 259, 52), (2, 591, 422, 776, 470)], crop=(256, 330, 1184, 580))

# 7 services
fig('50-services', '50-services', 'f-services', [(1, 1010, 90, 189, 48), (2, 1247, 92, 133, 45), (3, 1208, 226, 56, 56), (4, 1256, 226, 56, 56), (5, 1304, 226, 56, 56)], crop=(256, 64, 1184, 360))
fig('51-service-new', '51-service-new', 'f-servicenew', [(1, 956, 84, 468, 80), (2, 956, 176, 468, 80), (3, 1035, 270, 76, 45)], crop=(720, 0, 720, 340))
# 8 reports
fig('60-reports', '60-reports', 'f-reports', [(1, 1145, 84, 189, 48), (2, 316, 140, 1064, 383)], crop=(256, 64, 1184, 500))
# 9 account
fig('71-account', '71-account', 'f-account', [(1, 276, 160, 488, 56), (2, 276, 233, 371, 261), (3, 663, 233, 757, 396), (4, 1257, 568, 147, 45)], crop=(256, 64, 1184, 600))
fig('72b-account-email', '72-account-email', 'f-email', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1259, 392, 145, 45)], crop=(256, 140, 1184, 330))
fig('73b-account-security', '73-account-security', 'f-security', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1225, 392, 179, 45)], crop=(256, 140, 1184, 330))
print(len(os.listdir(O)))
