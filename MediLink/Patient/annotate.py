from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, os, re
R = json.load(open('../raw/pat-rects.json'))
O = 'fig'; os.makedirs(O, exist_ok=True)
FB = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
RED = (214, 40, 40); BLUE = (31, 90, 200)
PII = re.compile(r"Clarissa|clarissa|Reyes|David|Juancho|Cruz|0974655|0912|May 12, 0002|Secosana|Bulihan|Manila|Guitterez|Hans|Maria|Santos|Ronquillo|Alejandro|Pagtalunan|Allan|Agdao|Davao|Cristo|Malolos|Bago|Gallera|Evangelical|Single")

def load(n): return Image.open(f'../raw/pat-{n}.jpg').convert('RGB')

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
F('01-profile', 'f-layout', [(1, 2, 2, 1436, 60), (2, 4, 70, 248, 160), (3, 12, 230, 231, 470), (4, 1280, 12, 140, 40), (5, 262, 70, 1172, 690)])
F('50-user-menu', 'f-usermenu', [(1, 1280, 12, 140, 40), (2, 1224, 56, 200, 36), (3, 1224, 92, 200, 36)], crop=(840, 0, 600, 300))
F('01-profile', 'f-profile', [(1, 1311, 85, 108, 40), (2, 277, 133, 1142, 496), (3, 277, 655, 1142, 85)], crop=(256, 64, 1184, 700))
F('02-profile-update', 'f-profileupdate', [(1, 277, 101, 1142, 560), (2, 1223, 714, 196, 45)], crop=(256, 64, 1184, 720))
F('11-vitals-update', 'f-vitalsupdate', [(1, 277, 117, 1142, 224), (2, 1188, 349, 231, 45)], crop=(256, 64, 1184, 360))
F('10b-bmi', 'f-bmi', [(1, 1311, 85, 108, 40), (2, 277, 149, 1142, 224), (3, 277, 470, 563, 70), (4, 277, 547, 563, 144), (5, 277, 699, 563, 50), (6, 856, 463, 563, 289)], crop=(256, 64, 1184, 720))
F('12-allergies', 'f-allergies', [(1, 268, 76, 1160, 108)], crop=(256, 64, 1184, 160))
F('14-diagnosis-open', 'f-diagnosis', [(1, 277, 127, 56, 56)], crop=(256, 64, 1184, 220))
F('15-medication', 'f-medication', [(1, 268, 76, 1160, 136)], crop=(256, 64, 1184, 190))
F('16-diet', 'f-diet', [(1, 268, 76, 572, 100), (2, 856, 76, 572, 126), (3, 1334, 85, 85, 40)], crop=(256, 64, 1184, 190))
F('17-diet-add', 'f-dietadd', [(1, 510, 348, 420, 64), (2, 510, 420, 420, 104), (3, 840, 549, 90, 50)], crop=(460, 260, 520, 380))
F('18-family', 'f-family', [(1, 1334, 85, 85, 40), (2, 268, 120, 1160, 56)], crop=(256, 64, 1184, 170))
F('19-family-add', 'f-familyadd', [(1, 432, 304, 284, 64), (2, 724, 304, 284, 64), (3, 432, 376, 576, 64), (4, 432, 448, 284, 64), (5, 724, 448, 284, 64), (6, 432, 520, 284, 64), (7, 724, 520, 284, 64), (8, 918, 592, 90, 50)], crop=(390, 220, 660, 460))
F('20-laboratory', 'f-lab', [(1, 1334, 85, 85, 40), (2, 268, 128, 1160, 150), (3, 277, 134, 56, 56)], crop=(256, 64, 1184, 300))
F('21-lab-add', 'f-labadd', [(1, 851, 92, 577, 56), (2, 851, 160, 577, 200), (3, 851, 372, 577, 50)], crop=(820, 0, 620, 460))
F('22-imaging', 'f-imaging', [], crop=(256, 64, 1184, 470))
F('30-clinic-list', 'f-clinics', [(1, 276, 138, 216, 64), (2, 268, 205, 278, 115)], crop=(256, 64, 600, 300))
F('31-clinic-info', 'f-clinicinfo', [(1, 276, 147, 216, 64), (2, 562, 120, 866, 260), (3, 574, 400, 440, 150), (4, 1046, 444, 308, 158), (5, 570, 610, 860, 152), (6, 1361, 84, 59, 58)], crop=(256, 64, 1184, 740))
F('40-permissions', 'f-permissions', [(1, 1184, 85, 189, 48), (2, 277, 141, 1142, 123)], crop=(256, 64, 1184, 240))
F('60-health-graph', 'f-healthgraph', [(1, 264, 72, 279, 344), (2, 447, 375, 92, 39), (3, 854, 72, 279, 405)], crop=(0, 0, 1440, 1240))
F('61-graph-details', 'f-graphdetails', [(1, 276, 84, 1164, 600)], crop=(256, 64, 1184, 640))
F('51-account', 'f-account', [(1, 276, 160, 488, 56), (2, 276, 233, 371, 261), (3, 663, 233, 757, 396), (4, 1257, 568, 147, 45)], crop=(256, 64, 1184, 600))
F('52-account-email', 'f-email', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1259, 392, 145, 45)], crop=(256, 140, 1184, 330))
F('53-account-security', 'f-security', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1225, 392, 179, 45)], crop=(256, 140, 1184, 330))
print(len(os.listdir(O)))
