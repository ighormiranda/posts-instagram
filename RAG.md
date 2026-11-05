# RAG · Instagram @o.ighormiranda (atualizado 04/11/2026)

Resumo condensado do que já foi feito, para qualquer chat novo começar daqui.

## Contas e acessos
- **HighLevel certo:** subconta **Liga do Marketing** (locationId `9kACPQc23ubmvvj746BU`). A conexão já caiu duas vezes em subconta errada (Tarcisio/Textil Club e Paulo Maia). Sempre conferir com "get-location" antes de mexer.
- **Conta Instagram no HighLevel:** `6ac0018bde3dbf732e2805c6_9kACPQc23ubmvvj746BU_17841400898700445` · userId/createdBy `jt7F6GlvzbRCr7TR53Zk`.
- **Repositório das artes:** GitHub `ighormiranda/posts-instagram`. Os posts puxam a imagem por link raw do GitHub.
  - Pastas: `2026-10-semana-03`, `-04`, `2026-11-semana-05`, `-06`, `2026-11-avulsos` (Black Friday, Novembro Azul), `stories/2026-11-semana-05` e `-06`, `fotos/` (acervo), `videos/`.
- **Trocar capa sem editar o post:** substituir o arquivo no mesmo caminho em `main` (posts antigos usam link `main`). Posts novos usam link fixo por commit; para trocar, é preciso editar o post.

## Cuidados com o HighLevel (aprendidos)
- **Editar post pela conexão apaga a collab @arkyon.io.** Criar post também não marca collab. Ighor adiciona a collab à mão no Planejador.
- Story funciona com `type: story`, 1 imagem 1080x1920, legenda vazia. Testado: saiu no ar em 04/11 às 9h.
- Horários em UTC: 12h = 15:00Z · 19h = 22:00Z · story 9h = 12:00Z, 12h15 = 15:15Z, 19h15 = 22:15Z.
- Workflows: a conexão não cria automação; precisa ser pelo navegador do app Claude (janela aberta e visível).

## O que os dados mostraram (análise de out/nov)
- Capa com rosto em foto real rende ~2x a capa só de texto. Momentos reais (Reels, evento, história pessoal) são os campeões (Reels da filha 641, "3 coisas que eu mudei" 607, Reels evento 498).
- Capa com fundo branco rende menos que a escura com foto inteira.
- Visualizações subiram (+393% em 30 dias até 03/11), mas seguidores parados (~1.906). Problema principal: conversão no perfil (bio, fixados, destaques).
- Reels é o formato que mais leva a não seguidores; ainda são poucos.

## Regras de conteúdo (do Ighor)
- 2 posts/dia (12h e 19h) + 3 stories/dia automáticos (9h dica, 12h15 e 19h15 chamada pro post). Stories automáticos nunca dependem dos stories dele.
- Rosto na maioria das capas, variar roupas e cenários, não repetir foto em sequência. Nunca usar `Fotos_MentalidadeMaster1744`.
- Frases curtas, linhas quebradas, margem de segurança nas artes.
- Nunca culpar secretária/recepção; o problema é processo.
- CTAs variados, um por post: segue (prioridade, pra ganhar seguidor), compartilha, salva, DIAGNÓSTICO, ARKYBOOK (pode aparecer mais de uma vez por semana, só não ficar repetitivo).
- Séries em partes ("amanhã, parte 2") dão motivo pra seguir.
- Datas especiais entram no calendário (Novembro Azul, Black Friday; ano que vem: Dia do Médico 18/10, Dia da Secretária 30/09 valorizando a profissional).
- Nunca inventar número; só dados reais.

## Fila atual (Planejador)
- **03–08/11:** semana 05 completa (12h e 19h), capas trocadas por fotos novas. Legendas ainda com "Comenta ARKYBOOK" em todos.
- **09/11 12h:** Novembro Azul (todo azul, sem foto). Sem collab.
- **09–15/11:** semana 06 (13 posts), série "5 mensagens difíceis no WhatsApp" (10–14/11 às 12h) + resumo 15/11 19h. Sem collab.
- **20/11 12h:** Black Friday (montar oferta até 27). Sem collab.
- **Stories:** 04–15/11 e 20/11 agendados (39).
- **Reels 18h (3ª postagem do dia):** 06/11 Reels com prints dos insights (CTA segue) · 10/11 loop 7s (CTA BLACK) · 13/11 loop 4s (CTA segue). Arquivos em `videos/`. Sem collab e sem música (agendados pela conexão).
- **Carrossel "30 dias de automação"** pronto em `2026-11-avulsos/30dias_slideNN.jpg`, ainda sem data.
- **Case (RAG Black November mídia social, 05/11):** automação começou em 6/10. Falar "+393% nos primeiros 30 dias da automação" (nunca "últimos 30 dias"). Não usar "Visualizadores" (+58,6% em 30d, mas -52,6% em 90d). Pode usar: 85% das visualizações de 90 dias vieram de posts+stories; nenhum dia zerado desde 6/10. Não afirmar "sem anúncio" nem "todos carrosséis" sem confirmação. CTA da Black no feed: "Manda BLACK no direct"; LP em scroll storytelling vai pra bio quando tiver link. RAG completa em `ofertas/black-november/RAG-midia-social.md`.
- **Regra nova:** não mostrar fraqueza ("seguidores quase nada") em peça com oferta; só em peça cujo CTA é seguir.
- **Vazio:** 16–19/11 e 21–30/11 (faltam ~29 posts + stories).

## Ferramentas (no ambiente de trabalho do Claude, recriar se o chat for novo)
- `capa.py`: capa 1080x1350 (layout escuro com foto ou claro). Fontes Plus Jakarta Sans 800/700/500 + IBM Plex Mono 500.
- `gen.py` + JSON: carrossel inteiro (tipos de slide: capa, texto, item numerado, evite, chat WhatsApp, final com CTA).
- `stories.py`: story dica e story chamada pro post.
- Cores: preto #040404, branco, verde #1E822A, lima #9AE04C. Handle @o.ighormiranda e paginação no rodapé.

## Outras entregas
- Reels "frase do Makers Day" (22s) em `videos/reels-frase-makers-day.mp4`, com legenda pronta. Postar pelo celular com música em alta.
- **Black November da Liga:** "Audiência vale mais que dinheiro." Só 5 vagas. Bônus: 3 stories por dia no 1º mês pra quem fechar até 30/11. Palavra-chave BLACK. Próximos passos sugeridos: mensagem individual pros clientes atuais, amostra grátis de 1 carrossel pra quem responder BLACK, contagem regressiva 27–30/11, definir o que acontece com os stories depois do 1º mês. Artes em `ofertas/black-november/` (3 stories + status).
- **Oferta Liga (carrosséis com IA):** 30 por R$1.000, 60 por R$1.500, 90 por R$1.800/mês. Artes: 1 imagem pro status do WhatsApp e 3 stories em sequência (prova +393%, benefícios, planos + "Responde com CARROSSEL").

## Pendências
1. **Workflow "BLACK"** (Black November da Liga): gatilho resposta igual a "black" (sem diferenciar maiúscula) → etiqueta *black-november* → resposta automática → notificação pro Ighor. Montar pelo navegador do app com a janela visível. Confirmar se o WhatsApp está conectado no HighLevel. Texto da resposta aguardando aprovação final (versão Black November).
2. **Bio/nome:** opções enviadas; recomendado nome "Ighor Miranda | Vendas e IA pra Clínicas" + bio "Sua clínica não precisa de mais lead. / Precisa parar de perder os que já tem. / Clínicas de R$25 mil a +R$300 mil/mês. / Comenta DIAGNÓSTICO em um post 👇". Aguardando escolha.
3. Fixar "Quem sou eu / O que eu faço / O que eu vendo" e subir destaques "Sobre mim" e "Diagnóstico" (artes já na pasta).
4. Collab arkyon.io nos posts criados pela conexão (09/11 em diante).
5. Montar posts e stories de 16–19/11 e 21–30/11 (com série nova na semana de 16/11).
6. Workflows do DIAGNÓSTICO aparecem só como rascunho no HighLevel; conferir se a automação está ativa.
7. Mais Reels: Ighor manda vídeos curtos, Claude monta.
