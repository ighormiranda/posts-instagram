"""Stories de 8 a 31/12/2026: chamada do carrossel das 15h07 (8 a 30/12) e quadros das 9h (17 a 31/12).
Rodar de dentro de stories/2026-11-mes (usa jogo.py e mes.py de lá)."""
import os, json
src = open('mes.py').read().split("BN='BLACK")[0]
exec(src)
OUT = '/home/claude/posts-instagram/stories/2026-12-fim/'
PLAN.clear()
FEED = '/home/claude/posts-instagram/2026-12-feed/'


def chamada(date, cid, linha):
    im = Image.new('RGBA', (W, H), PR + (255,)); d = ImageDraw.Draw(im)
    capa.tracked(d, (M, 210), 'POST NOVO NO PERFIL', fnt('mono500', 32), LM)
    cov = Image.open(FEED + f'{cid}_slide01.jpg').convert('RGB').resize((800, 1000))
    im.paste(cov, ((W - 800) // 2, 300))
    d.rounded_rectangle(((W - 800) // 2 - 4, 296, (W + 800) // 2 + 4, 1304), 18, outline=LM, width=4)
    capa.draw_title(d, segs(linha), M, 1380, fnt('pjs800', 58), 900, {'b': BR, 'd': LM}, 68)
    cta_emoji(im, d, 1560, 'Vai lá no perfil ver', '👆')
    handle(d); save(im, date, '1522', f'chamada-{cid}')


# chamadas do carrossel (15h22)
for dia, cid, linha in [
    ('08', 'c08', 'Você aparece quando\nalguém pergunta *pra IA?*'),
    ('09', 'c09', '3 golpes de fim de ano\n*no seu WhatsApp.*'),
    ('10', 'c10', 'Como eu faço um carrossel\n*com IA, passo a passo.*'),
    ('12', 'c12', 'A minha primeira venda\nfoi *aos 7 anos.*'),
    ('13', 'c13', 'Os 4 posts que *mais\nderam resultado.*'),
    ('14', 'c14', '3 perguntas antes de\n*colocar IA no WhatsApp.*'),
    ('15', 'c15', '3 coisas pra *parar\nde fazer* em 2027.'),
    ('16', 'c16', 'Checklist pra empresa\n*não sumir no recesso.*'),
    ('17', 'c17', 'O seu concorrente\n*aparece mais.*'),
    ('19', 'c19', 'Antes do marketing,\neu trabalhei *na Petrobras.*'),
    ('20', 'c20', 'O que eu *aprendi\nem 2026.*'),
    ('21', 'c21', 'Planeja janeiro\n*em 20 minutos.*'),
    ('22', 'c22', 'Como eu deixei o recesso\n*inteiro pronto.*'),
    ('23', 'c23', 'Janeiro começa com o\n*Instagram pronto.*'),
    ('26', 'c26', '3 posts fáceis pra\n*não sumir* até o Ano Novo.'),
    ('27', 'c27', 'O que muda em 2027\n*pra sua empresa.*'),
    ('28', 'c28', 'As minhas *3 metas*\npro Instagram.'),
    ('29', 'c29', 'O planejamento de janeiro\n*em 1 página.*'),
    ('30', 'c30', 'Obrigado, 2026.\n*O perfil em números.*'),
]:
    chamada(f'2026-12-{dia}', cid, linha)

# quadros das 9h (17 a 31/12)
T_frase('2026-12-17', '0900', 'complete', 'O que eu mais quero\nresolver no meu\nnegócio em 2027 é...')
T_heart('2026-12-18', '0900', 'coracao', 'Toca no coração se\nvocê vai trabalhar\n*até o dia 23.*')
T_text('2026-12-19', '0900', 'embaralhada', 'SÁBADO: DESEMBARALHA', '*ÇAPRENSE*', 'É a minha palavra pra 2027.\n\nAcertou? Me manda a palavra.', cta='Toca pra ver a resposta', em='👉', tam=120)
T_text('2026-12-19', '1200', 'embaralhada-resposta', 'RESPOSTA', '*PRESENÇA.*', 'Quem aparece todo dia\né lembrado.\n\nQuem acertou de primeira?', tam=120)
T_ab('2026-12-20', '0900', 'isso-aquilo', 'Em janeiro\nvocê vai...', 'Começar devagar', 'Começar acelerado')
T_emojis('2026-12-21', '0900', '3-emojis', 'SEGUNDA: EMOJI', 'Como você está\nchegando no\n*fim do ano?*', [('🔋', 'Cheio de energia', None), ('🪫', 'Bateria no fim', None), ('😴', 'Só quero dormir', None)])
T_long('2026-12-22', '0900', 'mini-aula', 'Recesso\nnão é\n*sumiço.*', 'Quem some 15 dias volta\nem janeiro do zero.\n\nUm post por dia, agendado,\nmantém você lembrado.\n\n*Enquanto você descansa.*')
T_quiz('2026-12-23', '0900', 'quiz', 'O cliente some no fim de ano. *O que fazer?*', 'Esperar janeiro', 'Mandar boas festas sem vender nada', 'B', 'Mensagem sem venda\né lembrança.\n\n*Em janeiro, quem lembrou\nde você responde primeiro.*')
T_heart('2026-12-24', '0900', 'coracao', 'Toca no coração se\no Natal aí é com\n*a família toda junta.*')
T_text('2026-12-26', '0900', 'adivinha', 'SÁBADO: ADIVINHA', 'Quantos dias seguidos\nmeu perfil postou\n*até o Natal?*', 'Desde 6 de outubro.\n\nMe responde com um número.', cta='Chuta e toca pra ver', em='👉', tam=78)
T_text('2026-12-26', '1200', 'adivinha-resposta', 'RESPOSTA', '*81 dias.*', 'Nenhum dia zerado.\nNem no Natal.\n\nQuem chegou mais perto?', tam=120)
T_ab('2026-12-27', '0900', 'isso-aquilo', 'Em 2027 o seu\nInstagram vai...', 'Postar todo dia', 'Postar quando der')
T_emojis('2026-12-28', '0900', '3-emojis', 'SEGUNDA: EMOJI', 'Qual é a sua\npalavra pra\n*2027?*', [('🚀', 'Crescer', None), ('🧘', 'Equilíbrio', None), ('🎯', 'Foco', None)])
T_long('2026-12-29', '0900', 'mini-aula', 'Meta\nprecisa de\n*rotina.*', 'Meta sem rotina vira desejo.\n\nEscolhe uma coisa pra fazer\ntoda semana em janeiro.\n\n*E coloca na agenda hoje.*')
T_quiz('2026-12-30', '0900', 'quiz', 'O que mais faz o Instagram *te mostrar?*', 'Curtida', 'Resposta e conversa no direct', 'B', 'Curtida pesa pouco.\n\n*Resposta e conversa mostram\nque você importa* pra\nquem te segue.')
T_text('2026-12-31', '0900', 'ano-novo', 'FELIZ ANO NOVO', 'Obrigado\npor *2026.*', 'Em 2027 eu continuo\naparecendo aqui todo dia.\n\nQual é a sua meta\npro ano novo?', cta='Me responde aqui', tam=110)

json.dump(PLAN, open(OUT + 'plano.json', 'w'), ensure_ascii=False, indent=1)
print(len(PLAN))
