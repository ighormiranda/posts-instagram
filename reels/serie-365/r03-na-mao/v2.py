import subprocess, os, numpy as np, wave
from PIL import Image, ImageDraw, ImageFont
U='/mnt/user-data/uploads/'; A='/mnt/user-data/attachments/6b783e31-48d9-5fd3-b925-355c9d9bd392/'
CL={'4555':(A+'38f3f6b7-IMG_4555.mov',45.04),'4556':(U+'IMG_4556.mov',54.325313),'4558':(U+'IMG_4558.mov',144.618689)}
# (clipe, início global, fim global, legenda)
P=[('4555',2.07,2.99,'*Carrossel.*'),('4555',4.08,6.14,'Agendamento de *reunião.*'),
   ('4558',13.53,14.85,'Agenda do *mês inteiro.*'),('4558',22.64,24.52,'Resposta no WhatsApp *de madrugada.*'),
   ('4558',29.06,30.26,'Resumo de *reunião.*'),('4558',36.08,37.51,'Proposta *comercial.*'),
   ('4556',29.90,31.06,'Planilha de *orçamento.*'),('4558',41.33,42.50,'Roteiro de *Reels.*'),
   ('4558',46.69,48.00,'Página de *vendas.*'),('4558',53.95,55.31,'E o site *da empresa.*'),
   ('4558',56.88,60.16,'Hoje a IA faz tudo isso pra mim e *eu só aprovo.*'),
   ('4558',60.79,64.42,'Se você quer aprender a fazer isso também, *me segue, eu vou te ensinar.*')]
os.makedirs('tmp',exist_ok=True)
def speech(path,a,b):
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',path,'-ac','1','-ar','16000','tmp/w.wav'],check=True)
    w=wave.open('tmp/w.wav'); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)
    win=320; e=np.sqrt(np.convolve(x**2,np.ones(win)/win,'same'))
    thr=max(e.max()*0.12,300); idx=np.where(e>thr)[0]
    if len(idx)==0: return a,b
    return a+max(0,idx[0]/16000-0.12), a+min(len(x)/16000,idx[-1]/16000+0.18)
parts=[];caps=[];t0=0
for i,(c,gs,ge,tx) in enumerate(P):
    path,off=CL[c]; a,b=gs,ge
    out=f'tmp/p{i}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-to',f'{b:.3f}','-i',path,'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1',
        '-af','loudnorm=I=-15:TP=-1.5:LRA=11','-ar','44100','-ac','2','-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','-b:a','160k',out],check=True)
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],capture_output=True,text=True).stdout)
    parts.append(out)
    words=tx.split(' ')
    if len(words)<=5: caps.append((t0,t0+d,tx))
    else:
        chunks=[];cur=[]
        for w in words:
            cur.append(w)
            if len(cur)==3 or w.endswith(('.',',')): chunks.append(' '.join(cur));cur=[]
        if cur: chunks.append(' '.join(cur))
        dest=False;fixed=[]
        for ch in chunks:
            pre='*' if dest else ''
            if ch.count('*')%2: dest=not dest
            fixed.append(pre+ch+('*' if dest else ''))
        tot=sum(len(x.replace('*','')) for x in fixed); tt=t0
        for ch in fixed:
            dd=d*len(ch.replace('*',''))/tot; caps.append((tt,tt+dd,ch)); tt+=dd
    print(i,c,round(a,2),round(b,2),round(d,2))
    t0+=d
with open('tmp/list.txt','w') as f:
    for p in parts: f.write(f"file '{os.path.abspath(p)}'\n")
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','tmp/list.txt','-c','copy','tmp/base0.mp4'],check=True)
subprocess.run(['python3','../dentes.py','tmp/base0.mp4','tmp/base.mp4'],check=True)
F='/home/claude/posts-instagram/ferramentas/fonts/'; W,H=1080,1920; LM=(154,224,76)
fnt=lambda n,s: ImageFont.truetype(F+n+'.ttf',s)
def segs(t):
    out,d=[],False
    for p in t.split('*'):
        if p: out.append((p,d))
        d=not d
    return out
def cap(txt,path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',70)
    sg=segs(txt); tw=sum(d.textlength(p,font=f) for p,_ in sg)
    if tw>980:
        f=fnt('pjs800',int(70*980/tw)); tw=sum(d.textlength(p,font=f) for p,_ in sg)
    x=(W-tw)/2
    for p,ds in sg:
        d.text((x,1370),p,font=f,fill=LM if ds else (255,255,255),stroke_width=7,stroke_fill=(0,0,0)); x+=d.textlength(p,font=f)
    im.save(path)
def title(path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',50)
    L=['10 coisas que eu não','faço mais na mão']; ws=[d.textlength(l,font=f) for l in L]; bw=max(ws)+70
    x0=(W-bw)/2; d.rounded_rectangle((x0,250,x0+bw,422),22,fill=(255,255,255,240))
    for k,l in enumerate(L): d.text((x0+(bw-ws[k])/2,270+k*64),l,font=f,fill=(10,10,10))
    im.save(path)
# contador 1..10 nos itens
def cont(n,path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('Anton-Regular',64)
    t=f'{n}/10'; tw=d.textlength(t,font=f)
    d.rounded_rectangle((W-60-tw-40,450,W-60,540),20,fill=LM); d.text((W-80-tw,456),t,font=f,fill=(8,8,8)); im.save(path)
title('tmp/title.png')
inp=['-i','tmp/base.mp4','-i','tmp/title.png']; chain='[0:v][1:v]overlay=0:0[v1]'; last='v1'
# contador: item k (0=carrossel+agendamento => 1 e 2)
acc=0; starts=[]
for p in parts:
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout); starts.append((acc,acc+d)); acc+=d
marks=[(starts[k][0],starts[k][1],k+1) for k in range(10)]
for j,(a,b,n) in enumerate(marks):
    p=f'tmp/n{j}.png'; cont(n,p); inp+=['-i',p]; idx=len(inp)//2-1
    chain+=f";[{last}][{idx}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[n{j}]"; last=f'n{j}'
for k,(a,b,c) in enumerate(caps):
    p=f'tmp/c{k}.png'; cap(c,p); inp+=['-i',p]; idx=len(inp)//2-1
    chain+=f";[{last}][{idx}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[c{k}]"; last=f'c{k}'
subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',chain,'-map',f'[{last}]','-map','0:a','-c:v','libx264','-preset','slow','-crf','23','-maxrate','6M','-bufsize','12M','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart','r03-nao-faco-mais-na-mao.mp4'],check=True)
print('total',round(acc,2))
