import json,subprocess,glob
A='/mnt/user-data/attachments/6b783e31-48d9-5fd3-b925-355c9d9bd392/'
FONTS='/home/claude/posts-instagram/ferramentas/fonts'
def ts(x): h=int(x//3600); m=int(x%3600//60); s=x%60; return f'{h}:{m:02d}:{s:05.2f}'
def build(W,order,fix,title,hook,hl,broll,out,tokfix=None):
    words=[];segs=[];t=0;starts={}
    for n in order:
        d=json.load(open(f'{W}/IMG_{n}.json'))['chunks']
        src=glob.glob(A+f'*IMG_{n}.mov')[0]
        dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src]))
        s=max(0,d[0]['timestamp'][0]-0.12); e=min(dur,(d[-1]['timestamp'][1] or dur)+0.25)
        segs.append((src,s,e)); starts[n]=(t,t+e-s)
        for i,c in enumerate(d):
            w=c['text'].strip(); w=fix.get(n,{}).get(w,w)
            if tokfix and (n,i) in tokfix: w=tokfix[(n,i)]
            if w: words.append((t+c['timestamp'][0]-s, min(t+e-s,t+(c['timestamp'][1] or e)-s), w))
        t+=e-s
    fc=[]
    for i,(src,s,e) in enumerate(segs):
        fc.append(f'[{i}:v]trim={s}:{e},setpts=PTS-STARTPTS,scale=1080:1920,fps=30[v{i}];[{i}:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={e-s-0.04}:d=0.04[a{i}]')
    fc.append(''.join(f'[v{i}][a{i}]' for i in range(len(segs)))+f'concat=n={len(segs)}:v=1:a=1[v0][a]')
    inputs=[s[0] for s in segs]; cur='v0'
    for j,b in enumerate(broll):
        a0,a1=starts[b['clip']]; a0+=b.get('off',0); D=a1-a0
        k=len(inputs); 
        if b['type']=='img':
            inputs+=['IMG:'+b['src']]
            fc.append(f"[{k}:v]scale=672:1100,zoompan=z='1+0.05*on/({int(D*30)})':x='iw/2-(iw/zoom/2)':y='ih/3-(ih/zoom/3)':d={int(D*30)+1}:s=672x1100:fps=30,setsar=1,pad=1080:1920:204:220:color=0x0A0A0A,trim=0:{D},setpts=PTS-STARTPTS+{a0}/TB[b{j}]")
        else:
            inputs+=[b['src']]; L=b['end']-b['start']
            fc.append(f"[{k}:v]trim={b['start']}:{b['end']},setpts=(PTS-STARTPTS)*{D/L},fps=30,crop=1080:1140:0:420,pad=1080:1920:0:220:color=0x0A0A0A,setsar=1,setpts=PTS+{a0}/TB[b{j}]")
        fc.append(f"[{cur}][b{j}]overlay=0:0:eof_action=pass:enable='between(t,{a0},{a1})'[o{j}]"); cur=f'o{j}'
    ass=['[Script Info]','PlayResX: 1080','PlayResY: 1920','ScaledBorderAndShadow: yes','','[V4+ Styles]',
    'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
    'Style: Cap,Plus Jakarta Sans ExtraBold,82,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,6,2,2,80,80,480,1',
    'Style: Tit,IBM Plex Mono Medium,40,&H004CE09A,&H004CE09A,&H00000000,&HB4000000,0,0,0,0,100,100,6,0,3,18,0,8,60,60,110,1',
    'Style: Hook,Plus Jakarta Sans ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&HC8040404,0,0,0,0,100,100,0,0,3,26,0,8,90,90,230,1',
    '','[Events]','Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    ass.append(f'Dialogue: 0,{ts(0)},{ts(t)},Tit,,0,0,0,,{title}')
    ass.append(f'Dialogue: 0,{ts(0)},{ts(3.0)},Hook,,0,0,0,,{hook}')
    g=[]
    for i,wd in enumerate(words):
        g.append(wd)
        if wd[2][-1] in '.,?%' or len(g)==3 or i==len(words)-1:
            a=g[0][0]; b=words[i+1][0] if i+1<len(words) else t; b=min(b,g[-1][1]+0.5)
            txt=' '.join(('{\\c&H4CE09A&}'+w+'{\\c&HFFFFFF&}') if w.lower().strip('.,?') in hl else w for _,_,w in g)
            ass.append(f'Dialogue: 1,{ts(a)},{ts(b)},Cap,,0,0,0,,{txt}'); g=[]
    open(out+'.ass','w').write('\n'.join(ass))
    fc.append(f"[{cur}]ass={out}.ass:fontsdir={FONTS}[vo];[a]loudnorm=I=-14:TP=-1.5[ao]")
    cmd=['ffmpeg','-v','error','-y']
    for x in inputs:
        cmd+= (['-loop','1','-i',x[4:]] if x.startswith('IMG:') else ['-i',x])
    cmd+=['-filter_complex',';'.join(fc),'-map','[vo]','-map','[ao]','-t',str(t),'-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-movflags','+faststart',out]
    subprocess.run(cmd,check=True); print('dur',t); print(' '.join(w for _,_,w in words))
