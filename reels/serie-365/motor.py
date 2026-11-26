"""Motor dos Reels da série 1/365: cenas com foto/fundo, Ken Burns, texto animado e selo DIA X/365.
Gera mp4 1080x1920 30fps via ffmpeg (sem áudio)."""
import subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
F='/home/claude/posts-instagram/ferramentas/fonts/'
W,H,FPS=1080,1920,30
fnt=lambda n,s: ImageFont.truetype(F+n+'.ttf',s)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3

def load_bg(path,crop=None,zoom_to=1.12):
    im=ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    if crop: im=im.crop(crop)
    # cobre 1080x1920 com folga para o zoom
    base=ImageOps.fit(im,(int(W*zoom_to)+4,int(H*zoom_to)+4),centering=(0.5,0.4))
    return base

def kb_frame(base,t,zoom_to=1.12,pan=(0,0)):
    z=1+(zoom_to-1)*t
    bw,bh=base.size
    cw,ch=int(W*zoom_to/z),int(H*zoom_to/z)
    cx=(bw-cw)/2+pan[0]*t; cy=(bh-ch)/2+pan[1]*t
    cx=max(0,min(bw-cw,cx)); cy=max(0,min(bh-ch,cy))
    return base.crop((int(cx),int(cy),int(cx)+cw,int(cy)+ch)).resize((W,H),Image.BILINEAR)

def shade(im,top=0.55,bot=0.85,col=(4,4,4)):
    g=Image.new('L',(1,H))
    for y in range(H):
        a=0
        if y<H*0.35: a=top*(1-y/(H*0.35))
        if y>H*0.36: a=max(a,bot*min(1,(y-H*0.36)/(H*0.22)))
        g.putpixel((0,y),int(255*min(1,a)))
    return Image.composite(Image.new('RGB',(W,H),col),im,g.resize((W,H)))

def segs(t):
    out,d=[],False
    for p in t.split('*'):
        if p: out.append((p,d))
        d=not d
    return out

def wrap(d,text,f,maxw):
    """retorna linhas de [(palavra,dest)]"""
    lines=[]
    for raw in text.split('\n'):
        cur=[];w=0
        for chunk,dest in segs(raw):
            for word in chunk.split(' '):
                if not word: continue
                ww=d.textlength(word+' ',font=f)
                if cur and w+ww>maxw: lines.append(cur);cur=[];w=0
                cur.append((word,dest));w+=ww
        lines.append(cur)
    return lines

def draw_block(img,text,y,t,fname='Anton-Regular',size=130,cor=(254,254,254),dest=(154,224,76),x=90,maxw=840,lh=1.05,align='left',stagger=0.12,box=None):
    """desenha bloco de texto com entrada linha a linha (t = segundos desde o início do bloco)"""
    d=ImageDraw.Draw(img); f=fnt(fname,size)
    lines=wrap(d,text,f,maxw)
    for i,ln in enumerate(lines):
        p=ease((t-i*stagger)/0.35)
        if p<=0: continue
        layer=Image.new('RGBA',(W,int(size*1.5)),(0,0,0,0)); ld=ImageDraw.Draw(layer)
        tw=sum(ld.textlength(w+' ',font=f) for w,_ in ln)-ld.textlength(' ',font=f)
        xx=x if align=='left' else (W-tw)/2
        if box:
            ld.rounded_rectangle((xx-22,int(size*0.08),xx+tw+22,int(size*1.28)),14,fill=box)
        for w,ds in ln:
            ld.text((xx,0),w,font=f,fill=dest if ds else cor)
            xx+=ld.textlength(w+' ',font=f)
        if p<1:
            a=layer.split()[3].point(lambda v:int(v*p)); layer.putalpha(a)
        img.paste(layer,(0,int(y+i*size*lh+(1-p)*40)),layer)
    return y+len(lines)*size*lh

def selo(img,dia,cor=(154,224,76)):
    d=ImageDraw.Draw(img); f=fnt('mono500',34)
    txt=f'DIA {dia}/365'; tw=d.textlength(txt,font=f)
    d.rounded_rectangle((90,170,90+tw+44,234),32,fill=(4,4,4))
    d.ellipse((108,193,124,209),fill=cor)
    d.text((134,180),txt,font=f,fill=(254,254,254))

def handle(img):
    d=ImageDraw.Draw(img); f=fnt('mono500',30); t='@o.ighormiranda'
    d.text(((W-d.textlength(t,font=f))/2,1560),t,font=f,fill=(230,230,230))

def render(cenas,out,dia,cor_selo=(154,224,76)):
    """cenas: lista de dicts {dur, bg(callable t->Image), draw(callable img,t)}"""
    total=sum(c['dur'] for c in cenas)
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest',
        '-c:v','libx264','-pix_fmt','yuv420p','-preset','medium','-crf','20','-c:a','aac','-b:a','96k','-movflags','+faststart',out],stdin=subprocess.PIPE)
    prev=None
    for ci,c in enumerate(cenas):
        n=int(c['dur']*FPS)
        for k in range(n):
            t=k/FPS
            img=c['bg'](t/c['dur']).convert('RGB')
            c['draw'](img,t)
            selo(img,dia,cor_selo); handle(img)
            # transição: fade da cena anterior nos 6 primeiros frames
            if prev is not None and k<6:
                img=Image.blend(prev,img,(k+1)/6)
            p.stdin.write(img.tobytes())
            last=img
        prev=last
    p.stdin.close(); p.wait()
    return total
