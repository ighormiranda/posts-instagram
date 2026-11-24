"""Carrossel 'Guerra cibernética? Fato x boato' (inspirado no formato do @phmquintanilha: fonte + número + meta prática)."""
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import os
D = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(D)
F = R + '/ferramentas/fonts/'
W, H, M = 1080, 1350, 80
LM = (154, 224, 76); BR = (250, 250, 248); SUB = (200, 210, 200); BG = (6, 8, 6); RED = (240, 90, 80)
f = lambda n, s: ImageFont.truetype(F + n + '.ttf', s)
OUT = D + '/ciber_slide'
TOT = 10


def grad(top=(6, 8, 6), bot=(18, 70, 34), flip=False):
    im = Image.new('RGB', (W, H), top)
    px = im.load()
    for y in range(H):
        t = y / H if not flip else 1 - y / H
        t = max(0, (t - 0.35) / 0.65)
        c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    return im


def scan(d, y0, y1):
    for y in range(y0, y1, 9):
        for x in range(240, W - 240, 14):
            d.point((x, y), fill=(60, 80, 60))


def center(d, txt, y, font, fill, lh, maxw=920, hl=None):
    """Quebra e centraliza. Trechos entre * * ficam na cor hl."""
    words = txt.split(' ')
    lines, cur = [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t.replace('*', ''), font=font) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    on = False
    for ln in lines:
        x = (W - d.textlength(ln.replace('*', ''), font=font)) / 2
        parts = ln.split('*')
        for i, part in enumerate(parts):
            if i > 0: on = not on
            if part:
                d.text((x, y), part, font=font, fill=(hl if on and hl else fill))
                x += d.textlength(part, font=font)
        y += lh
    return y


def foot(d, n):
    ft = f('mono500', 22)
    d.text((M, 1278), '@o.ighormiranda', font=ft, fill=(150, 165, 150))
    p = f'{n:02d}/{TOT:02d}'
    d.text((W - M - d.textlength(p, font=ft), 1278), p, font=ft, fill=(150, 165, 150))


def dado(n, titulo, fonte, big, lado, corpo, tag='FATO', tagc=LM, flip=False):
    im = grad(flip=flip); d = ImageDraw.Draw(im)
    scan(d, 250, 280)
    # selo fato/boato
    ft = f('mono500', 26); tw = d.textlength(tag, font=ft)
    d.rounded_rectangle(((W - tw) / 2 - 22, 290, (W + tw) / 2 + 22, 338), 24, fill=tagc)
    d.text(((W - tw) / 2, 298), tag, font=ft, fill=BG)
    y = center(d, titulo, 390, f('pjs800', 64), LM, 76)
    scan(d, y + 10, y + 40)
    # caixa de fonte
    by = y + 60; bh = 210
    d.rectangle((M - 20, by, W - M + 20, by + bh), outline=(70, 90, 70), width=2, fill=(10, 16, 11))
    fc = f('pjs700', 26); fw = d.textlength('• Fonte: ' + fonte, font=fc)
    d.rounded_rectangle((M + 6, by + 22, M + 40 + fw, by + 66), 22, fill=(24, 60, 30))
    d.text((M + 22, by + 28), '• Fonte: ' + fonte, font=fc, fill=LM)
    fb = f('pjs800', 104 if len(big) < 7 else 84)
    d.text((M + 10, by + 78), big, font=fb, fill=LM)
    bw = d.textlength(big, font=fb)
    fl = f('pjs500', 32); yy = by + 96
    words, cur, lines = lado.split(' '), '', []
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=fl) > W - 2 * M - bw - 50 and cur: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur)
    for ln in lines[:3]:
        d.text((M + bw + 40, yy), ln, font=fl, fill=BR); yy += 40
    center(d, corpo, by + bh + 60, f('pjs500', 42), BR, 56, hl=LM)
    foot(d, n); im.save(OUT + f'{n:02d}.jpg', quality=92)


def foto(n, path, frase, meta, center_y=0.3):
    im = Image.new('RGB', (W, H), BG)
    ph = ImageOps.fit(Image.open(path).convert('RGB'), (W, 620), centering=(0.5, center_y))
    im.paste(ph, (0, 0))
    g = Image.new('L', (W, 620))
    gd = ImageDraw.Draw(g)
    for y in range(620): gd.line((0, y, W, y), fill=int(255 * max(0, (y - 430) / 190)))
    im.paste(Image.new('RGB', (W, 620), BG), (0, 0), g)
    low = grad(flip=True).crop((0, 620, W, H)); im.paste(low, (0, 620))
    d = ImageDraw.Draw(im)
    scan(d, 640, 660)
    y = center(d, frase, 690, f('pjs800', 50), BR, 62, hl=LM)
    by = y + 40
    fm = f('pjs500', 34)
    # mede o texto da meta
    tmp = Image.new('RGB', (W, 400)); td = ImageDraw.Draw(tmp)
    h_end = center(td, meta, 0, fm, BR, 46, maxw=820)
    bh = 90 + h_end + 30
    d.rectangle((M - 20, by, W - M + 20, by + bh), outline=LM, width=3)
    center(d, 'Meta prática pra esta semana', by + 26, f('pjs700', 34), LM, 40)
    center(d, meta, by + 90, fm, BR, 46, maxw=820)
    foot(d, n); im.save(OUT + f'{n:02d}.jpg', quality=92)


# 1 capa
im = Image.new('RGB', (W, H), BG)
ph = ImageOps.fit(Image.open(R + '/fotos/palco/palestrando-fundo-verde.jpg').convert('RGB'), (W, H), centering=(0.5, 0.2))
im.paste(ph, (0, 0))
ov = Image.new('L', (W, H)); od = ImageDraw.Draw(ov)
for y in range(H): od.line((0, y, W, y), fill=int(235 * max(0, (y - 380) / 520)) if y < 900 else 235)
im.paste(Image.new('RGB', (W, H), (8, 30, 14)), (0, 0), ov)
d = ImageDraw.Draw(im)
y = center(d, 'Guerra', 700, f('pjs800', 150), LM, 150)
y = center(d, 'cibernética?', y - 10, f('pjs800', 104), BR, 110)
y = center(d, 'O que é *fato*, o que é *boato* e o que fazer na sua empresa', y + 20, f('pjs700', 44), BR, 54, maxw=880, hl=LM)
pill = 'segundo as fontes oficiais de novembro'
fp = f('pjs500', 32); pw = d.textlength(pill, font=fp)
d.rounded_rectangle(((W - pw) / 2 - 30, y + 30, (W + pw) / 2 + 30, y + 92), 31, outline=(140, 200, 120), width=2)
d.text(((W - pw) / 2, y + 42), pill, font=fp, fill=BR)
foot(d, 1); im.save(OUT + '01.jpg', quality=92)

dado(2, '#1 Vazaram nome e CPF de quem tem previdência.', 'Caixa Seguridade', '7,6 mi',
     'de clientes ativos na base atingida', 'A Caixa Vida e Previdência achou o ataque em 6/11. Foram copiados *nomes e CPFs*. Senhas, saldos e dados bancários não, segundo a empresa.')
foto(3, R + '/fotos/evento-makers/anotando-plateia.jpg',
     'O golpe vem *depois* do vazamento: alguém liga sabendo o seu nome e o seu CPF.',
     'Combine com a sua equipe: banco e seguradora não pedem senha nem código por telefone. Desligou e liga de volta no número oficial.')
dado(4, '#2 Até o Tesouro Nacional foi atingido.', 'Tesouro Nacional', '4 mil',
     'chaves Pix expostas, em 30 mil cadastros', 'O acesso indevido foi achado em 4/11. O Tesouro diz que *não houve impacto financeiro*. Mas chave Pix + nome é tudo que um golpista quer.', flip=True)
dado(5, '#3 O maior porto da América Latina parou o administrativo.', 'Autoridade Portuária de Santos', 'Manual',
     'foi como o administrativo voltou a funcionar', 'O Porto de Santos confirmou o ataque em 6/11 e a Polícia Federal investiga. Navios e acessos seguiram operando. *Quem tem processo só no sistema, para junto.*')
foto(6, R + '/fotos/evento-makers/bracos-cruzados-em-pe.jpg',
     'Se o seu sistema cair amanhã, o que a sua empresa *consegue fazer no papel?*',
     'Tenha uma cópia dos arquivos importantes fora do computador e teste hoje se ela abre.', center_y=0.25)
dado(7, '#4 Os criminosos já usam agentes de IA.', 'Banco Central', '115',
     'incidentes cibernéticos no sistema financeiro em 2026', 'Em 17/11 o BC disse que o risco *subiu desde outubro* por causa de ataques feitos com agentes de inteligência artificial.', flip=True)
dado(8, '#5 O "apagão mundial" do dia 17 não aconteceu.', 'Microsoft, FAA e operadoras', 'Boato',
     'nenhum governo ou operadora anunciou apagão', 'Várias quedas que viralizaram este mês foram *falha técnica*, não ataque: Microsoft 365 e os voos nos EUA, segundo as próprias empresas.', tag='BOATO', tagc=RED)
foto(9, R + '/fotos/palco/palestrando.jpg',
     'Pânico não protege ninguém. *Hábito* protege.',
     'Ative hoje a verificação em duas etapas no e-mail, no banco e no Instagram da empresa.', center_y=0.2)

# 10 fecho
im = grad(); d = ImageDraw.Draw(im)
scan(d, 380, 410)
y = center(d, 'Você não precisa virar especialista em segurança.', 440, f('pjs800', 66), LM, 76)
y = center(d, 'Precisa de *3 hábitos*: desconfiar da ligação, ter cópia fora do computador e duas etapas em tudo.', y + 30, f('pjs500', 40), BR, 52, hl=LM)
y = center(d, 'Manda esse post pro seu sócio.', y + 50, f('pjs800', 46), BR, 56)
center(d, 'E me segue pra entender IA e tecnologia *sem pânico*.', y + 10, f('pjs500', 36), SUB, 46, hl=LM)
foot(d, 10); im.save(OUT + '10.jpg', quality=92)
print('ok')
