import cv2,numpy as np,sys,subprocess
casc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
state={'box':None,'miss':0}
def whiten(im):
    g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY); s=cv2.resize(g,None,fx=0.25,fy=0.25)
    f=casc.detectMultiScale(s,1.1,5,minSize=(60,60))
    if len(f)==0:
        state['miss']+=1
    if len(f):
        state['miss']=0
        b=max(f,key=lambda r:r[2])*4
        state['box']=b if state['box'] is None else (0.6*np.array(state['box'])+0.4*b)
    if state['box'] is None or state['miss']>8: return im
    x,y,w,h=[int(v) for v in state['box']]
    y0,y1,x0,x1=y+int(h*0.62),min(im.shape[0],y+int(h*1.0)),max(0,x+int(w*0.18)),min(im.shape[1],x+int(w*0.82))
    roi=im[y0:y1,x0:x1]
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV).astype(np.float32)
    H,S,V=hsv[...,0],hsv[...,1],hsv[...,2]
    m=((H>=11)&(H<=38)&(S<95)&(V>140)).astype(np.float32)
    hh,ww=m.shape
    ell=np.zeros((hh,ww),np.uint8); cv2.ellipse(ell,(ww//2,int(hh*0.36)),(int(ww*0.27),int(hh*0.24)),0,0,360,1,-1)
    m=m*ell
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3)))
    n,lab,st,_=cv2.connectedComponentsWithStats((m>0).astype(np.uint8))
    keep=np.zeros(n,bool); keep[1:]=st[1:,cv2.CC_STAT_AREA]>=80
    m=(keep[lab]).astype(np.float32)
    m=cv2.GaussianBlur(m,(0,0),2.5)
    S2=S*(1-0.55*m); V2=np.minimum(255,V*(1+0.07*m))
    hsv[...,1]=S2; hsv[...,2]=V2
    im[y0:y1,x0:x1]=cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2BGR)
    return im
if __name__=='__main__':
    src,dst=sys.argv[1],sys.argv[2]
    skip_from=float(sys.argv[3]) if len(sys.argv)>3 else 1e9
    W,H=1080,1920
    dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-i',src,'-map','0:v','-map','1:a','-c:v','libx264','-crf','21','-preset','medium','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',dst],stdin=subprocess.PIPE)
    n=W*H*3; k=0
    while True:
        b=dec.stdout.read(n)
        if len(b)<n: break
        fr=np.frombuffer(b,np.uint8).reshape(H,W,3).copy()
        enc.stdin.write((fr if k/30>=skip_from else whiten(fr)).tobytes()); k+=1
    enc.stdin.close(); enc.wait()
