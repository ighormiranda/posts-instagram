"""Gera capas 1080x1350 no padrão visual do @o.ighormiranda.
Uso: python3 capa.py specs.json saida_dir
Spec: {"out": nome, "layout": "claro"|"escuro", "fundo": "branco"|"verde"|"lima" (claro),
       "foto": caminho, "zoom": 1.0, "ox": 0, "oy": 0, "chapeu": "...",
       "titulo": [["texto", "base"|"dest"], ...], "sub": "...", "pag": "01/07", "tam": 70}
"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

import os
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts') + '/'
W, H = 1080, 1350
M = 90
BRANCO, PRETO = (254, 254, 254), (4, 4, 4)
VERDE, LIMA = (30, 130, 42), (154, 224, 76)


def font(n, s):
    return ImageFont.truetype(F + n + '.ttf', s)


def foto_layer(spec, area_h):
    im = ImageOps.exif_transpose(Image.open(spec['foto'])).convert('RGB')
    z = spec.get('zoom', 1.0)
    w = int(W * z)
    h = int(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    x = (W - w) // 2 + spec.get('ox', 0)
    y = spec.get('oy', 0)
    canvas = Image.new('RGB', (W, area_h), PRETO)
    canvas.paste(im, (x, y))
    return canvas


def grad_mask(h, start, end, inverse=False):
    """alpha 0 até start, sobe até 255 em end."""
    m = Image.new('L', (1, h))
    for yy in range(h):
        if yy <= start: a = 0
        elif yy >= end: a = 255
        else: a = int(255 * ((yy - start) / (end - start)) ** 1.2)
        m.putpixel((0, yy), 255 - a if inverse else a)
    return m.resize((W, h))


TR = -1.6
PUNCT = '.,?!:;'


def word_w(d, w, fnt):
    n = len(w); k = fnt.size / 70
    extra = TR * k * (n - 1) - sum(7 * k for c in w[1:] if c in PUNCT)
    return d.textlength(w, font=fnt) + extra


def draw_word(d, x, y, w, fnt, fill):
    off = 0.0; k = fnt.size / 70
    for i, c in enumerate(w):
        if i > 0 and c in PUNCT: off -= 7 * k
        px = x + d.textlength(w[:i], font=fnt) + TR * k * i + off if i else x
        d.text((px, y), c, font=fnt, fill=fill)


def layout_lines(segs, fnt, maxw, d):
    words = []
    for txt, kind in segs:
        for i, part in enumerate(txt.split('\n')):
            if i > 0: words.append(('\n', kind))
            for w in part.split(' '):
                if w: words.append((w, kind))
    lines, cur, curw = [], [], 0
    sp = d.textlength(' ', font=fnt)
    for w, k in words:
        if w == '\n':
            lines.append(cur); cur, curw = [], 0; continue
        ww = word_w(d, w, fnt)
        add = ww + (sp if cur else 0)
        if cur and curw + add > maxw:
            lines.append(cur); cur, curw = [(w, k)], ww
        else:
            cur.append((w, k)); curw += add
    if cur: lines.append(cur)
    return lines, sp


def draw_title(d, segs, x, y, fnt, maxw, cores, lh):
    lines, sp = layout_lines(segs, fnt, maxw, d)
    for ln in lines:
        cx = x
        for w, k in ln:
            draw_word(d, cx, y, w, fnt, cores[k])
            cx += word_w(d, w, fnt) + sp
        y += lh
    return y


def text_block_height(d, spec, fnt, maxw, lh, subf):
    lines, _ = layout_lines(spec['titulo'], fnt, maxw, d)
    h = 26 + 34 + len(lines) * lh
    if spec.get('sub'):
        sl, _ = layout_lines([(spec['sub'], 'base')], subf, maxw, d)
        h += 22 + len(sl) * 46
    return h


def tracked(d, xy, txt, fnt, fill, tr=5):
    x, y = xy
    for ch in txt:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tr


def render(spec, outdir):
    tam = spec.get('tam', 70)
    tf = font('pjs800', tam)
    lh = int(tam * 1.1)
    subf = font('pjs500', 34)
    mono = font('mono500', 24)
    maxw = spec.get('maxw', 880)
    img = Image.new('RGB', (W, H), BRANCO)
    d = ImageDraw.Draw(img)

    if spec['layout'] == 'claro':
        fundo = {'branco': BRANCO, 'verde': VERDE, 'lima': LIMA}[spec.get('fundo', 'branco')]
        img.paste(fundo, (0, 0, W, H))
        top = spec.get('foto_y', 560)
        layer = foto_layer(spec, H - top)
        # funde a foto no fundo
        base = Image.new('RGB', (W, H - top), fundo)
        mask = grad_mask(H - top, 0, spec.get('fade', 230))
        img.paste(Image.composite(layer, base, mask), (0, top))
        # escurece rodapé pra ler o @
        dark = Image.new('RGB', (W, H), PRETO)
        img = Image.composite(dark, img, grad_mask(H, 1020, 1350).point(lambda a: int(a * 0.55)))
        d = ImageDraw.Draw(img)
        if fundo == BRANCO:
            cores = {'base': PRETO, 'dest': VERDE}; ch = VERDE; subc = (60, 60, 60)
        elif fundo == VERDE:
            cores = {'base': BRANCO, 'dest': LIMA}; ch = LIMA; subc = (230, 245, 230)
        else:
            cores = {'base': PRETO, 'dest': (20, 90, 30)}; ch = (20, 90, 30); subc = (30, 40, 30)
        y = spec.get('texto_y', 170)
        tracked(d, (M, y), spec['chapeu'].upper(), mono, ch)
        y += 26 + 34
        y = draw_title(d, spec['titulo'], M, y, tf, maxw, cores, lh)
        if spec.get('sub'):
            y += 22
            draw_title(d, [(spec['sub'], 'base')], M, y, subf, maxw, {'base': subc}, 46)
    else:
        img.paste(foto_layer(spec, H), (0, 0))
        dark = Image.new('RGB', (W, H), PRETO)
        hb = text_block_height(d, spec, tf, maxw, lh, subf)
        ytxt = 1130 - hb
        g0 = spec.get('grad', ytxt - 300)
        img = Image.composite(dark, img, grad_mask(H, g0, ytxt + 60))
        d = ImageDraw.Draw(img)
        cores = {'base': BRANCO, 'dest': LIMA}
        y = ytxt
        tracked(d, (M, y), spec['chapeu'].upper(), mono, LIMA)
        y += 26 + 34
        y = draw_title(d, spec['titulo'], M, y, tf, maxw, cores, lh)
        if spec.get('sub'):
            y += 22
            draw_title(d, [(spec['sub'], 'base')], M, y, subf, maxw, {'base': (200, 200, 200)}, 46)

    # espaçamento das letras do chapéu: redesenha com tracking
    foot = font('mono500', 22)
    d.text((M, 1170), '@o.ighormiranda', font=foot, fill=BRANCO)
    pw = d.textlength(spec['pag'], font=foot)
    d.text((W - M - pw, 1170), spec['pag'], font=foot, fill=BRANCO)
    os.makedirs(outdir, exist_ok=True)
    p = os.path.join(outdir, spec['out'])
    img.save(p, quality=90)
    return p


if __name__ == '__main__':
    specs = json.load(open(sys.argv[1]))
    only = sys.argv[3:] if len(sys.argv) > 3 else None
    for s in specs:
        if only and s['out'] not in only: continue
        print(render(s, sys.argv[2]))
