from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, os, re
R = json.load(open('../raw/lab-rects.json'))
O = 'fig'; os.makedirs(O, exist_ok=True)
FB = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
RED = (214, 40, 40); BLUE = (31, 90, 200)
PII = re.compile(r"Clarissa|clarissa|Reyes|David|Juancho|Cruz|0974655|0912|May 12, 0002|Secosana|Bulihan|Manila|Guitterez|Hans|Maria|Santos|Ronquillo|Alejandro|Pagtalunan|Allan|Agdao|Davao|Cristo|Malolos|Bago|Gallera|Evangelical|Single")

def load(n): return Image.open(f'../raw/lab-{n}.jpg').convert('RGB')

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
F('02-test', 'f-layout', [(1, 2, 2, 1436, 60), (2, 4, 70, 248, 160), (3, 12, 230, 231, 186), (4, 1341, 12, 79, 40), (5, 262, 70, 1172, 770)])
F('50-user-menu', 'f-usermenu', [(1, 1341, 12, 79, 40), (2, 1224, 56, 200, 36), (3, 1224, 92, 200, 36)], crop=(840, 0, 600, 300))
F('01-patients', 'f-patients', [(1, 316, 84, 266, 166), (2, 332, 154, 188, 64)], crop=(256, 64, 600, 260))
F('02-test', 'f-test', [(1, 1265, 84, 115, 40), (2, 316, 132, 1064, 191), (3, 1171, 205, 32, 38), (4, 1205, 205, 32, 38)], crop=(256, 64, 1184, 300))
F('03-newtest', 'f-newtest', [(1, 1031, 76, 397, 64), (2, 1031, 148, 397, 64), (3, 1031, 220, 397, 50), (4, 1372, 12, 56, 56)], crop=(980, 0, 460, 300))
F('04-edittest', 'f-edittest', [(1, 1031, 66, 397, 74), (2, 1031, 140, 397, 72), (3, 1031, 220, 397, 50)], crop=(980, 0, 460, 300))
F('05-values', 'f-values', [(1, 1205, 205, 32, 38), (2, 332, 384, 1032, 227), (3, 1124, 331, 132, 45), (4, 1256, 331, 108, 45), (5, 1200, 457, 56, 56)], crop=(256, 64, 1184, 590))
F('06-addvalue', 'f-addvalue', [(1, 1021, 76, 407, 64), (2, 1021, 148, 407, 64), (3, 1021, 220, 407, 50), (4, 1372, 12, 56, 56)], crop=(970, 0, 470, 300))
F('07-editvalue', 'f-editvalue', [(1, 1021, 66, 407, 74), (2, 1021, 140, 407, 72), (3, 1021, 220, 407, 50)], crop=(970, 0, 470, 300))
F('08-report', 'f-report', [(1, 316, 128, 1064, 374), (2, 1262, 201, 32, 38), (3, 330, 444, 1040, 50)], crop=(256, 64, 1184, 470))
F('09-result', 'f-result', [(1, 252, 112, 936, 322), (2, 1071, 442, 125, 45), (3, 252, 525, 936, 205)], crop=(240, 103, 960, 694))
F('10-resultprint', 'f-resultprint', [(1, 252, 225, 936, 400), (2, 1082, 637, 106, 45)], crop=(240, 207, 960, 486))
F('51-account', 'f-account', [(1, 276, 160, 488, 56), (2, 276, 233, 371, 261), (3, 663, 233, 757, 396), (4, 1257, 568, 147, 45)], crop=(256, 64, 1184, 600))
F('52-account-email', 'f-email', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1259, 392, 145, 45)], crop=(256, 140, 1184, 330))
F('53-account-security', 'f-security', [(1, 292, 303, 548, 64), (2, 856, 303, 548, 64), (3, 1225, 392, 179, 45)], crop=(256, 140, 1184, 330))
