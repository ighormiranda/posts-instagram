"""Carrossel de lançamento: Conheça a Maré Alta, da Presença 365 (paleta e fontes da Liga)."""
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import os
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(D))
F = R + '/ferramentas/fonts/'
W, H, M = 1080, 1350, 80
PRETO=(7,5,11); NAVY=(45,26,71); ROXO=(71,1,125); LUZ=(78,73,193); CARMIM=(206,20,61); AMAR=(227,230,42); BR=(254,254,254); SUB=(200,195,225)
anton=lambda s: ImageFont.truetype(F+'Anton-Regular.ttf', s)
pop=lambda s, w='Medium': ImageFont.truetype(F+f'Poppins-{w}.ttf', s)
mono=lambda s: ImageFont.truetype(F+'mono500.ttf', s)
TOT=5

def bg():
    im=Image.new('RGB',(W,H),PRETO); px=im.load()
    for y in range(H):
        t=y/H; c=tuple(int(PRETO[i]+(NAVY[i]-PRETO[i])*t) for i in range(3))
        for x in range(W): px[x,y]=c
    # pontilhado da marca
    d=ImageDraw.Draw(im)
    for y in range(20,H,26):
        for x in range(20+(13 if (y//26)%2 else 0),W,26):
            d.ellipse((x-2,y-2,x+2,y+2),fill=(52,36,92))
    return im

def wrap(d,txt,font,maxw):
    out,cur=[],''
    for w in txt.split(' '):
        t=(cur+' '+w).strip()
        if d.textlength(t.replace('*',''),font=font)>maxw and cur: out.append(cur);cur=w
        else: cur=t
    out.append(cur); return out

def text(d,txt,y,font,fill,lh,maxw=W-2*M,hl=AMAR,align='left',x0=M):
    on=False
    for ln in wrap(d,txt,font,maxw):
        lw=d.textlength(ln.replace('*',''),font=font)
        x=x0 if align=='left' else (W-lw)/2
        for i,p in enumerate(ln.split('*')):
            if i>0: on=not on
            if p: d.text((x,y),p,font=font,fill=hl if on else fill); x+=d.textlength(p,font=font)
        y+=lh
    return y

def foot(d,n):
    ft=mono(22); d.text((M,1282),'@o.ighormiranda',font=ft,fill=SUB)
    p=f'{n:02d}/{TOT:02d}'; d.text((W-M-d.textlength(p,font=ft),1282),p,font=ft,fill=SUB)

def tag(d,t,y,c=LUZ,fc=BR):
    ft=mono(26); tw=d.textlength(t,font=ft)
    d.rounded_rectangle((M,y,M+tw+44,y+50),25,fill=c); d.text((M+22,y+9),t,font=ft,fill=fc)

OUT=D+'/mare_slide'
# 1 capa
im=ImageOps.fit(Image.open(R+'/fotos/mare-alta/cena-01-grafico.png').convert('RGB'),(W,H),centering=(0.5,0.3))
g=Image.new('L',(W,H)); gd=ImageDraw.Draw(g)
for y in range(H): gd.line((0,y,W,y),fill=int(245*min(1,max(0,(y-820)/300))))
im.paste(Image.new('RGB',(W,H),PRETO),(0,0),g); d=ImageDraw.Draw(im)
d.text((M,1000),'CONHEÇA A',font=mono(34),fill=AMAR)
d.text((M,1036),'MARÉ ALTA',font=anton(170),fill=BR)
d.text((M,1250),'a heroína da Presença 365',font=pop(38,'SemiBold'),fill=SUB)
im.save(OUT+'01.jpg',quality=92)

# 2 problema
im=bg(); d=ImageDraw.Draw(im)
tag(d,'O PROBLEMA',300,CARMIM)
y=text(d,'Sua empresa some do Instagram por uma semana.',400,anton(96),BR,112)
y=text(d,'E o cliente *esquece* de você.',y+30,anton(96),BR,112,hl=CARMIM)
text(d,'Não é culpa sua. Você está atendendo, vendendo, resolvendo. Não sobra tempo pra postar todo dia.',y+50,pop(38),SUB,54)
foot(d,2); im.save(OUT+'02.jpg',quality=92)

# 3 o que ela faz (close-up da ficha)
im=bg(); d=ImageDraw.Draw(im)
sheet=Image.open(R+'/fotos/mare-alta/ficha-personagem-v2.png').convert('RGB')
sw,sh=sheet.size
face=sheet.crop((int(sw*0.715),int(sh*0.655),sw,sh))
face=ImageOps.fit(face,(W,560),centering=(0.5,0.4)); im.paste(face,(0,0))
g=Image.new('L',(W,560)); gd=ImageDraw.Draw(g)
for y in range(560): gd.line((0,y,W,y),fill=int(255*max(0,(y-380)/180)))
im.paste(Image.new('RGB',(W,560),PRETO),(0,0),g); d=ImageDraw.Draw(im)
tag(d,'O QUE ELA FAZ',590)
y=680
for i,t in enumerate(['Posta todo dia por você.','Descobre o que está dando certo.','Faz mais disso.']):
    d.text((M,y),str(i+1),font=anton(110),fill=AMAR)
    text(d,t,y+28,pop(46,'SemiBold'),BR,58,maxw=W-2*M-110,x0=M+100); y+=170
foot(d,3); im.save(OUT+'03.jpg',quality=92)

# 4 por que maré
im=bg(); d=ImageDraw.Draw(im)
tag(d,'POR QUE MARÉ ALTA',340)
y=text(d,'Maré não sobe num dia só.',440,anton(100),BR,116)
y=text(d,'Sobe *um pouco todo dia.*',y,anton(100),BR,116,hl=AMAR)
text(d,'É assim que a sua empresa vira lembrada: aparecendo todo dia, os 365 dias do ano. Você cuida da empresa. Ela cuida do seu Instagram.',y+50,pop(38),SUB,54)
foot(d,4); im.save(OUT+'04.jpg',quality=92)

# 5 chamada
im=bg(); d=ImageDraw.Draw(im)
y=text(d,'Quer a Maré Alta trabalhando na sua empresa?',380,anton(104),BR,120,align='center',maxw=900)
ft=anton(84); t='Manda PRESENÇA'; tw=d.textlength(t,font=ft)
d.rounded_rectangle(((W-tw)/2-50,y+50,(W+tw)/2+50,y+190),70,fill=AMAR)
d.text(((W-tw)/2,y+62),t,font=ft,fill=PRETO)
text(d,'no WhatsApp do link da bio',y+220,pop(40,'SemiBold'),BR,54,align='center')
text(d,'Presença 365 · Liga do Marketing',y+340,mono(28),SUB,40,align='center')
foot(d,5); im.save(OUT+'05.jpg',quality=92)
print('ok')
