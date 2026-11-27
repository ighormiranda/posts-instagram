import sys; sys.path.insert(0,'..')
from editor import *
A='/mnt/user-data/attachments/6b783e31-48d9-5fd3-b925-355c9d9bd392/'
P=[('abb17cd4-IMG_4572.mov','O cliente *cancelou.*'),('adbdce08-IMG_4573.mov','O cliente *não pagou.*'),
   ('95e58f98-IMG_4574.mov','E você, empresário, ainda vai pagar *a comissão do vendedor.*'),
   ('981a4827-IMG_4576.mov','Cancelamento ou inadimplência não autoriza mais você a *descontar a comissão* do seu vendedor.'),
   ('90cd7490-IMG_4577.mov','Ou seja, o risco da venda ruim *é seu.*'),
   ('0c9364db-IMG_4578.mov','Então, antes da comissão, *a venda precisa ser boa.*'),
   ('c6c7ea00-IMG_4579.mov','E um *agente de IA* pode atuar exatamente nessa parte.'),
   ('f07164d7-IMG_4582.mov','Ele separa quem só está curioso de quem *realmente quer comprar.*'),
   ('f9b1ef9c-IMG_4583.mov','Ele *confirma o pagamento* e vai atrás de *quem sumiu.*'),
   ('73cc6404-IMG_4584.mov','E ele *não ganha comissão.*'),
   ('e919a846-IMG_4585.mov','Ou seja, a sua equipe comercial vai ganhar comissão até da venda que deu errado, e a IA *não vai ganhar comissão nenhuma.*'),
   ('564631ab-IMG_4586.mov','Você quer ver como pode funcionar na sua empresa? *Me chama no direct.*')]
import os
os.makedirs('tmp',exist_ok=True)
# card da tese (aparece na peça 3)
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
d.rounded_rectangle((50,225,1030,560),26,fill=(8,8,8,250),outline=LM,width=4)
d.text((95,255),'TST · TEMA 65 (tese vinculante)',font=fnt('mono500',34),fill=LM)
y=315
for l in ['"A inadimplência ou cancelamento','da compra pelo cliente não autoriza','o empregador a estornar as','comissões do empregado."']:
    d.text((100,y),l,font=fnt('pjs700',40),fill=(255,255,255)); y+=54
im.save('tmp/card-tst.png')
t=build([(A+f,tx) for f,tx in P],['Venda cancelada.','E a comissão?'],'r05-comissao-tst.mp4',cards=[(3,'tmp/card-tst.png')],rodape=('Conteúdo informativo. Não é orientação jurídica.',10))
print('total',round(t,2))
