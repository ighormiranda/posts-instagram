import sys, math
sys.path.insert(0,'.')
from motor import *
FOT='/home/claude/posts-instagram/fotos/'
LM=(154,224,76); LIL=(170,160,255)

# ---------- 1. Dica em motion (segunda) ----------
def grad_bg(t, c1=(22,40,26), c2=(4,4,4)):
    im=Image.new('RGB',(W,H),c2); d=ImageDraw.Draw(im)
    cx=W*0.5+180*math.sin(t*2.2); cy=H*0.42+120*math.cos(t*1.7)
    glow=Image.new('L',(W//4,H//4),0); gd=ImageDraw.Draw(glow)
    gd.ellipse((cx/4-110,cy/4-110,cx/4+110,cy/4+110),fill=150)
    glow=glow.filter(ImageFilter.GaussianBlur(40)).resize((W,H))
    return Image.composite(Image.new('RGB',(W,H),c1),im,glow)
T0=[0]
def cena_txt(dur,texto,size=118,chapeu=None,cta=None,y=640):
    def bg(t,_s=T0[0]): return grad_bg(_s+t*dur)
    def dr(img,t):
        yy=y
        if chapeu: draw_block(img,chapeu,yy-90,t,'mono500',38,cor=LM,dest=LM); 
        yy=draw_block(img,texto,yy,t,'Anton-Regular',size,dest=LM)
        if cta: draw_block(img,cta,yy+50,t-0.6,'pjs800',50,cor=(4,4,4),dest=(4,4,4),box=LM)
    T0[0]+=dur
    return {'dur':dur,'bg':bg,'draw':dr}
r1=[cena_txt(2.3,'Seu cliente\nnão te esqueceu\n*porque você é ruim.*'),
    cena_txt(2.2,'Ele esqueceu\n*porque você sumiu.*',size=140),
    cena_txt(2.8,'3 posts por semana:\n*12 lembranças* no mês.\nUm por dia: *30.*',size=112,chapeu='A CONTA'),
    cena_txt(3.0,'Quem aparece\ntodo dia\n*é lembrado.*',size=150,cta='Segue pra dica de amanhã')]

# ---------- 2. Maré Alta (quarta) ----------
FICHA=FOT+'mare-alta/ficha-personagem-v2.png'; CENA=FOT+'mare-alta/cena-01-grafico.png'
def foto_cena(path,dur,texto,crop=None,chapeu=None,cta=None,y=1020,size=104,dest=LIL,blur=0,pan=(0,0),zoom=1.12):
    base=load_bg(path,crop,zoom)
    if blur: base=base.filter(ImageFilter.GaussianBlur(blur))
    def bg(t): return shade(kb_frame(base,t,zoom,pan))
    def dr(img,t):
        yy=y
        if chapeu: draw_block(img,chapeu,yy-80,t,'mono500',36,cor=dest,dest=dest)
        yy=draw_block(img,texto,yy,t,'Anton-Regular',size,dest=dest)
        if cta: draw_block(img,cta,yy+40,t-0.6,'pjs800',48,cor=(4,4,4),dest=(4,4,4),box=dest)
    return {'dur':dur,'bg':bg,'draw':dr}
r2=[foto_cena(CENA,2.8,'Toda empresa tem\num inimigo *invisível.*',chapeu='EPISÓDIO 1 · A ORIGEM'),
    foto_cena(CENA,2.8,'*O Sumiço.*\nEle chega quando\nvocê para de postar.',blur=6),
    foto_cena(FICHA,2.8,'Mas toda maré\ntem uma *heroína.*',crop=(0,0,560,941)),
    foto_cena(FICHA,3.0,'*Maré Alta.*\nUm post por dia.\nO ano inteiro.',crop=(1160,330,1672,630),size=110),
    foto_cena(FICHA,3.0,'Episódio 2\nna próxima quarta.',crop=(1160,610,1672,941),cta='Segue pra não perder',size=110)]

# ---------- 3. Pessoal (sábado) ----------
def pessoal(path,dur,texto,sub=None,cta=None,size=104):
    base=load_bg(path)
    def bg(t): return shade(kb_frame(base,t),bot=0.9)
    def dr(img,t):
        yy=draw_block(img,texto,1000,t,'pjs800',size,dest=LM,lh=1.12)
        if sub: yy=draw_block(img,sub,yy+20,t-0.4,'pjs500',44,cor=(225,225,225),dest=LM,lh=1.3)
        if cta: draw_block(img,cta,yy+40,t-0.6,'pjs800',48,cor=(4,4,4),dest=(4,4,4),box=LM)
    return {'dur':dur,'bg':bg,'draw':dr}
r3=[pessoal(FOT+'jaqueta-externa/bracos-cruzados.jpg',2.4,'3 coisas que\nquase ninguém\n*sabe sobre mim.*'),
    pessoal(FOT+'estudio-camisa-roxa/sorrindo.jpg',3.2,'1. Minha primeira\nvenda foi aos *7 anos.*','Bijuteria pras professoras.\nPra comprar um anel de dragão.',size=88),
    pessoal(FOT+'jaqueta-externa/olhando-lado.jpg',3.2,'2. Dei aula de wakeboard\npro *Amazing Race China.*','Quando eu era GO\nno Club Med.',size=80),
    pessoal(FOT+'escritorio/em-pe-escritorio-janela.jpg',3.0,'3. Antes do marketing,\ntrabalhei na *Petrobras.*','E na Eletronuclear.',size=80),
    pessoal(FOT+'palco/palestrando.jpg',3.0,'Hoje eu junto\ntudo isso *na Liga.*',cta='Segue pra conhecer o resto',size=96)]

quais=sys.argv[1:] or ['1','2','3']
if '1' in quais: render(r1,'amostra-1-dica-motion.mp4',7)
if '2' in quais: render(r2,'amostra-2-mare-alta-ep1.mp4',2,cor_selo=LIL)
if '3' in quais: render(r3,'amostra-3-pessoal.mp4',5)
print('ok')
