import sys;sys.path.insert(0,'/root/mesa/tools');import montar
S='/home/claude/posts-instagram/2026-11-semana-07/'
P='/mnt/user-data/attachments/6b783e31-48d9-5fd3-b925-355c9d9bd392/'
which=sys.argv[1]
if which=='2':
  montar.build('/root/mesa/ep2',['4350','4351','4355','4356','4357','4359','4360','4361'],
   {'4360':{'incomodo':'incomodou','incomodo.':'incomodou.'},'4357':{'depois':'Depois'}},
   'DIÁRIO DA MÁQUINA · EP. 2','{\\c&H4CE09A&}+393%{\\c&HFFFFFF&}\\NNOS PRIMEIROS 30 DIAS',
   {'+393%','6','outubro','viral,','dia,','detalhe','amanhã','amanhã.'},
   [{'clip':'4355','type':'img','src':'/home/claude/posts-instagram/ofertas/black-november/lp/print-painel-ig.jpg'},
    {'clip':'4356','type':'vid','src':'/root/mesa/ep2/lp/lp.webm','start':6.0,'end':9.5},
    {'clip':'4357','type':'vid','src':'/root/mesa/ep2/lp/lp.webm','start':9.5,'end':18.5}],
   '/root/mesa/ep2/ep2b.mp4',tokfix={('4351',0):'Foi',('4351',1):'o quanto',('4350',0):'+393%.',('4350',1):''})
if which=='3':
  montar.build('/root/mesa/ep3',[str(n) for n in range(4378,4396)],{},
   'DIÁRIO DA MÁQUINA · EP. 3','MUITA GENTE VIU.\\N{\\c&H4CE09A&}QUASE NINGUÉM SEGUIU.{\\c&HFFFFFF&}',
   {'393%.','88%','nova,','dica.','história.','1.919','10','lembrado.','compra.','amanhã'},
   [{'clip':'4380','type':'img','src':P+'e063b9be-image.png'}],
   '/root/mesa/ep3/ep3.mp4',tokfix={('4378',5):'393%.',('4378',6):'',('4380',5):'88%',('4380',6):'',('4389',3):'1.919',('4389',4):'',('4381',0):'',('4381',1):'Gente'})
if which=='4':
  montar.build('/root/mesa/ep4',['4397','4402','4403','4404','4407'],{},
   'DIÁRIO DA MÁQUINA · EP. 4','EU TESTEI EM MIM\\N{\\c&H4CE09A&}ANTES DE VENDER.{\\c&HFFFFFF&}',
   {'30','vendido.','tempo.','aprovar,','lembrado.','cinco','amanhã','carrinho'},
   [{'clip':'4403','type':'img','src':S+'s7c21_slide01.jpg','dur':7}],
   '/root/mesa/ep4/ep4.mp4',
   tokfix={('4402',15):'postando,',('4403',2):'faz',('4403',4):'carrosséis,',('4403',6):'Reels,',('4403',8):'stories,',('4403',9):'automatiza',('4403',42):'Reels,',('4403',76):'tripezinho',('4403',91):'Reels'})
if which=='4b':
  F='/home/claude/posts-instagram/fotos/'; R='/home/claude/posts-instagram/reels/'
  montar.build('/root/mesa/ep4',['4397','4402','4403','4404','4407'],{},
   'DIÁRIO DA MÁQUINA · EP. 4','EU TESTEI EM MIM\\N{\\c&H4CE09A&}ANTES DE VENDER.{\\c&HFFFFFF&}',
   {'30','vendido.','tempo.','aprovar,','lembrado.','cinco','amanhã','carrinho'},
   [{'clip':'4403','type':'img','src':S+'s7c21_slide01.jpg','off':0.9,'dur':1.4},
    {'clip':'4403','type':'vid','src':R+'trend-missao/missao-empresario.mp4','start':8,'end':10,'off':2.3,'dur':0.9},
    {'clip':'4403','type':'img','src':'/home/claude/posts-instagram/stories/2026-11-avulsos/missao-personagem.jpg','off':3.2,'dur':3.6},
    {'clip':'4403','type':'img','src':F+'estudio-blazer-marinho/sorrindo-tres-quartos.jpg','off':9.6,'dur':2.8},
    {'clip':'4403','type':'img','src':F+'evento-makers/conversa-cracha.jpg','off':12.4,'dur':3.4},
    {'clip':'4403','type':'vid','src':R+'diario-da-maquina/ep01.mp4','start':8,'end':12,'off':16.0,'dur':3.6},
    {'clip':'4403','type':'vid','src':R+'trend-missao/missao-empresario.mp4','start':4,'end':12,'off':30.0,'dur':2.6}],
   '/root/mesa/ep4/ep4.mp4',
   tokfix={('4402',15):'postando,',('4403',2):'faz',('4403',4):'carrosséis,',('4403',6):'Reels,',('4403',8):'stories,',('4403',9):'automatiza',('4403',42):'Reels,',('4403',76):'tripezinho',('4403',91):'Reels'})
if which=='5':
  montar.build('/root/mesa/ep5',['4408','4409','4411','4412','4415','4417','4418','4427','4420','4428','4429'],{},
   'DIÁRIO DA MÁQUINA · EP. 5 · ABRIU','TODO MUNDO VAI TE\\N{\\c&H4CE09A&}DAR DESCONTO.{\\c&HFFFFFF&}',
   {'audiência.','empresa.','dia.','amostra','30','black.','primeiro.','vaga','figurinhas'},
   [{'clip':'4417','type':'img','src':S+'s7c24_slide01.jpg'}],
   '/root/mesa/ep5/ep5.mp4',
   tokfix={('4412',0):'Carrossel,',('4412',1):'',('4412',2):'Reels,',('4412',3):'stories',('4420',26):'BLACK.',('4417',12):'amostra',('4427',3):'a estratégia',('4427',7):'stories!'})
