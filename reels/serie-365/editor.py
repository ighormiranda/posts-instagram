"""Editor genérico dos Reels gravados: cortes pela fala, legenda, título, cards e dentes.
build(pecas, titulo, saida, cards=[], rodape=None)
pecas: [(arquivo, texto_com_*destaque*)]  (corta do início ao fim da fala de cada arquivo)
cards: [(indice_da_peca, png_path)] mostra o PNG durante a peça"""
import subprocess, os, wave, numpy as np
from PIL import Image, ImageDraw, ImageFont
F='/home/claude/posts-instagram/ferramentas/fonts/'; W,H=1080,1920; LM=(154,224,76)
fnt=lambda n,s: ImageFont.truetype(F+n+'.ttf',s)
DENTES=os.path.join(os.path.dirname(os.path.abspath(__file__)),'dentes.py')
def fala(path):
    subprocess.run(['ffmpeg','-v','error','-y','-i',path,'-ac','1','-ar','16000','tmp/w.wav'],check=True)
    w=wave.open('tmp/w.wav'); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)
    hop=160; fr=np.array([np.sqrt(np.mean(x[i:i+hop]**2)) for i in range(0,len(x)-hop,hop)])
    thr=max(np.percentile(fr,95)*0.15,200); idx=np.where(fr>thr)[0]
    dur=len(x)/16000
    if len(idx)==0: return 0,dur
    return max(0,idx[0]*hop/16000-0.12), min(dur,idx[-1]*hop/16000+0.2)
def segs(t):
    out,d=[],False
    for p in t.split('*'):
        if p: out.append((p,d))
        d=not d
    return out
def chunks(tx):
    words=tx.split(' '); ch=[];cur=[]
    for w in words:
        cur.append(w)
        if len(cur)==3 or w.endswith(('.',',','?')): ch.append(' '.join(cur));cur=[]
    if cur: ch.append(' '.join(cur))
    dest=False;out=[]
    for c in ch:
        pre='*' if dest else ''
        if c.count('*')%2: dest=not dest
        out.append(pre+c+('*' if dest else ''))
    return out
def cap_png(txt,path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',72)
    sg=segs(txt); tw=sum(d.textlength(p,font=f) for p,_ in sg)
    if tw>960: f=fnt('pjs800',int(72*960/tw)); tw=sum(d.textlength(p,font=f) for p,_ in sg)
    x=(W-tw)/2
    for p,ds in sg: d.text((x,1370),p,font=f,fill=LM if ds else (255,255,255),stroke_width=7,stroke_fill=(0,0,0)); x+=d.textlength(p,font=f)
    im.save(path)
def title_png(lines,path,pos='center'):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs800',50)
    ws=[d.textlength(l,font=f) for l in lines]; bw=max(ws)+70; x0=(W-bw)/2 if pos=='center' else W-40-bw
    d.rounded_rectangle((x0,250,x0+bw,250+len(lines)*64+44),22,fill=(255,255,255,240))
    for k,l in enumerate(lines): d.text((x0+(bw-ws[k])/2,270+k*64),l,font=f,fill=(10,10,10))
    im.save(path)
def rodape_png(txt,path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=fnt('pjs500',28)
    tw=d.textlength(txt,font=f); d.text(((W-tw)/2,1490),txt,font=f,fill=(235,235,235),stroke_width=3,stroke_fill=(0,0,0)); im.save(path)
def build(pecas,titulo,saida,cards=[],rodape=None,titulo_pos='center'):
    os.makedirs('tmp',exist_ok=True); parts=[];caps=[];spans=[];t0=0
    for i,(path,tx) in enumerate(pecas):
        a,b=fala(path); o=f'tmp/p{i}.mp4'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-to',f'{b:.3f}','-i',path,'-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1','-af','loudnorm=I=-15:TP=-1.5:LRA=11','-ar','44100','-ac','2','-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','-b:a','160k',o],check=True)
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',o],capture_output=True,text=True).stdout)
        ch=chunks(tx); tot=sum(len(c.replace('*','')) for c in ch); tt=t0+0.08
        for c in ch:
            dd=(d-0.25)*len(c.replace('*',''))/tot; caps.append((tt,tt+dd,c)); tt+=dd
        parts.append(o); spans.append((t0,t0+d)); t0+=d
    with open('tmp/list.txt','w') as f:
        for p in parts: f.write(f"file '{os.path.abspath(p)}'\n")
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','tmp/list.txt','-c','copy','tmp/base0.mp4'],check=True)
    subprocess.run(['python3',DENTES,'tmp/base0.mp4','tmp/base.mp4'],check=True)
    title_png(titulo,'tmp/t.png',titulo_pos); inp=['-i','tmp/base.mp4','-i','tmp/t.png']; chain='[0:v][1:v]overlay=0:0[v1]'; last='v1'
    def add(png,a,b,tag):
        nonlocal chain,last
        inp.extend(['-i',png]); idx=len(inp)//2-1
        chain+=f";[{last}][{idx}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[{tag}]"; last=tag
    for j,(k,png) in enumerate(cards): add(png,spans[k][0],spans[k][1],f'k{j}')
    if rodape: rodape_png(rodape[0],'tmp/rod.png'); add('tmp/rod.png',spans[rodape[1]][0],t0,'rod')
    for k,(a,b,c) in enumerate(caps):
        p=f'tmp/c{k}.png'; cap_png(c,p); add(p,a,b,f'c{k}')
    subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',chain,'-map',f'[{last}]','-map','0:a','-c:v','libx264','-preset','slow','-crf','23','-maxrate','6M','-bufsize','12M','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',saida],check=True)
    return t0
