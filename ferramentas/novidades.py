"""Série "Novidades da IA" (toda sexta) no padrão @o.ighormiranda.

Uso:
  python3 novidades.py edicao.json saida_dir            -> slides .jpg (prévia; vídeo vira moldura "VÍDEO OFICIAL")
  python3 novidades.py edicao.json saida_dir --videos   -> slides com vídeo viram .mp4 (precisa do arquivo em item.video)

edicao.json:
{
  "id": "ia-2026-11-13",
  "semana": "SEMANA DE 09 A 13/11",
  "titulo": "O que saiu de IA essa semana\n*e o que muda pro seu negócio.*",
  "foto": "escritorio/mesa-laptop-cafe.jpg",
  "itens": [
    {"empresa": "ANTHROPIC", "titulo": "...", "texto": "...", "pratica": "...",
     "fonte": "Anthropic (anthropic.com/news/...)", "video": "caminho/opcional.mp4", "imagem": "caminho/opcional.jpg"}
  ]
}
Regra: só notícia verificada em fonte oficial; vídeo só oficial da empresa, com crédito.
"""
import sys, os, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont, ImageOps
import capa, gen

F = capa.F
W, H, M = 1080, 1350, 80
BR, PR, LM = (254, 254, 254), (4, 4, 4), (154, 224, 76)
SUB = (205, 210, 205)
fnt = lambda n, s: ImageFont.truetype(F + n + '.ttf', s)
FRAME = (M, 0, W - M, 0)  # y definido por slide
FW, FH = W - 2 * M, int((W - 2 * M) * 9 / 16)


def segs(x):
    return gen.segs(x)


def rich(d, txt, x, y, size, cores, lh=None, maxw=920, peso='pjs800'):
    lh = lh or int(size * 1.15)
    return capa.draw_title(d, segs(txt), x, y, fnt(peso, size), maxw, cores, lh)


def foot(d, n, tot):
    f = fnt('mono500', 22)
    d.text((M, 1260), '@o.ighormiranda', font=f, fill=(150, 160, 150))
    p = f'{n:02d}/{tot:02d}'
    d.text((W - M - d.textlength(p, font=f), 1260), p, font=f, fill=(150, 160, 150))


def capa_slide(ed, tot, out):
    im = Image.new('RGB', (W, H), PR)
    ph = ImageOps.fit(ImageOps.exif_transpose(Image.open(gen.FOT + ed['foto'])).convert('RGB'), (W, 760), centering=(0.5, 0.3))
    im.paste(ph, (0, 0))
    g = Image.new('L', (1, 760))
    for y in range(760): g.putpixel((0, y), int(255 * max(0, (y - 380) / 380)))
    sh = Image.new('RGB', (W, 760), PR); im.paste(sh, (0, 0), g.resize((W, 760)))
    d = ImageDraw.Draw(im)
    tag = 'NOVIDADES DA IA · ' + ed['semana']
    f = fnt('mono500', 26); tw = d.textlength(tag, font=f) + len(tag) * 6 + 56
    d.rounded_rectangle((M, 690, M + tw, 746), 28, fill=LM)
    capa.tracked(d, (M + 25, 704), tag, f, PR)
    rich(d, ed['titulo'], M, 790, 62, {'b': BR, 'd': LM}, 72)
    d.text((M, 1180), 'Arrasta pro lado', font=fnt('pjs500', 32), fill=SUB)
    foot(d, 1, tot)
    im.save(out, quality=92)


def item_slide(it, k, n, tot, out_png, final=False):
    """Desenha o slide e devolve a caixa da moldura de mídia (x0,y0,x1,y1)."""
    im = Image.new('RGB', (W, H), PR); d = ImageDraw.Draw(im)
    semmidia = final and not ((it.get('imagem') and os.path.exists(it['imagem'])) or (it.get('video') and os.path.exists(it['video'])))
    top = 330 if semmidia else 110
    capa.tracked(d, (M, top), f'{k:02d} · {it["empresa"].upper()}', fnt('mono500', 26), LM)
    y = rich(d, it['titulo'], M, top + 50, 60 if semmidia else 52, {'b': BR, 'd': LM}, 70 if semmidia else 60)
    y = rich(d, it['texto'], M, y + 18, 38 if semmidia else 34, {'b': SUB, 'd': LM}, 52 if semmidia else 46, peso='pjs500')
    fy = y + 34
    box = (M, fy, M + FW, fy + FH)
    temmidia = (it.get('imagem') and os.path.exists(it['imagem'])) or (it.get('video') and os.path.exists(it['video']))
    if final and not temmidia:
        d.text((M, y + 30), 'Fonte: ' + it.get('fonte', ''), font=fnt('pjs500', 24), fill=(130, 140, 130))
        if it.get('pratica'):
            yy = y + 110
            d.rounded_rectangle((M, yy, W - M, yy + 170), 22, fill=(20, 40, 24))
            capa.tracked(d, (M + 28, yy + 24), 'NA PRÁTICA', fnt('mono500', 24), LM)
            rich(d, it['pratica'], M + 28, yy + 62, 36, {'b': BR, 'd': LM}, 46, maxw=W - 2 * M - 56, peso='pjs700')
        foot(d, n, tot); im.save(out_png, quality=92); return None
    if it.get('imagem') and os.path.exists(it['imagem']):
        img = ImageOps.fit(Image.open(it['imagem']).convert('RGB'), (FW, FH))
        m = Image.new('L', (FW, FH), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, FW, FH), 24, fill=255)
        im.paste(img, box[:2], m)
    else:
        d.rounded_rectangle(box, 24, fill=(22, 28, 24))
        t = 'VÍDEO OFICIAL'; f = fnt('mono500', 28)
        d.text(((W - d.textlength(t, font=f)) / 2, fy + FH / 2 - 40), t, font=f, fill=(120, 130, 120))
        f2 = fnt('pjs500', 26); s = it.get('fonte', '')[:60]
        d.text(((W - d.textlength(s, font=f2)) / 2, fy + FH / 2 + 4), s, font=f2, fill=(100, 110, 100))
    y = fy + FH + 22
    d.text((M, y), 'Fonte: ' + it.get('fonte', ''), font=fnt('pjs500', 24), fill=(130, 140, 130))
    if it.get('pratica'):
        yy = max(y + 60, 1080)
        d.rounded_rectangle((M, yy, W - M, yy + 140), 22, fill=(20, 40, 24))
        capa.tracked(d, (M + 28, yy + 20), 'NA PRÁTICA', fnt('mono500', 22), LM)
        rich(d, it['pratica'], M + 28, yy + 54, 30, {'b': BR, 'd': LM}, 38, maxw=W - 2 * M - 56, peso='pjs700')
    foot(d, n, tot)
    im.save(out_png, quality=92)
    return box


def final_slide(n, tot, out):
    im = Image.new('RGB', (W, H), PR); d = ImageDraw.Draw(im)
    capa.tracked(d, (M, 440), 'TODA SEXTA TEM', fnt('mono500', 28), LM)
    y = rich(d, 'As novidades da IA\nda semana, filtradas\n*pro seu negócio.*', M, 500, 72, {'b': BR, 'd': LM}, 82)
    rich(d, 'Segue @o.ighormiranda\npra não perder a próxima.', M, y + 50, 44, {'b': SUB, 'd': LM}, 58, peso='pjs700')
    foot(d, n, tot)
    im.save(out, quality=92)


def video_slide(png, box, video, out_mp4, maxdur=30):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    fc = (f"[1:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1,fps=30[v];"
          f"[0:v][v]overlay={x0}:{y0}:shortest=1,format=yuv420p")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', png, '-t', str(maxdur), '-i', video,
                    '-filter_complex', fc, '-t', str(maxdur), '-c:v', 'libx264', '-crf', '20', '-an',
                    '-movflags', '+faststart', out_mp4], check=True)


if __name__ == '__main__':
    ed = json.load(open(sys.argv[1])); outd = sys.argv[2]; os.makedirs(outd, exist_ok=True)
    comvideo = '--videos' in sys.argv
    tot = len(ed['itens']) + 2; pid = ed['id']
    capa_slide(ed, tot, f'{outd}/{pid}_slide01.jpg')
    for k, it in enumerate(ed['itens'], 1):
        png = f'{outd}/{pid}_slide{k + 1:02d}.jpg'
        box = item_slide(it, k, k + 1, tot, png, final=comvideo)
        if comvideo and box and it.get('video') and os.path.exists(it['video']):
            video_slide(png, box, it['video'], f'{outd}/{pid}_slide{k + 1:02d}.mp4')
    final_slide(tot, tot, f'{outd}/{pid}_slide{tot:02d}.jpg')
    print('ok', tot, 'slides')
