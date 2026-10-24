from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, os, re
R = json.load(open('../raw/adm-rects.json'))
O = 'fig'; os.makedirs(O, exist_ok=True)
FB = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
RED = (214, 40, 40); BLUE = (31, 90, 200)
PII = re.compile(r"Clarissa|clarissa|Reyes|David|Juancho|Cruz|0974655|0912|May 12, 0002|Secosana|Bulihan|Manila|Guitterez|Hans|Maria|Santos|Ronquillo|Alejandro|Pagtalunan|Allan|Agdao|Davao|Cristo|Malolos|Bago|Gallera|Evangelical|Single")

def load(n): return Image.open(f'../raw/adm-{n}.jpg').convert('RGB')

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

def boxes(img, items, s=2, ox=0, oy=0, lw=9, r=40, minx=0, miny=0):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(FB, int(r * 1.15))
    for it in items:
        n, x, y, w, h = it[:5]; col = it[5] if len(it) > 5 else RED
        X = (x - ox) * s; Y = (y - oy) * s
        d.rounded_rectangle([X, Y, X + w * s, Y + h * s], radius=8, outline=col, width=lw)
        if n is None: continue
        if w < 70 and Y - 2 * r - 6 >= miny * s: cx = X + w * s / 2; cy = Y - r - 4
        elif w < 120: cx = X + w * s; cy = max(r + 2, Y)
        elif X - 2 * r - 8 >= minx * s: cx = X - r - 6; cy = Y + r
        else: cx = max(minx * s + r + 2, X); cy = max(miny * s + r + 2, Y)
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
    boxes(im, bx, minx=crop[0] if crop else 0, miny=crop[1] if crop else 0)
    save(im, name, crop)





F = lambda src, name, bx, crop=None: fig(src, None, name, bx, crop=crop)
F('01-clinics', 'f-layout', [(1, 2, 2, 1436, 60), (2, 4, 70, 248, 160), (3, 12, 230, 231, 140), (4, 1341, 12, 79, 40), (5, 262, 70, 1172, 800)], crop=(0, 0, 1440, 880))
F('50-user-menu', 'f-usermenu', [(1, 1341, 12, 79, 40), (2, 1224, 56, 200, 36), (3, 1224, 92, 200, 36)], crop=(840, 0, 600, 300))
# Clinics
F('01-clinics', 'f-addclinic', [(1, 276, 138, 216, 64), (2, 570, 138, 850, 56), (3, 570, 202, 850, 208), (4, 570, 418, 421, 366), (5, 999, 418, 421, 366), (6, 1311, 793, 109, 50)], crop=(256, 64, 1184, 800))
F('02-clinic-info', 'f-clinicinfo', [(1, 1302, 84, 59, 58), (2, 1361, 84, 59, 58), (3, 600, 440, 395, 98), (4, 1046, 444, 308, 158), (5, 1283, 610, 137, 40), (6, 1261, 777, 159, 40), (7, 1251, 944, 169, 40), (8, 1279, 1111, 141, 40)], crop=(256, 64, 1184, 1240))
F('03-clinic-edit', 'f-clinicedit', [(1, 862, 367, 138, 45), (2, 440, 428, 560, 208), (3, 436, 645, 568, 340), (4, 890, 994, 110, 50)], crop=(400, 330, 640, 730))
F('04-add-doctor', 'f-clinicdoctor', [(1, 623, 662, 194, 64), (2, 726, 734, 90, 50)], crop=(590, 580, 260, 240))
F('05-add-secretary', 'f-clinicstaff', [(1, 432, 410, 284, 352), (2, 724, 400, 284, 360), (3, 432, 793, 284, 64), (4, 432, 865, 576, 136), (5, 918, 1009, 90, 50)], crop=(400, 300, 640, 800))
# Pharmacy
F('10-pharmacy', 'f-addpharmacy', [(1, 276, 138, 216, 64), (2, 570, 202, 850, 208), (3, 570, 418, 421, 366), (4, 999, 418, 421, 366), (5, 1311, 793, 109, 50)], crop=(256, 64, 1184, 800))
F('11-pharmacy-info', 'f-pharmacyinfo', [(1, 1302, 84, 59, 58), (2, 600, 440, 395, 98), (3, 1292, 610, 128, 40), (4, 1264, 777, 156, 40), (5, 1250, 984, 170, 40)], crop=(256, 64, 1184, 1120))
F('13-add-admin', 'f-pharmacystaff', [(1, 432, 410, 284, 352), (2, 724, 400, 284, 360), (3, 432, 793, 284, 64), (4, 432, 865, 576, 136), (5, 918, 1009, 90, 50)], crop=(400, 300, 640, 800))
# Doctors
F('20-doctors', 'f-adddoctor', [(1, 276, 147, 216, 64), (2, 1260, 84, 160, 40), (3, 570, 171, 421, 784), (4, 999, 171, 421, 720), (5, 570, 963, 850, 136), (6, 1311, 1107, 109, 50)], crop=(256, 64, 1184, 1110))
F('21-doctor-info', 'f-doctorinfo', [(1, 1302, 84, 59, 58), (2, 1361, 84, 59, 58), (3, 600, 440, 800, 108)], crop=(256, 64, 1184, 620))
F('22-doctor-edit', 'f-doctoredit', [(1, 440, 93, 555, 784)], crop=(400, 20, 640, 1380))
F('30-specialization', 'f-spec', [(1, 570, 84, 89, 40), (2, 1230, 84, 190, 40), (3, 570, 149, 804, 64), (4, 1360, 213, 56, 56)], crop=(256, 64, 1184, 500))
F('31-add-spec', 'f-addspec', [(1, 619, 662, 203, 64), (2, 731, 734, 90, 50)], crop=(590, 580, 260, 240))
F('32-edit-spec', 'f-editspec', [(1, 510, 662, 420, 64), (2, 820, 734, 110, 50)], crop=(480, 580, 480, 240))
F('51-account', 'f-account', [(1, 276, 160, 488, 56), (2, 276, 233, 371, 261), (3, 663, 233, 757, 396), (4, 1257, 568, 147, 45)], crop=(256, 64, 1184, 600))
F('52-account-email', 'f-email', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1259, 392, 145, 45)], crop=(256, 140, 1184, 330))
F('53-account-security', 'f-security', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1225, 392, 179, 45)], crop=(256, 140, 1184, 330))
print(len(os.listdir(O)))
