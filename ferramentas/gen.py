"""Gerador de carrosséis no padrão @o.ighormiranda.
Uso: python3 gen.py conteudo.json saida_dir [post_id ...]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont, ImageOps
import capa

F = capa.F
W, H, M = 1080, 1350, 90
BR, PR, VD, LM = (254, 254, 254), (4, 4, 4), (30, 130, 42), (154, 224, 76)
CINZA = (40, 40, 40)
FOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fotos') + '/'
fnt = lambda n, s: ImageFont.truetype(F + n + '.ttf', s)


def foot(d, n, tot, cor, right=W - M):
    f = fnt('mono500', 22)
    d.text((M, 1170), '@o.ighormiranda', font=f, fill=cor)
    p = f'{n:02d}/{tot:02d}'
    d.text((right - d.textlength(p, font=f), 1170), p, font=f, fill=cor)


def segs(x):
    """'texto *destaque* texto' -> [(t,'b'),(t,'d')]"""
    out, dest = [], False
    for i, part in enumerate(x.split('*')):
        if part: out.append((part, 'd' if dest else 'b'))
        dest = not dest
    return out


def rich(d, txt, x, y, size, cores, lh=None, maxw=900, peso='pjs800'):
    lh = lh or int(size * 1.13)
    return capa.draw_title(d, segs(txt), x, y, fnt(peso, size), maxw, cores, lh)


def s_capa(s, n, tot, out):
    if s.get('foto'):
        titulo = [[t, 'base' if k == 'b' else 'dest'] for t, k in segs(s['titulo'])]
        spec = {"out": os.path.basename(out), "layout": "escuro", "foto": FOT + s['foto'], "oy": s.get('oy', -20),
                "zoom": s.get('zoom', 1.0), "ox": s.get('ox', 0), "chapeu": s['chapeu'],
                "titulo": titulo, "pag": f'01/{tot:02d}', "tam": s.get('tam', 70)}
        if s.get('sub'): spec['sub'] = s['sub']
        return capa.render(spec, os.path.dirname(out) or '.')
    im = Image.new('RGB', (W, H), PR); d = ImageDraw.Draw(im)
    capa.tracked(d, (M, 470), s['chapeu'].upper(), fnt('mono500', 26), LM)
    y = rich(d, s['titulo'], M, 530, s.get('tam', 96), {'b': BR, 'd': LM})
    if s.get('sub'): rich(d, s['sub'], M, y + 30, 38, {'b': (200, 200, 200), 'd': LM}, 52, peso='pjs500')
    foot(d, 1, tot, BR); im.save(out, quality=90)


def s_texto(s, n, tot, out):
    escuro = s.get('fundo', 'escuro') == 'escuro'
    bg, base, dest, subc = (PR, BR, LM, (215, 215, 215)) if escuro else (BR, PR, VD, CINZA)
    im = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(im)
    y = 400
    if s.get('chapeu'):
        capa.tracked(d, (M, y - 60), s['chapeu'].upper(), fnt('mono500', 26), dest)
    y = rich(d, s['titulo'], M, y, 64, {'b': base, 'd': dest}, 72)
    if s.get('sub'): rich(d, s['sub'], M, y + 34, 38, {'b': subc, 'd': dest}, 52, peso='pjs500')
    foot(d, n, tot, base); im.save(out, quality=90)


def s_item(s, n, tot, out):
    im = Image.new('RGB', (W, H), BR); d = ImageDraw.Draw(im)
    capa.tracked(d, (M, 330), s['label'].upper(), fnt('mono500', 26), VD)
    d.text((M - 8, 370), f"{s['k']:02d}", font=fnt('pjs800', 260), fill=BR, stroke_width=5, stroke_fill=VD)
    y = rich(d, s['titulo'], M, 690, 64, {'b': PR, 'd': VD}, 72)
    rich(d, s['corpo'], M, y + 30, 38, {'b': CINZA, 'd': VD}, 54, peso='pjs500')
    foot(d, n, tot, PR); im.save(out, quality=90)


def s_evite(s, n, tot, out):
    im = Image.new('RGB', (W, H), BR); d = ImageDraw.Draw(im)
    capa.tracked(d, (M, 330), s.get('chapeu', 'O que evitar').upper(), fnt('mono500', 26), (190, 40, 40))
    y = rich(d, s['titulo'], M, 380, 64, {'b': PR, 'd': VD}, 72) + 40
    for it in s['itens']:
        d.rounded_rectangle((M, y, W - M, y + 150), 22, fill=(246, 244, 244))
        cx, cy = M + 50, y + 75
        d.line([(cx - 16, cy - 16), (cx + 16, cy + 16)], fill=(190, 40, 40), width=7)
        d.line([(cx - 16, cy + 16), (cx + 16, cy - 16)], fill=(190, 40, 40), width=7)
        rich(d, it, M + 100, y + 36, 34, {'b': CINZA, 'd': PR}, 44, 760, peso='pjs500')
        y += 180
    foot(d, n, tot, PR); im.save(out, quality=90)


def bubble(d, txt, side, y, f, maxw=720):
    lines, sp = capa.layout_lines([(txt, 'b')], f, maxw - 70, d)
    lh = int(f.size * 1.35)
    bw = max(sum(capa.word_w(d, w, f) for w, _ in ln) + sp * (len(ln) - 1) for ln in lines) + 70
    bh = len(lines) * lh + 50
    if side == 'p':
        x0, fill, cor = M, (44, 48, 46), BR
    else:
        x0, fill, cor = W - M - bw, LM, PR
    d.rounded_rectangle((x0, y, x0 + bw, y + bh), 30, fill=fill)
    capa.draw_title(d, [(txt, 'b')], x0 + 35, y + 25, f, maxw - 70, {'b': cor}, lh)
    return y + bh + 28


def s_chat(s, n, tot, out):
    im = Image.new('RGB', (W, H), (12, 20, 14)); d = ImageDraw.Draw(im)
    capa.tracked(d, (M, 230), s['chapeu'].upper(), fnt('mono500', 26), LM)
    y = 290
    if s.get('titulo'):
        y = rich(d, s['titulo'], M, y, 56, {'b': BR, 'd': LM}, 64) + 40
    f = fnt('pjs500', s.get('tam', 36))
    for side, txt in s['msgs']:
        if side == 'sep':
            y += 10
            d.line([(M, y), (W - M, y)], fill=(50, 60, 52), width=2); y += 36; continue
        if side == 'lbl':
            capa.tracked(d, (M, y), txt.upper(), fnt('mono500', 22), (150, 170, 150)); y += 44; continue
        y = bubble(d, txt, side, y, f)
    if s.get('nota'):
        rich(d, s['nota'], M, max(y + 20, 960), 34, {'b': (200, 210, 200), 'd': LM}, 46, peso='pjs500')
    foot(d, n, tot, BR); im.save(out, quality=90)


CTA = {
    'segue': ('Segue @o.ighormiranda', None),
    'manda': ('Manda pra', None),
    'salva': ('Salva esse post', None),
    'diagnostico': ('Comenta DIAGNÓSTICO', 'que eu te chamo no direct pra gente marcar um horário.'),
    'arkybook': ('Comenta ARKYBOOK', 'que eu te mando os 12 prompts pra usar no comercial da sua clínica.'),
}


def s_final(s, n, tot, out):
    im = Image.new('RGB', (W, H), BR); d = ImageDraw.Draw(im)
    ph = ImageOps.fit(ImageOps.exif_transpose(Image.open(FOT + s['foto'])).convert('RGB'), (420, 1120),
                      centering=(s.get('cx', 0.5), 0.3))
    im.paste(ph, (W - 420, 0))
    y = 200
    if s.get('titulo'):
        y = rich(d, s['titulo'], M, y, 52, {'b': PR, 'd': VD}, 60, 520) + 30
    for it in s.get('lista', []):
        d.line([(M + 2, y + 24), (M + 15, y + 37), (M + 40, y + 9)], fill=VD, width=6, joint='curve')
        rich(d, it, M + 56, y, 34, {'b': PR, 'd': VD}, 42, 450, peso='pjs700'); y += 62
    top = max(y + 40, 560 if not s.get('lista') else 700)
    head, sub = CTA[s['cta']]
    head = s.get('cta_titulo', head); sub = s.get('cta_sub', sub)
    d.rounded_rectangle((M, top, 640, top + 300), 26, fill=PR)
    yy = capa.draw_title(d, segs(head), M + 36, top + 36, fnt('pjs800', 44), 480, {'b': LM, 'd': LM}, 52)
    if sub: capa.draw_title(d, segs(sub), M + 36, yy + 14, fnt('pjs500', 32), 480, {'b': BR, 'd': LM}, 42)
    foot(d, n, tot, PR, right=W - 420 - 30)
    im.save(out, quality=90)


T = {'capa': s_capa, 'texto': s_texto, 'item': s_item, 'evite': s_evite, 'chat': s_chat, 'final': s_final}

if __name__ == '__main__':
    posts = json.load(open(sys.argv[1]))
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    only = set(sys.argv[3:])
    for p in posts:
        if only and p['id'] not in only: continue
        tot = len(p['slides'])
        for i, s in enumerate(p['slides'], 1):
            T[s['t']](s, i, tot, os.path.join(outdir, f"{p['id']}_slide{i:02d}.jpg"))
        print(p['id'], tot)
