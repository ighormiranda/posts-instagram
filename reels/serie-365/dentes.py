"""Clareia levemente os dentes num vídeo (MediaPipe Face Mesh, boca por dentro).
Uso: python3 dentes.py entrada.mp4 saida.mp4"""
import sys, subprocess, numpy as np, cv2, dlib
src,dst=sys.argv[1],sys.argv[2]
W,H=1080,1920
fps=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip()
dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',fps,'-i','-','-i',src,'-map','0:v','-map','1:a?',
    '-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','copy',dst],stdin=subprocess.PIPE)
det=dlib.get_frontal_face_detector(); sp=dlib.shape_predictor('/home/claude/models/shape_predictor_68_face_landmarks.dat'); box=None
n=0
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    img=np.frombuffer(buf,np.uint8).reshape(H,W,3).copy()
    if n%3==0 or box is None:
        sm=cv2.resize(img,(W//4,H//4)); g=cv2.cvtColor(sm,cv2.COLOR_BGR2GRAY)
        ds=det(g,0)
        if ds:
            d0=max(ds,key=lambda r:r.area()); box=dlib.rectangle(d0.left()*4,d0.top()*4,d0.right()*4,d0.bottom()*4)
    if box is not None:
        sh=sp(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),box)
        pts=np.array([[sh.part(i).x,sh.part(i).y] for i in range(60,68)],np.int32)
        mask=np.zeros((H,W),np.uint8); cv2.fillPoly(mask,[pts],255)
        x,y,w,h=cv2.boundingRect(pts)
        if w>10 and h>4:
            x0,y0,x1,y1=max(0,x-4),max(0,y-4),min(W,x+w+4),min(H,y+h+4)
            roi=img[y0:y1,x0:x1]; m=mask[y0:y1,x0:x1]
            hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV).astype(np.float32)
            # dente: claro e amarelado (matiz 8-40 no OpenCV), não lábio vermelho/escuro
            teeth=(m>0)&(hsv[...,2]>95)&(hsv[...,0]>=8)&(hsv[...,0]<=40)
            k=cv2.GaussianBlur(teeth.astype(np.float32),(7,7),0)
            hsv[...,1]=hsv[...,1]*(1-0.7*k)
            hsv[...,2]=np.clip(hsv[...,2]*(1+0.14*k),0,255)
            img[y0:y1,x0:x1]=cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2BGR)
    enc.stdin.write(img.tobytes()); n+=1
enc.stdin.close(); enc.wait(); print('frames',n)
