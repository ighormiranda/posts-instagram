import subprocess, re, os
from PIL import Image, ImageDraw, ImageFont
A='/mnt/user-data/attachments/6b783e31-48d9-5fd3-b925-355c9d9bd392/'
F='/home/claude/posts-instagram/ferramentas/fonts/'
W,H=1080,1920
LM=(154,224,76)
cuts=[('b4847473-IMG_4549.mov',0.10,17.75,[(0.32,2.46,'Primo Rico: *3.*'),(2.84,4.52,'Hormozi: *3.*'),(4.98,6.78,'Pedro Quintanilha: *3.*'),(7.28,11.34,'Joel Jota: *2,7.* Mas eu já ouvi da boca dele mesmo:'),(11.34,13.54,'quando ele começou, ele fazia *6 por dia.*'),(14.08,17.52,'E foi isso que tornou o Joel Jota o Joel Jota que nós conhecemos hoje.')]),
      ('79927eaf-IMG_4550.mov',0.10,2.75,[(0.28,2.54,'E você? *Uma vez por semana?*')]),
      ('e1f631e2-IMG_4551.mov',0.00,3.80,[(0.07,3.67,'Eu também não tenho tempo de gravar *três vezes por dia,* eu te entendo.')]),
      ('2c981559-IMG_4553.mov',0.20,7.00,[(0.40,5.06,'E por isso eu montei *um sistema que posta por mim* e que pode postar por você também.'),(5.70,6.58,'Me chama no *direct.*')])]
os.makedirs('tmp',exist_ok=True)
# 1. cortes verticais 1080x1920 30fps
parts=[];caps=[];t0=0
for i,(f,a,b,segs) in enumerate(cuts):
    out=f'tmp/p{i}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',A+f,'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1',
        '-af','loudnorm=I=-15:TP=-1.5:LRA=11','-ar','44100','-ac','2','-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','-b:a','160k',out],check=True)
    parts.append(out)
    for s,e,tx in segs:
        # divide em blocos de até 3 palavras, tempo proporcional ao tamanho
        words=tx.split(' '); chunks=[];cur=[]
        for w in words:
            cur.append(w)
            if len(cur)==3 or w.endswith(('.',',','?')): chunks.append(' '.join(cur));cur=[]
        if cur: chunks.append(' '.join(cur))
        # reequilibra destaque: estado do * entre blocos
        tot=sum(len(c) for c in chunks); tt=s-a
        dest=False; fixed=[]
        for c in chunks:
            pre='*' if dest else ''
            n=c.count('*'); 
            if n%2: dest=not dest
            suf='*' if dest else ''
            fixed.append(pre+c+suf)
        for c in fixed:
            d=(e-s)*len(c.replace('*',''))/max(1,len(tx.replace('*','')))
            caps.append((t0+tt,t0+tt+d,c)); tt+=d
    t0+=b-a
TOTAL=t0
with open('tmp/list.txt','w') as fl:
    for p in parts: fl.write(f"file '{os.path.abspath(p)}'\n")
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','tmp/list.txt','-c','copy','tmp/base0.mp4'],check=True)
subprocess.run(['python3','../dentes.py','tmp/base0.mp4','tmp/base.mp4'],check=True)

def fnt(n,s): return ImageFont.truetype(F+n+'.ttf',s)
def segs(t):
    out,d=[],False
    for p in t.split('*'):
        if p: out.append((p,d))
        d=not d
    return out
# 2. overlays PNG
def caption_png(txt,path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',74)
    sg=segs(txt); tw=sum(d.textlength(p,font=f) for p,_ in sg)
    x=(W-tw)/2; y=1370
    for p,ds in sg:
        d.text((x,y),p,font=f,fill=LM if ds else (255,255,255),stroke_width=7,stroke_fill=(0,0,0))
        x+=d.textlength(p,font=f)
    im.save(path)
def title_png(path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',50)
    lines=['Quantas vezes por dia','os grandes postam?']
    ws=[d.textlength(l,font=f) for l in lines]; bw=max(ws)+70
    POS='right'
    bx0=(W-bw)/2 if POS=='center' else W-40-bw
    d.rounded_rectangle((bx0,250,bx0+bw,250+2*64+44),22,fill=(255,255,255,240))
    for k,l in enumerate(lines): d.text((bx0+(bw-ws[k])/2,270+k*64),l,font=f,fill=(10,10,10))
    f2=fnt('mono500',26); s='posts no feed de 12 a 26/11/2026'
    0 and d.text(((W-d.textlength(s,font=f2))/2,445),s,font=f2,fill=(235,235,235),stroke_width=3,stroke_fill=(0,0,0))
    im.save(path)
def title_only(path):
    im=Image.open('tmp/title_fonte.png').copy(); ImageDraw.Draw(im).rectangle((0,435,W,485),fill=(0,0,0,0)); im.save(path)
title_png('tmp/title_fonte.png'); title_only('tmp/title.png')
def card_png(nome,num,path,tip=(80,500)):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    f1=fnt('pjs800',46); f2=fnt('Anton-Regular',120); f3=fnt('pjs800',40)
    w=max(d.textlength(nome,font=f1), d.textlength(num,font=f2)+d.textlength(' por dia',font=f3))+60
    x0=max(30,tip[0]-50); y0=tip[1]-25-230
    d.rounded_rectangle((x0,y0,x0+w,y0+230),26,fill=(8,8,8,225),outline=LM,width=4)
    d.text((x0+30,y0+22),nome,font=f1,fill=(255,255,255))
    d.text((x0+30,y0+72),num,font=f2,fill=LM)
    d.text((x0+40+d.textlength(num,font=f2),y0+150),'por dia',font=f3,fill=(230,230,230))
    # seta apontando pro dedo (canto de cima)
    d.polygon([(tip[0]-22,y0+230),(tip[0],y0+256),(tip[0]+22,y0+230)],fill=LM)
    im.save(path)
CARDS=[('Primo Rico','3',0.22,2.5,(80,500)),('Hormozi','3',2.74,4.6,(60,495)),('Pedro Quintanilha','3',4.88,6.9,(96,675)),('Joel Jota','2,7',7.18,11.3,(210,900))]
inputs=['-i','tmp/base.mp4','-i','tmp/title_fonte.png','-i','tmp/title.png']
chain='[0:v][1:v]overlay=0:0:enable=\'between(t,0,13.6)\'[v1];[v1][2:v]overlay=0:0:enable=\'gt(t,13.6)\'[v2]'
last='v2'
for j,(nome,num,a0,a1,tp) in enumerate(CARDS):
    p=f'tmp/card{j}.png'; card_png(nome,num,p,tp); inputs+=['-i',p]
    idx=len(inputs)//2-1
    chain+=f";[{last}][{idx}:v]overlay=0:0:enable='between(t,{a0},{a1})'[k{j}]"; last=f'k{j}'
for k,(s,e,c) in enumerate(caps):
    p=f'tmp/c{k}.png'; caption_png(c,p); inputs+=['-i',p]
    chain+=f";[{last}][{len(inputs)//2-1}:v]overlay=0:0:enable='between(t,{s:.2f},{e:.2f})'[w{k}]"; last=f'w{k}'
subprocess.run(['ffmpeg','-v','error','-y',*inputs,'-filter_complex',chain,'-map',f'[{last}]','-map','0:a','-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart','r01-os-grandes-postam-3.mp4'],check=True)
print('total',round(TOTAL,2),'legendas',len(caps))
