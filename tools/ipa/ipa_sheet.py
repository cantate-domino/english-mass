"""python tools/ipa/ipa_sheet.py sheets/<song>.png sheets/<song>-ipa.png spec_<name>  (needs pytesseract + tesseract)
ipa_sheet.py SRC OUT SPEC_MODULE — writes Oxford (BrE) IPA + linking marks under each lyric line.
SPEC: LINES=[(y_approx, "hyphen-ated lyric text"), ...]; IPA from oxford.py OX dict (strong forms)."""
import sys, re, importlib, difflib, pytesseract
from PIL import Image, ImageDraw, ImageFont
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specs'))
from oxford import OX, SKIP
src, out, mod = sys.argv[1:4]
S = importlib.import_module(mod)
im = Image.open(src).convert('RGB'); W, H = im.size
norm = lambda s: re.sub(r"[^a-z']", '', s.lower().replace('’', "'"))
VOW = 'aeiouæɑɒɔəɜʊʌɪ'
def ends_cons(ipa):
    if ipa.endswith('(r)'): return True
    c = ipa.rstrip('ː')[-1]
    return c not in VOW
def starts_vowel(ipa):
    s = ipa.lstrip('ˈˌ')
    return s[0] in VOW + 'eɛ'

def band_tokens(y):
    y0, y1 = max(0, y - 18), min(H, y + 40)
    b = im.crop((0, y0, W, y1)).convert('L'); b = b.resize((b.width * 3, b.height * 3), Image.LANCZOS)
    d = pytesseract.image_to_data(b, config='--psm 6', output_type=pytesseract.Output.DICT)
    toks = []
    for i, t in enumerate(d['text']):
        t = t.strip(); t = re.sub(r'^(\d)\.[05]0?$', lambda m: m.group(1) + '.O', t) if re.match(r'^\d\.0$', t) else re.sub(r'^(\d)\.50$', r'\1.So', t)
        if not t or float(d['conf'][i]) < 0: continue
        x, w, top, h = d['left'][i] / 3, d['width'][i] / 3, d['top'][i] / 3 + y0, d['height'][i] / 3
        if abs(top - y) > 16: continue
        parts = [p for p in t.split('-')]
        n = sum(max(1, len(p)) for p in parts); cx = x
        for p in parts:
            pw = w * max(1, len(p)) / n
            if norm(p): toks.append(dict(x0=cx, x1=cx + pw, t=norm(p), top=top, bot=top + h))
            cx += pw
    return sorted(toks, key=lambda t: t['x0'])

def align(syl, toks):
    n, m = len(syl), len(toks); NEG = -1e9
    best = [[NEG] * (m + 1) for _ in range(n + 1)]; back = {}
    best[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            v = best[i][j]
            if v == NEG: continue
            for (ni, nj, sc, mv) in [(i + 1, j, 0, None), (i, j + 1, 0, None)] + [
                (i + k, j + 1, None, k) for k in (1, 2, 3) if i + k <= n and j < m]:
                if mv:
                    cat = ''.join(syl[i:i + mv]); r = difflib.SequenceMatcher(None, cat, toks[j]['t']).ratio()
                    if r < 0.6: continue
                    sc = r * len(cat)
                if ni <= n and nj <= m and v + sc > best[ni][nj]:
                    best[ni][nj] = v + sc; back[(ni, nj)] = (i, j, mv)
    pos = [None] * n; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, mv = back[(i, j)]
        if mv:
            t = toks[pj]; L = sum(len(s) for s in syl[pi:pi + mv]); cx = t['x0']
            for k in range(pi, pi + mv):
                w = (t['x1'] - t['x0']) * len(syl[k]) / L; pos[k] = (cx, cx + w); cx += w
        i, j = pi, pj
    return pos

G = 22
def vline(gl, x, r, k=7):
    return all(gl.getpixel((x, min(H - 1, max(0, rr)))) < 140 for rr in range(r - k, r + k + 1))
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
FL = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
RED, BLUE = (160, 30, 40), (30, 80, 160)
plan = []
for y, text in S.LINES:
    words = []  # (display, syllables, punct_after)
    for w in text.split():
        syls = [norm(s) for s in w.split('-') if norm(s)]
        if not syls: continue
        words.append((w, syls, bool(re.search(r'[,.;:!?)]$', w))))
    flat = [s for _, ss, _ in words for s in ss]
    toks = band_tokens(y)
    pos = align(flat, toks)
    known = [k for k, p in enumerate(pos) if p]
    if not known: print('!! no match', y, text); continue
    for k, p in enumerate(pos):
        if p: continue
        l = max([q for q in known if q < k], default=None); r = min([q for q in known if q > k], default=None)
        if l is not None and r is not None:
            f = (k - l) / (r - l); x = pos[l][1] + (pos[r][0] - pos[l][1]) * f; pos[k] = (x - 10, x + 10)
        elif l is not None: x = pos[l][1] + 30 * (k - l); pos[k] = (x - 10, x + 10)
        else: x = pos[r][0] - 30 * (r - k); pos[k] = (x - 10, x + 10)
    spans = []; k = 0
    for w, ss, pa in words:
        ps = pos[k:k + len(ss)]; spans.append((min(p[0] for p in ps), max(p[1] for p in ps))); k += len(ss)
    bot = max(t['bot'] for t in toks if any(abs(t['x0'] - p[0]) < 1 for p in pos if p)) if toks else y + 24
    top = sorted(t['top'] for t in toks)[len(toks) // 2]
    gl = im.convert('L'); best = None
    for r in range(int(bot) - 1, int(bot) + 20):
        if r >= H: break
        dark = sum(1 for x in range(0, W, 1) if gl.getpixel((x, r)) < 245 and not vline(gl, x, r))
        if best is None or dark < best[0]: best = (dark, r)
    plan.append(dict(y=top, cut=best[1], words=words, spans=spans)); print('   bot', bot, 'cut', best)
    print(f'{y}->{top:.0f} matched {len(known)}/{len(flat)}  {text[:50]}')
plan.sort(key=lambda p: p['cut'])
new = Image.new('RGB', (W, H + G * len(plan)), 'white'); prev = 0; off = 0
for p in plan:
    new.paste(im.crop((0, prev, W, p['cut'])), (0, prev + off)); p['base'] = p['cut'] + off; prev = p['cut']; off += G
new.paste(im.crop((0, prev, W, H)), (0, prev + off))
# reconnect braces / barlines that crossed a cut
g = im.convert('L'); d = ImageDraw.Draw(new)
for p in plan:
    c = p['cut']
    for x in range(W):
        if c >= 1 and c < H and vline(g, x, c):
            d.line([(x, p['base']), (x, p['base'] + G - 1)], fill=(g.getpixel((x, c)),)*3)
missing = set()
for p in plan:
    ipas = []
    for w, ss, pa in p['words']:
        key = ''.join(ss)
        if key not in OX: missing.add(key); ipas.append(None); continue
        ipas.append(OX[key])
    for i,(w,ss,pa) in enumerate(p['words']):
        if ''.join(ss)=='the' and i+1<len(ipas) and ipas[i+1] and starts_vowel(ipas[i+1]): ipas[i]='ði'
    box = []
    for (w, ss, pa), (a, b), ipa in zip(p['words'], p['spans'], ipas):
        if ipa is None or ''.join(ss) in SKIP: box.append((a, b)); continue
        tw = d.textlength(ipa, font=F); x0 = (a + b) / 2 - tw / 2
        d.text((x0, p['base'] + 1), ipa, font=F, fill=RED); box.append((x0, x0 + tw))
    for i in range(len(p['words']) - 1):
        w, ss, pa = p['words'][i]
        if pa or ipas[i] is None or ipas[i + 1] is None: continue
        nxt = ''.join(p['words'][i + 1][1])
        a = ipas[i] if not (''.join(ss) == 'the') else 'ðə'
        if ends_cons(ipas[i]) and starts_vowel(ipas[i + 1]):
            x = (box[i][1] + box[i + 1][0]) / 2
            d.text((x - 7, p['base'] - 10), '‿', font=FL, fill=BLUE)
new.save(out, optimize=True)
print(out, new.size, 'MISSING:', sorted(missing))
