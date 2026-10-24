from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, os, re
R = json.load(open('../raw/sec-rects.json'))
O = 'fig'; os.makedirs(O, exist_ok=True)
FB = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
RED = (214, 40, 40); BLUE = (31, 90, 200)
PII = re.compile(r"Clarissa|clarissa|Reyes|David|Juancho|Cruz|0974655|0912|May 12, 0002|Secosana|Bulihan|Manila|Guitterez|Hans|Maria|Santos|Ronquillo|Alejandro|Pagtalunan|Allan|Agdao|Davao|Cristo|Malolos|Bago|Gallera|Evangelical|Single")

def load(n): return Image.open(f'../raw/sec-{n}.jpg').convert('RGB')

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
        elif w < 120: cx = X + w * s; cy = max(r + 2, Y)
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


# ---------------- Secretary figures ----------------
F = lambda src, name, bx, crop=None: fig(src, None, name, bx, crop=crop)
# 1 layout
F('01-appointment', 'f-layout', [(1, 2, 2, 1436, 60), (2, 4, 70, 248, 160), (3, 12, 230, 231, 236), (4, 1313, 12, 107, 40), (5, 262, 70, 1172, 770)])
F('50-user-menu', 'f-usermenu', [(1, 1313, 12, 107, 40), (2, 1224, 56, 200, 36), (3, 1224, 92, 200, 36)], crop=(840, 0, 600, 300))
# 2 appointments
F('01-appointment', 'f-appt', [(1, 276, 147, 314, 48), (2, 276, 195, 360, 244)], crop=(256, 64, 1184, 420))
F('02-appt-details', 'f-apptdetails', [(1, 668, 120, 752, 360), (2, 981, 488, 228, 40), (3, 1216, 488, 204, 39), (4, 1325, 84, 95, 39)], crop=(256, 64, 1184, 500))
F('03-reschedule', 'f-reschedule', [(1, 510, 365, 420, 64), (2, 510, 468, 420, 64), (3, 840, 548, 90, 50)], crop=(460, 260, 520, 380))
F('04-appt-search', 'f-apptsearch', [(1, 276, 147, 314, 48), (2, 276, 195, 360, 150)], crop=(256, 64, 420, 340))
# 3 patient list (1340 tall)
F('10-patient-list', 'f-patients', [(1, 276, 138, 314, 48), (2, 276, 186, 360, 528), (3, 652, 68, 784, 803), (4, 1328, 797, 92, 50)], crop=(256, 64, 1184, 820))
F('11-patient-details', 'f-patientdetails', [(1, 652, 68, 784, 302), (2, 652, 378, 784, 80), (3, 652, 466, 784, 290), (4, 1267, 482, 153, 40), (5, 1325, 84, 95, 39)], crop=(256, 64, 1184, 700))
F('17-new-appointment', 'f-newappt', [(1, 510, 260, 420, 64), (2, 510, 340, 420, 64), (3, 510, 420, 420, 64), (4, 510, 500, 420, 64), (5, 510, 580, 420, 64), (6, 840, 652, 90, 50)], crop=(460, 160, 520, 580))
F('18-new-appointment-doctor', 'f-newappt2', [(1, 510, 500, 420, 64), (2, 510, 580, 420, 64)], crop=(460, 160, 520, 580))
F('12-profiles', 'f-profiles', [(1, 1332, 483, 87, 40), (2, 664, 527, 754, 400), (3, 664, 940, 754, 330)], crop=(640, 360, 800, 940))
F('12b-profiles-edit', 'f-profilesedit', [(1, 1192, 1246, 227, 45)], crop=(640, 360, 800, 940))
F('13-laboratory', 'f-lab', [(1, 1326, 475, 85, 40), (2, 664, 515, 760, 150), (3, 677, 523, 56, 58)], crop=(640, 360, 800, 400))
F('14-imaging', 'f-imaging', [], crop=(640, 360, 800, 540))
F('15-lab-add', 'f-labadd', [(1, 851, 92, 577, 56), (2, 851, 160, 577, 200), (3, 851, 372, 577, 50)], crop=(820, 0, 620, 460))
# 4 billing
F('20-billing', 'f-billing', [(1, 276, 147, 314, 48), (2, 276, 195, 360, 244)], crop=(256, 64, 420, 420))
F('21-billing-patient', 'f-bill', [(1, 668, 184, 752, 442), (2, 1297, 257, 56, 56), (3, 1190, 626, 114, 40), (4, 1305, 626, 115, 40)], crop=(640, 64, 800, 640))
F('22-bill-edit-amount', 'f-editamount', [(1, 549, 376, 342, 64), (2, 549, 448, 342, 64), (3, 801, 520, 90, 50)], crop=(500, 290, 440, 330))
F('23b-new-bill-service', 'f-newbill-service', [(1, 510, 376, 420, 64), (2, 510, 448, 420, 64), (3, 840, 520, 90, 50)], crop=(460, 290, 520, 330))
F('23c-new-bill-others', 'f-newbill-others', [(1, 510, 340, 420, 64), (2, 510, 412, 420, 64), (3, 510, 484, 420, 64), (4, 840, 556, 90, 50)], crop=(460, 255, 520, 400))
F('24-payment', 'f-payment', [(1, 578, 376, 284, 64), (2, 578, 448, 284, 64), (3, 772, 520, 90, 50)], crop=(530, 290, 380, 330))
# 5 reports
F('30-reports', 'f-reports', [(1, 1072, 84, 189, 48), (2, 1307, 84, 113, 45), (3, 276, 140, 1144, 525), (4, 1316, 214, 56, 56)], crop=(256, 64, 1184, 640))
F('31-reports-filter', 'f-filter', [(1, 510, 382, 406, 64), (2, 510, 454, 406, 64), (3, 821, 526, 109, 45)], crop=(460, 300, 520, 300))
F('32-receipt', 'f-receipt', [(1, 8, 8, 1424, 222), (2, 8, 252, 1424, 330), (3, 1188, 598, 112, 45), (4, 1302, 598, 110, 45)], crop=(0, 0, 1440, 680))
# 6 follow up
F('40-follow-up', 'f-followup', [(1, 1070, 92, 189, 48), (2, 1305, 92, 115, 48), (3, 276, 155, 1144, 310), (4, 1323, 229, 56, 56)], crop=(256, 64, 1184, 440))
F('41-follow-up-done', 'f-followupdone', [(1, 1305, 92, 115, 48), (2, 276, 155, 1144, 380)], crop=(256, 64, 1184, 520))
# 7 account
F('51-account', 'f-account', [(1, 276, 160, 488, 56), (2, 276, 233, 371, 261), (3, 663, 233, 757, 396), (4, 1257, 568, 147, 45)], crop=(256, 64, 1184, 600))
F('52-account-email', 'f-email', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1259, 392, 145, 45)], crop=(256, 140, 1184, 330))
F('53-account-security', 'f-security', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1225, 392, 179, 45)], crop=(256, 140, 1184, 330))
print(len(os.listdir(O)))
