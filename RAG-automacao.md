# RAG · Como automatizar as postagens (HighLevel + GitHub) · atualizado 16/11/2026

Manual para um chat novo agendar posts, carrosséis, Reels e stories sozinho, sem o Ighor postar nada à mão.
Serve para o perfil do Ighor e para qualquer cliente: só muda a subconta e o accountId.

## 1. Como funciona (resumo)
1. A arte é gerada em Python (PIL) e salva no repositório GitHub **ighormiranda/posts-instagram**.
2. Faz commit e push. A imagem fica pública no link "raw" do GitHub.
3. Esse link vai para o HighLevel (conector "High Level" / ferramenta `social-media-posting_create-post`), que publica no Instagram na data marcada.

## 2. Preparar a sessão
- Conectores necessários: **High Level** (subconta certa) e **GitHub** com acesso ao repositório.
- Clonar: `git clone https://github.com/ighormiranda/posts-instagram` (pedir acesso com add_repo, se precisar).
- Autor do commit: `Ighor Miranda <ighor@ligadomarketing.com>`.
- Fontes e geradores ficam em `ferramentas/`: capa.py, gen.py, novidades.py, fonts/, monstros/.

## 3. IDs do HighLevel
**Perfil do Ighor (@o.ighormiranda), subconta Liga do Marketing (location 9kACPQc23ubmvvj746BU):**
- accountId: `6ac0018bde3dbf732e2805c6_9kACPQc23ubmvvj746BU_17841400898700445`
- userId: `jt7F6GlvzbRCr7TR53Zk`

**Cliente novo:**
1. Conectar o HighLevel na subconta do cliente.
2. Rodar `social-media-posting_get-account` e pegar o accountId do Instagram dele.
3. Pegar o userId com `locations_get-location`, ou copiar o `createdBy` de um post existente (`get-posts`).
4. Criar uma pasta só do cliente no repositório, por exemplo `clientes/nome-do-cliente/`.

## 4. Link da mídia
Use sempre o link fixo no commit (nunca "main", senão a imagem muda se o arquivo for editado):
`https://raw.githubusercontent.com/ighormiranda/posts-instagram/<HASH_DO_COMMIT>/<caminho/arquivo.jpg>`
O hash sai de `git rev-parse HEAD`, depois do push.

## 5. Chamada para agendar (create-post)
```
body_accountIds: ["<accountId>"]
body_userId: "<userId>"
body_type: "post" | "story" | "reel"
body_status: "scheduled"
body_scheduleDate: "2026-11-20T15:00:00.000Z"   (sempre em UTC)
body_summary: "legenda"                          (stories não precisam)
body_media: [{"type":"image/jpeg","url":"<raw>"}, ...]   (carrossel = vários itens, na ordem)
```
- Reel: `{"type":"video/mp4","url":"<raw .mp4>"}` com body_type "reel".
- Carrossel misto (jpg + mp4) funciona.
- Story: uma imagem 1080x1920 por chamada.
- Post: 1080x1350 (4:5).

**Horário (Brasil, UTC-3):** 9h = 12:00Z · 12h = 15:00Z · 12h15 = 15:15Z · 16h = 19:00Z · 18h = 21:00Z · 19h = 22:00Z · 19h15 = 22:15Z · 20h30 = 23:30Z · 21h = 00:00Z do dia seguinte.

## 6. Problemas conhecidos (e o que fazer)
- **edit-post não funciona** (erro de JSON). Para mudar horário ou arte, crie um post novo e peça para o Ighor apagar o antigo no Planejador. Avise sempre.
- **Antes de agendar, rode `get-posts`** no período (body_type "all") para não marcar dois posts no mesmo horário.
- **Legenda:** nunca use os caracteres de maior e menor (o HighLevel transforma em &gt;).
- **Collab** com @arkyon.io não dá pela API. Depois que o post sai, o Claude adiciona pelo Chrome (Instagram web, já logado): post → ⋯ → Editar → "Adicionar colaboradores" → arkyon.io → marcar → Concluir → Concluir. O Ighor aceita o convite no perfil da Arkyon. Não precisa perguntar antes.
  - Leva collab Arkyon **só o que faz sentido no perfil da Arkyon** (transformação comercial): atendimento e WhatsApp, follow-up, agendamento, CRM, processo comercial, IA no atendimento, gestão e riscos do negócio (ex.: Economist 2027).
  - Não leva: Black November e oferta da Liga (é produto da Liga), dicas de Instagram e conteúdo (retenção, Reels, stories), Novidades da IA genéricas, post pessoal, família, viagem, jogos e reações de stories.
  - Collab com a ELO (@elosaudeclube): só o Reels de terça ("Terça com IA"). Nunca ELO e Arkyon no mesmo post.
  - Cuidado no menu ⋯: o 2º item é Editar e o 3º é "Ocultar número de curtidas". Conferir na tela antes de clicar e deixar o "rótulo de IA" desligado.
- **Enquete, caixinha, quiz oficial, link e menção** também não vão pela API. Faça story "toque/responda com emoji" ou deixe para o Ighor colar na hora.
- Se o conector HighLevel cair: mande os arquivos (SendUserFile) para postar à mão e peça para reconectar.
- Se uma chamada some sem resposta, confira com get-posts antes de repetir (evita duplicado).

## 7. Rotina padrão do perfil do Ighor
- **Feed:** 2 posts por dia (12h e 19h). Reels às 18h quando houver. Sexta 18h: "Novidades da IA" (ver `ferramentas/README-novidades.md` e a tarefa agendada de quinta 9h47).
- **Stories automáticos:**
  - 9h: dica
  - 12h15: chamada do post das 12h
  - 19h15: chamada do post das 19h
  - 20h30: 1 interativo (jogo do objeto escondido, quiz por toque ou reação)
- Jogo do objeto escondido: foto e pergunta saem automáticas. A revelação é manual no dia seguinte, com o @ de quem acertou.
- Datas especiais ganham post temático (ex.: sexta 13 = terror, `2026-11-avulsos/sexta13_*` e `sanguessuga_*`).

## 8. Regras de conteúdo
- Só dado real do painel: "+393% nos primeiros 30 dias da automação" (nunca "últimos 30 dias", nunca "Visualizadores", não dizer "sem anúncio").
- Público: empresários em geral (negócio, crescimento, mentalidade). Clínica continua na oferta.
- Oferta atual: Black November, LP black.ligadomarketing.com. CTA "link na bio" ou "Manda BLACK".
- "Seguidores quase não vieram" só em peça com CTA de seguir, nunca perto da oferta.
- Foto: só as do repositório `fotos/` que o Ighor aprovou. Fotos proibidas estão listadas no RAG.md. A pasta nova `fotos/estudio-blazer-marinho/` é dele (ensaio 2026).
- Vídeo de terceiros: só oficial da empresa, com crédito.
- Visual padrão: fundo preto/verde-escuro, verde-lima #9AE04C, Plus Jakarta Sans, @o.ighormiranda no rodapé.

## 9. Destaques (Instagram web, pelo Chrome)
Abrir o destaque → ⋯ → Editar → Avançar → aba "Stories" → marcar → Avançar → Concluir.
Destaques atuais: Sobre mim, Black, Resultados, IA na prática, Bastidores, Perguntas. Já foram alimentados em 14/11.

## 10. Onde está o resto
- `RAG.md`: histórico completo do perfil.
- `RAG-yap-stories.md`: estratégia de série YAP e stories interativos.
- `ofertas/black-november/RAG-midia-social.md`: funil da Black.

## 11. Banco de fotos novas (17/11)
Em `fotos/`, todas do Ighor e aprovadas para uso:
- `estudio-branco-camisa-preta/`: fundo branco, bom para recorte e capa (caneca, celular, mão no queixo, braços cruzados).
- `estudio-camisa-roxa/`: fundo laranja, gestos de apontar (para cima, para o lado) e dedo na testa. Ótimas para capa com texto.
- `estudio-moletom-makers/`: moletom verde Makers.
- `estudio-blazer-marinho/`: ensaio 2026 (Drive).
- `evento-a-vida-e-hoje/`: letreiro "A vida é hoje", apontando.
- `familia-com-filha/`: com a filha. Usar só em post pessoal/bastidor e com o OK do Ighor.
- `natureza-rio/` (sem camisa), `viagem/`, `jantar/`: uso pontual em conteúdo pessoal.
- `gerada-ia/`: fotos do Ighor geradas com IA (ChatGPT). Ao postar, ligar o "rótulo de IA" no Instagram (regra para foto realista feita com IA). Usar com moderação: post com cara de IA tende a performar menos.
