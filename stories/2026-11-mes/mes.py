import json, os
exec(open('jogo.py').read().split('# ---------- JOGO')[0])
OUT='/home/claude/posts-instagram/stories/2026-11-mes/'
PLAN=[]
def save(im,date,hhmm,slug,obs=''):
    fn=f'{date}_{hhmm}-{slug}.jpg'; im.convert('RGB').save(OUT+fn,quality=92)
    PLAN.append({'data':date,'hora':hhmm[:2]+':'+hhmm[2:],'arquivo':fn,'obs':obs})
def cta_emoji(im,d,y,txt,em='👇'):
    f=fnt('pjs800',44); w=d.textlength(txt,font=f)
    d.text((M,y),txt,font=f,fill=BR); e=emoji(em,62); im.alpha_composite(e,(int(M+w+16),y-6))
def rows(im,d,y,ops):
    for e,a,b in ops:
        d.rounded_rectangle((M,y,W-M,y+140),26,fill=(18,28,20),outline=(50,80,50),width=3)
        im.alpha_composite(emoji(e,90),(M+36,y+25))
        d.text((M+170,y+22),a,font=fnt('pjs800',48),fill=BR)
        if b: d.text((M+172,y+82),b,font=fnt('pjs500',32),fill=(190,200,190))
        y+=165
    return y
def T_text(date,hh,slug,chip,ti,sub=None,cta=None,em='👇',tom='verde',tam=84,y0=380,obs=''):
    im,d,y=card(chip,ti,sub,tom=tom,tam=tam,y0=y0)
    if cta: cta_emoji(im,d,y+70,cta,em)
    handle(d); save(im,date,hh,slug,obs)
def T_emojis(date,hh,slug,chip,ti,ops,cta='Me responde só com o emoji',tom='escuro'):
    im,d,y=card(chip,ti,None,tom=tom,tam=80,y0=300)
    y=rows(im,d,y+50,ops); cta_emoji(im,d,y+40,cta); handle(d); save(im,date,hh,slug)
def T_quiz(date,hh,slug,ti,a,b,certa,porque):
    im,d,y=card('QUIZ DE QUARTA',ti,None,tom='escuro',tam=74,y0=300)
    y+=50
    for L,t in (('A',a),('B',b)):
        d.rounded_rectangle((M,y,W-M,y+230),26,fill=(18,28,20),outline=(50,80,50),width=3)
        d.text((M+36,y+26),L,font=fnt('pjs800',64),fill=LM)
        capa.draw_title(d,segs(t),M+120,y+40,fnt('pjs500',38),700,{'b':BR,'d':LM},50); y+=260
    cta_emoji(im,d,y+30,'Pensa e toca pra ver','👉'); handle(d); save(im,date,hh,slug+'-pergunta')
    h2=hh[:3]+str(int(hh[3])+1)
    im,d,y=card('RESPOSTA',f'Letra *{certa}.*',porque,tom='verde',tam=110,y0=420)
    cta_emoji(im,d,y+70,'Acertou? Me responde com '+certa); handle(d); save(im,date,h2,slug+'-resposta')
def T_heart(date,hh,slug,ti):
    im,d,y=card('SEXTA DO CORAÇÃO',ti,None,tom='verde',tam=82,y0=420)
    d.text((M,1500),'Toca no coração aqui',font=fnt('pjs800',50),fill=BR)
    im.alpha_composite(emoji('👇',110),(880,1560))
    handle(d); save(im,date,hh,slug)
def T_ab(date,hh,slug,ti,a,b):
    im,d,y=card('DOMINGO: ISSO OU AQUILO',ti,None,tom='escuro',tam=78,y0=330)
    y+=60
    for L,t in (('A',a),('B',b)):
        d.rounded_rectangle((M,y,W-M,y+170),26,fill=(18,28,20),outline=(50,80,50),width=3)
        d.text((M+36,y+44),L,font=fnt('pjs800',70),fill=LM)
        capa.draw_title(d,segs(t),M+130,y+50,fnt('pjs700',44),720,{'b':BR,'d':LM},54); y+=200
    cta_emoji(im,d,y+40,'Me responde com A ou B'); handle(d); save(im,date,hh,slug)
def T_frase(date,hh,slug,ini):
    im,d,y=card('QUINTA: COMPLETE A FRASE',ini,None,tom='verde',tam=86,y0=420)
    d.line((M,y+40,M+520,y+40),fill=LM,width=6)
    cta_emoji(im,d,y+130,'Completa aqui na resposta'); handle(d); save(im,date,hh,slug)
def T_long(date,hh,slug,ti,body):
    im,d,y=card('TERÇA: MINI-AULA',ti,body,tom='escuro',tam=78,y0=360)
    d.text((M,250),'Segura o dedo na tela pra ler',font=fnt('pjs700',36),fill=LM)
    im.alpha_composite(emoji('☝️',56),(M+560,236))
    handle(d); save(im,date,hh,slug)
def jogo(date,foto,ch,x,y,leg,nome='um *objeto*\nescondido'):
    ph=ImageOps.fit(ImageOps.exif_transpose(Image.open(FOT+foto)).convert('RGB'),(W,H),centering=(0.5,0.5)).convert('RGBA')
    g=Image.new('L',(1,H))
    for yy in range(H): g.putpixel((0,yy),int(210*max(0,(yy-1300)/620)))
    sh=Image.new('RGBA',(W,H),PR+(255,)); sh.putalpha(g.resize((W,H))); ph=Image.alpha_composite(ph,sh)
    e=emoji(ch,42); e.putalpha(e.getchannel('A').point(lambda v:int(v*0.9)))
    a=ph.copy(); a.alpha_composite(e,(x,y)); d=ImageDraw.Draw(a)
    capa.draw_title(d,segs(leg),M,1420,fnt('pjs800',56),900,{'b':BR,'d':LM},66)
    save(a,date,'2030','jogo-1-foto',f'jogo: {ch} escondido em x={x},y={y}')
    im,d,yy=card('VOCÊ REPAROU?',f'Tinha {nome}\nno story anterior.','Volta um story e procura.\n\nAchou? Me responde\n*onde ele tá.*\n\nO primeiro que acertar ganha\n*30 minutos de conversa\nsobre o seu negócio.*',tom='verde',tam=84,y0=300)
    im.alpha_composite(emoji(ch,120),(W-M-130,190))
    im.alpha_composite(emoji('👈',110),(M,yy+50)); d=ImageDraw.Draw(im)
    d.text((M+140,yy+78),'toca do lado esquerdo pra voltar',font=fnt('pjs700',34),fill=BR)
    handle(d); save(im,date,'2045','jogo-2-pergunta')
    r=ph.copy(); r.alpha_composite(e,(x,y)); cx,cy=x+21,y+21
    dim=Image.new('RGBA',(W,H),(0,0,0,130)); mk=Image.new('L',(W,H),130); ImageDraw.Draw(mk).ellipse((cx-75,cy-75,cx+75,cy+75),fill=0); dim.putalpha(mk)
    r=Image.alpha_composite(r,dim); d=ImageDraw.Draw(r); d.ellipse((cx-75,cy-75,cx+75,cy+75),outline=LM,width=8)
    capa.tracked(d,(M,1400),'TAVA AQUI',fnt('mono500',34),LM)
    d.text((M,1460),'Quem achou primeiro: @',font=fnt('pjs800',56),fill=BR)
    d.text((M,1560),'Semana que vem tem outro.',font=fnt('pjs500',42),fill=(210,215,210))
    nd=f'2026-{date[5:7]}-{int(date[8:])+1:02d}' if date!='2026-11-30' else '2026-12-01'
    r.convert('RGB').save(OUT+f'MANUAL_{nd}-revelacao-{date}.jpg',quality=92)
    PLAN.append({'data':nd,'hora':'manual','arquivo':f'MANUAL_{nd}-revelacao-{date}.jpg','obs':'revelação manual com o @ do ganhador'})
BN='BLACK NOVEMBER DA LIGA'
exec(open('mes_conteudo.py').read())
json.dump(PLAN,open(OUT+'plano.json','w'),ensure_ascii=False,indent=1)
print(len(PLAN))
