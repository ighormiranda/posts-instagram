import sys
sys.path.insert(0,'.')
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import capa
F=capa.F; W,H,M=1080,1920,90
BR,PR,LM=(254,254,254),(4,4,4),(154,224,76)
fnt=lambda n,s: ImageFont.truetype(F+n+'.ttf',s)
EF=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
OUT='/home/claude/posts-instagram/stories/jogos/'
FOT='/home/claude/posts-instagram/fotos/'
def emoji(ch,size):
    im=Image.new('RGBA',(160,160),(0,0,0,0)); ImageDraw.Draw(im).text((10,10),ch,font=EF,embedded_color=True)
    im=im.crop(im.getbbox()); r=size/max(im.size)
    return im.resize((max(1,int(im.width*r)),max(1,int(im.height*r))),Image.LANCZOS)
def segs(x):
    out,d=[],False
    for p in x.split('*'):
        if p: out.append((p,'d' if d else 'b'))
        d=not d
    return out
def handle(d,cor=BR):
    f=fnt('mono500',26); t='@o.ighormiranda'; d.text(((W-d.textlength(t,font=f))/2,1640),t,font=f,fill=cor)
def grad(top,bot):
    im=Image.new('RGB',(1,H))
    for y in range(H):
        t=y/(H-1); im.putpixel((0,y),tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3)))
    return im.resize((W,H)).convert('RGBA')
def card(ch,ti,sub=None,tom='escuro',tam=80,y0=420):
    im=grad(*{'escuro':((30,34,32),(4,4,4)),'verde':((22,70,32),(4,12,6))}[tom]); d=ImageDraw.Draw(im)
    if ch: capa.tracked(d,(M,y0),ch,fnt('mono500',30),LM)
    y=capa.draw_title(d,segs(ti),M,y0+60,fnt('pjs800',tam),900,{'b':BR,'d':LM},int(tam*1.12))
    if sub: y=capa.draw_title(d,segs(sub),M,y+40,fnt('pjs500',42),900,{'b':(210,215,210),'d':LM},58)
    return im,d,y

# ---------- JOGO DO DRAGÃO ----------
foto=ImageOps.fit(ImageOps.exif_transpose(Image.open(FOT+'evento-makers/maca-no-rosto-plateia.jpg')).convert('RGB'),(W,H),centering=(0.5,0.5))
DX,DY,DS=945,150,40   # posição do dragão
def base_foto():
    im=foto.copy().convert('RGBA')
    g=Image.new('L',(1,H))
    for y in range(H): g.putpixel((0,y),int(200*max(0,(y-1350)/570)))
    sh=Image.new('RGBA',(W,H),PR+(255,)); sh.putalpha(g.resize((W,H))); return Image.alpha_composite(im,sh)
im=base_foto(); dr=emoji('🐉',DS); dr.putalpha(dr.getchannel('A').point(lambda v:int(v*0.92)))
im.alpha_composite(dr,(DX,DY)); d=ImageDraw.Draw(im)
capa.draw_title(d,segs('Makers Day.\nAinda tô processando\ntudo que eu vi lá.'),M,1400,fnt('pjs800',56),900,{'b':BR,'d':LM},64)
im.convert('RGB').save(OUT+'dragao-1-foto.jpg',quality=93)
cache=im

im,d,y=card('VOCÊ REPAROU?','Tinha um *dragão*\nescondido no\nstory anterior.',
 'Volta um story e procura.\n\nAchou? Me responde aqui com\n*DRAGÃO + onde ele tá.*\n\nO primeiro que acertar ganha\n*30 minutos de conversa\nsobre o seu negócio.*',tom='verde',tam=84,y0=330)
h=emoji('👈',120); im.alpha_composite(h,(M,y+50))
d=ImageDraw.Draw(im); d.text((M+150,y+82),'toca do lado esquerdo pra voltar',font=fnt('pjs700',34),fill=BR)
handle(d); im.convert('RGB').save(OUT+'dragao-2-pergunta.jpg',quality=93)

# revelação
im=base_foto(); im.alpha_composite(dr,(DX,DY))
dim=Image.new('RGBA',(W,H),(0,0,0,120)); m=Image.new('L',(W,H),255)
cx,cy=DX+DS//2,DY+DS//2; ImageDraw.Draw(m).ellipse((cx-70,cy-70,cx+70,cy+70),fill=0); dim.putalpha(m.point(lambda v:int(v*120/255)))
im=Image.alpha_composite(im,dim); d=ImageDraw.Draw(im)
d.ellipse((cx-70,cy-70,cx+70,cy+70),outline=LM,width=8)
z=foto.crop((cx-60,cy-60,cx+60,cy+60)).resize((330,330),Image.LANCZOS).convert('RGBA')
zd=dr.resize((DS*330//120,DS*330//120)); z.alpha_composite(zd,((330-zd.width)//2,(330-zd.height)//2))
mk=Image.new('L',(330,330),0); ImageDraw.Draw(mk).ellipse((0,0,330,330),fill=255)
zx,zy=660,470; im.paste(z,(zx,zy),mk); d.ellipse((zx,zy,zx+330,zy+330),outline=LM,width=8)
d.line([(cx-20,cy+68),(zx+200,zy+8)],fill=LM,width=6)
capa.tracked(d,(M,300),'TAVA AQUI',fnt('mono500',30),LM)
capa.draw_title(d,segs('Quem achou primeiro:\n*@'),M,360,fnt('pjs800',64),900,{'b':BR,'d':LM},72)
capa.draw_title(d,segs('Semana que vem tem outro.\nFica de olho nos stories.'),M,1430,fnt('pjs800',56),900,{'b':BR,'d':LM},64)
im.convert('RGB').save(OUT+'dragao-3-revelacao.jpg',quality=93)

# ---------- REAÇÕES ----------
def coracao(name,ch,ti,sub=None):
    im,d,y=card(ch,ti,sub,tam=80,y0=480)
    h=emoji('👇',130); im.alpha_composite(h,(W-h.width-60,1560))
    d=ImageDraw.Draw(im); f=fnt('pjs700',38); t='toca no coração aqui'
    d.text((W-h.width-80-d.textlength(t,font=f),1600),t,font=f,fill=LM)
    im.convert('RGB').save(OUT+name,quality=93)
coracao('reacao-1-preco.jpg','JÁ ACONTECEU AÍ?','Cliente pergunta\no preço no WhatsApp\n*e some.*','Se isso já aconteceu\nno seu negócio essa semana,\ntoca no coração.')
coracao('reacao-2-falta.jpg','SINCERÃO','Cliente marcou\na reunião\n*e não apareceu.*','Quem já passou por isso\ntoca no coração.\nVou te mostrar como evitar.')
# emoji resposta
im,d,y=card('ME RESPONDE COM 1 EMOJI','Como foi a sua\nsemana de vendas?\n*Sem mentir.*',None,tam=84,y0=420)
yy=y+80
for e,t in [('🔥','Bombou'),('😐','Mais ou menos'),('🥶','Parada')]:
    d.rounded_rectangle((M,yy,W-M,yy+150),30,fill=(30,40,34)); im.alpha_composite(emoji(e,90),(M+40,yy+30))
    d=ImageDraw.Draw(im); d.text((M+170,yy+45),t,font=fnt('pjs800',54),fill=BR); yy+=180
d.text((M,yy+30),'Responde aqui embaixo. Eu leio todas.',font=fnt('pjs500',38),fill=(210,215,210))
im.convert('RGB').save(OUT+'reacao-3-emoji.jpg',quality=93)
# quiz por toque
im,d,y=card('TESTE RÁPIDO','Qual mensagem faz\no cliente *responder*\nmais?',None,tam=78,y0=330)
yy=y+60
for k,t in [('A','"Olá! Segue nossa tabela\nde valores."'),('B','"Oi, Ana! Vi que você\nperguntou do plano anual.\nPosso te fazer 2 perguntas\nrápidas?"')]:
    nl=t.count('\n')+1; hh=70+nl*52
    d.rounded_rectangle((M,yy,W-M,yy+hh),30,fill=(30,40,34))
    d.text((M+36,yy+30),k,font=fnt('pjs800',60),fill=LM)
    capa.draw_title(d,segs(t),M+120,yy+36,fnt('pjs500',40),760,{'b':BR,'d':LM},52); yy+=hh+30
h=emoji('👉',120); im.alpha_composite(h,(W-h.width-70,yy+40))
d=ImageDraw.Draw(im); f=fnt('pjs700',38); t='pensa e toca pra ver'
d.text((W-h.width-90-d.textlength(t,font=f),yy+80),t,font=f,fill=LM)
handle(d); im.convert('RGB').save(OUT+'quiz-1-pergunta.jpg',quality=93)
im,d,y=card('RESPOSTA','*B.*\nDe longe.','Tem o nome da pessoa.\nMostra que você leu.\nE termina com uma pergunta\nfácil de responder.\n\nTabela sozinha\nvira "vou pensar".',tom='verde',tam=110,y0=420)
handle(d); im.convert('RGB').save(OUT+'quiz-2-resposta.jpg',quality=93)
