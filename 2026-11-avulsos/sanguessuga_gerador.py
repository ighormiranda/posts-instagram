exec(open('sexta13.py').read().split('TOT=7')[0])
ID='sanguessuga'; TOT=8
FD='/home/claude/posts-instagram/fotos/estudio-blazer-marinho/'
def fade(im,y0,y1,top=False):
    g=Image.new('L',(1,H))
    for y in range(H):
        t=min(1,max(0,(y-y0)/(y1-y0))); g.putpixel((0,y),int(255*(1-t if top else t)))
    im.paste(Image.new('RGB',(W,H),BK),(0,0),g.resize((W,H))); return im
def duo(path,cen=(0.5,0.2),h=H):
    ph=ImageOps.fit(Image.open(path).convert('L'),(W,h),centering=cen)
    ph=ImageOps.autocontrast(ph,cutoff=2)
    return ImageOps.colorize(ph,black=(0,0,0),mid=(110,10,16),white=(240,205,195))
def wrap(d,txt,f,maxw):
    out=[]
    for par in txt.split('\n'):
        ln=''
        for w in par.split():
            t=(ln+' '+w).strip()
            if d.textlength(t,font=f)<=maxw: ln=t
            else: out.append(ln); ln=w
        out.append(ln)
    return '\n'.join(out)
# 1 capa: vampiro IA
v=ImageOps.fit(Image.open(FD+'vampiro-ia.png').convert('RGB'),(W,H),centering=(0.5,0.15))
v=fade(v,620,1080); v=textura(v); d=ImageDraw.Draw(v)
centered(d,860,'TEM UM SANGUESSUGA',CR(96),RED)
centered(d,965,'no seu negócio.',CR(96),BONE)
centered(d,1100,'Ele não aparece no espelho.\nAparece no fim do mês, no caixa.',EL(36),DIM,48)
foot(d,1,TOT); v.save(OUT+f'{ID}_slide01.jpg',quality=92)
itens=[('serio-maos-bolso.jpg',(0.5,0.12),'O lead esquecido','Chamou no direct, pediu informação\ne ninguém respondeu no mesmo dia.\nEsfriou. Foi pro concorrente.','Responder rápido e ter follow-up\npronto pra quem não respondeu.'),
 ('serio-abotoando.jpg',(0.5,0.15),'O "vou pensar"','Perguntou o preço, visualizou\ne sumiu. E você nunca mais chamou.','Voltar a falar em 24h, 3 dias e 7 dias,\nsem pressão, com algo de valor.'),
 ('olhar-lado-abotoando.jpg',(0.5,0.12),'O desconto no susto','O cliente hesitou e você\nbaixou o preço antes dele pedir.\nA margem sangra calada.','Mostrar valor antes do preço.\nDesconto só com contrapartida.'),
 ('serio-tres-quartos.jpg',(0.5,0.1),'O cliente que some','Comprou uma vez e nunca mais\nouviu falar de você.\nO mais barato de vender, perdido.','Pós-venda e lembrete na hora certa.\nQuem já comprou compra de novo.'),
 ('serio-maos-bolso.jpg',(0.5,0.05),'O perfil parado','Sem post, ninguém lembra.\nSem lembrar, ninguém chama.\nO silêncio também cobra a conta.','Aparecer todo dia.\nAqui eu automatizei: +393% de\nvisualizações nos primeiros 30 dias.')]
for i,(f,cen,t,s,cura) in enumerate(itens,2):
    im=Image.new('RGB',(W,H),BK); ph=duo(FD+f,cen,620); im.paste(ph,(0,0))
    im=fade(im,330,620); im=textura(im); d=ImageDraw.Draw(im)
    centered(d,560,f'SANGUESSUGA Nº{i-1}',EL(36),RED)
    y=centered(d,615,t,CR(92),BONE,100)
    y=centered(d,y+20,s,EL(36),DIM,48)
    y+=34; d.line((W/2-60,y,W/2+60,y),fill=RED,width=3)
    centered(d,y+28,'COMO MATAR',PJ('pjs800',28),RED)
    centered(d,y+72,cura,PJ('pjs700',34),BONE,46)
    foot(d,i,TOT); im.save(OUT+f'{ID}_slide{i:02d}.jpg',quality=92)
# 7 virada: caçador (foto colorida séria, leve escurecida)
ph=ImageOps.fit(Image.open(FD+'serio-tres-quartos.jpg').convert('RGB'),(W,H),centering=(0.5,0.1))
ph=ImageOps.colorize(ImageOps.autocontrast(ph.convert('L'),cutoff=2),black=(0,0,0),mid=(60,40,38),white=(235,225,215))
im=fade(ph,560,980); im=textura(im); d=ImageDraw.Draw(im)
centered(d,860,'Todo negócio tem.',CR(88),BONE)
centered(d,965,'O problema é deixar sugando.',EL(40),DIM)
centered(d,1050,'Qual desses tá no seu?\nMe conta nos comentários: 1, 2, 3, 4 ou 5.',PJ('pjs700',34),BONE,46)
foot(d,7,TOT); im.save(OUT+f'{ID}_slide07.jpg',quality=92)
# 8 final: sorrindo, cor real = o dia amanheceu
ph=ImageOps.fit(Image.open(FD+'sorrindo-frente-aberto.jpg').convert('RGB'),(W,H),centering=(0.5,0.1))
im=fade(ph,520,900); im=textura(im); d=ImageDraw.Draw(im)
centered(d,800,'Eu caço sanguessuga',CR(80),BONE)
centered(d,890,'em negócio todo dia.',CR(80),RED)
d.rectangle((M+60,1010,W-M-60,1180),outline=RED,width=4)
centered(d,1035,'LINK NA BIO',PJ('pjs800',58),RED)
centered(d,1115,'Black November · só 5 vagas',EL(34),BONE)
foot(d,8,TOT); im.save(OUT+f'{ID}_slide08.jpg',quality=92)
print('ok')
