import subprocess, os
from PIL import Image, ImageDraw, ImageFont
SRC='/mnt/user-data/uploads/IMG_4570.mov'
F='/home/claude/posts-instagram/ferramentas/fonts/'; W,H=1080,1920; LM=(154,224,76)
fnt=lambda n,s: ImageFont.truetype(F+n+'.ttf',s)
cuts=[(56.5,71.2,[(0.3,4.5,'A gente já sabe'),(4.5,7.5,'o que *não pode.*'),(7.5,11,'*Esse pode,* esse o papai deixa.'),(11,14.7,'Esse o papai *não deixa.*')]),
      (85.5,90.0,[(0.2,4.4,'Esse aí o papai *não deixa.*')]),
      (115.5,119.8,[(0.2,4.2,'*Uhul!*')])]
os.makedirs('tmp',exist_ok=True); parts=[];caps=[];t0=0
for i,(a,b,cs) in enumerate(cuts):
    o=f'tmp/p{i}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',SRC,'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1','-af','loudnorm=I=-15:TP=-1.5:LRA=11','-ar','44100','-ac','2','-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','-b:a','160k',o],check=True)
    parts.append(o); caps+=[(t0+s,t0+e,c) for s,e,c in cs]; t0+=b-a
# cartão final: último quadro escurecido, 4 s
subprocess.run(['ffmpeg','-v','error','-y','-sseof','-0.1','-i','tmp/p2.mp4','-frames:v','1','tmp/last.png'],check=True)
im=Image.open('tmp/last.png').convert('RGB'); im=Image.blend(im,Image.new('RGB',im.size,(4,4,4)),0.72); d=ImageDraw.Draw(im)
def block(d,txt,y,f,lh):
    for line in txt.split('\n'):
        x=90; dest=False
        for k,p in enumerate(line.split('*')):
            if p: d.text((x,y),p,font=f,fill=LM if k%2 else (255,255,255)); x+=d.textlength(p,font=f)
        y+=lh
    return y
y=block(d,'Toda IA no WhatsApp\nprecisa disso:',560,fnt('pjs800',72),86)
y=block(d,'saber o que *pode*\ne o que *não pode*\nresponder.',y+30,fnt('Anton-Regular',112),122)
f=fnt('pjs800',50); t='Segue pra aprender a montar a sua'; tw=d.textlength(t,font=f)
d.rounded_rectangle((90,y+60,90+tw+60,y+160),24,fill=LM); d.text((120,y+80),t,font=f,fill=(8,8,8))
im.save('tmp/end.png')
subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-t','4','-i','tmp/end.png','-f','lavfi','-t','4','-i','anullsrc=r=44100:cl=stereo','-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','-b:a','160k','-shortest','tmp/p3.mp4'],check=True)
parts.append('tmp/p3.mp4')
with open('tmp/list.txt','w') as fl:
    for p in parts: fl.write(f"file '{os.path.abspath(p)}'\n")
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','tmp/list.txt','-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','tmp/base.mp4'],check=True)
def cap(txt,path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',74)
    sg=[(p,k%2==1) for k,p in enumerate(txt.split('*')) if p]; tw=sum(d.textlength(p,font=f) for p,_ in sg)
    if tw>960: f=fnt('pjs800',int(74*960/tw)); tw=sum(d.textlength(p,font=f) for p,_ in sg)
    x=(W-tw)/2
    for p,ds in sg: d.text((x,1370),p,font=f,fill=LM if ds else (255,255,255),stroke_width=7,stroke_fill=(0,0,0)); x+=d.textlength(p,font=f)
    im.save(path)
def title(path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',50)
    L=['O que a Flora já entendeu','e muita empresa não']; ws=[d.textlength(l,font=f) for l in L]; bw=max(ws)+70; x0=(W-bw)/2
    d.rounded_rectangle((x0,250,x0+bw,422),22,fill=(255,255,255,240))
    for k,l in enumerate(L): d.text((x0+(bw-ws[k])/2,270+k*64),l,font=f,fill=(10,10,10))
    im.save(path)
title('tmp/t.png'); inp=['-i','tmp/base.mp4','-i','tmp/t.png']; chain=f"[0:v][1:v]overlay=0:0:enable='lt(t,{t0:.2f})'[v1]"; last='v1'
for k,(a,b,c) in enumerate(caps):
    p=f'tmp/c{k}.png'; cap(c,p); inp+=['-i',p]; idx=len(inp)//2-1
    chain+=f";[{last}][{idx}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[c{k}]"; last=f'c{k}'
subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',chain,'-map',f'[{last}]','-map','0:a','-c:v','libx264','-preset','slow','-crf','23','-maxrate','6M','-bufsize','12M','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart','r04-flora-pode-nao-pode.mp4'],check=True)
print('total',t0+4)
