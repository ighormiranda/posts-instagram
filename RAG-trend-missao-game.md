# RAG · Trend "Missão" (lançamento do GTA 6) · nov/2026
Feito no @o.ighormiranda em 19/11/2026. Serve para replicar em clientes (ex.: Dra. Shakti).

## 1. O que é a trend
- No lançamento do GTA 6, os perfis começaram a postar Reels no estilo de **capa de game de mundo aberto**: a pessoa vira uma ilustração com céu de pôr do sol roxo e laranja, palmeiras e cidade de praia, e aparece **"MISSÃO INICIADA"** + uma missão impossível do nicho.
- Referência vista: um Reels da área da saúde em que a médica aparece no estilo game com "MISSÃO INICIADA: convencer a Dona Maria a tirar o tapetinho da sala". A legenda brinca com o GTA e fecha com uma pergunta para o público.
- Funciona porque junta o assunto do momento com uma dor que o público reconhece na hora.
- **Prazo:** trend de lançamento dura poucos dias. Postar rápido vale mais que postar perfeito.

## 2. Regras de direito autoral (obrigatório)
- **Não** usar o logo do GTA, o nome do jogo na arte, personagens ou arte oficial (são da Rockstar).
- Usar só o **estilo** (ilustração de game, neon, pôr do sol, "MISSÃO INICIADA").
- O nome "GTA 6" pode aparecer **só na legenda**, para pegar o assunto.

## 3. Como gerar as imagens (ChatGPT)
- Gerar **todas no mesmo chat**, para o rosto e o estilo ficarem iguais.
- Anexar 3 fotos reais da pessoa (frente, lado, sorrindo).
- Se a pessoa for profissional de saúde, usar a roupa e os objetos da profissão (jaleco, consultório), sem aparecer paciente.

**Prompt base (cena 1, "missão iniciada"):**
```
Use as fotos anexadas como referência exata do rosto e do corpo desta pessoa (mesma cor de olhos, cabelo, traços e tipo físico; não deixe mais magra nem mais jovem).
Transforme em uma ilustração no estilo de arte de capa de videogame de mundo aberto: traço de quadrinho realista, cores saturadas, céu de pôr do sol roxo e laranja, palmeiras, rua de cidade litorânea ao fundo.
A pessoa está andando confiante na direção da câmera, com a roupa de trabalho dela, segurando [objeto da profissão].
Formato vertical 9:16. Sem nenhum texto, logotipo ou marca na imagem. Deixe a parte de baixo mais livre para texto.
```

**Cenas seguintes (sempre começar com "Mesmo homem/mulher, mesmo estilo de ilustração de capa de videogame de mundo aberto das imagens anteriores."):**
- **Missão falhou:** cansado/a à noite, escritório ou consultório bagunçado, mão na testa, celular cheio de notificações, luz de monitor e neon roxo pela janela.
- **Missão concluída:** relaxado/a numa varanda de frente para o mar ao pôr do sol, sorrindo, notebook ou celular mostrando um gráfico subindo.
- **Close final:** rosto e ombros, olhando para a câmera, pôr do sol neon com palmeiras desfocadas.
- **Conquista desbloqueada (story):** terraço de prédio à noite, cidade neon, braço levantado comemorando, confete no ar.
- **Escolhe o seu personagem (story):** três versões da pessoa lado a lado, como numa tela de seleção de jogo, cada uma com a roupa de um tipo de público/serviço.

## 4. O Reels (o que foi feito no perfil do Ighor)
Arquivo: `reels/trend-missao/missao-empresario.mp4` (15 s, 1080x1920). Gerador: Python (PIL) + ffmpeg. Cada tela tem zoom lento, flash branco na troca e texto entrando linha a linha.

| Tela | Imagem | Selo | Texto |
|---|---|---|---|
| 1 (0–3,6 s) | andando no calçadão | MISSÃO INICIADA (amarelo) | POSTAR TODO DIA / NO INSTAGRAM / DA EMPRESA |
| 2 (3,6–7,4 s) | escritório à noite, tela vermelha e tremendo | MISSÃO FALHOU (vermelho) | DIA 4. / SEM TEMPO. / SEM IDEIA. / PERFIL PARADO. |
| 3 (7,4–11,8 s) | varanda relaxado | MISSÃO CONCLUÍDA (verde) | LIGUEI A AUTOMAÇÃO. + dado real |
| 4 (11,8–15,5 s) | close | PRÓXIMA MISSÃO (rosa) | 10 MIL SEGUIDORES. / Me segue pra acompanhar. |

Visual: texto branco com contorno preto, palavra-chave em cor (amarelo, rosa, verde, vermelho), degradê escuro na parte de baixo, @ do perfil no topo. Texto sempre acima dos 15% de baixo da tela (o Instagram cobre essa faixa).

**Legenda usada:**
> @o.ighormiranda
> GTA 6 chegou, mas tem missão que nem o empresário consegue concluir sozinho 😂
> Qual é a sua missão impossível no seu negócio? Me conta nos comentários.

**Postagem:** feita **à mão pelo app**, para colocar um áudio de game em alta (o HighLevel não adiciona música da biblioteca do Instagram). Ao postar, renomear o áudio (ex.: "missão do empresário").

## 5. Stories que acompanham (agendados no HighLevel)
1. **Chamada para o Reels** (logo depois do post): imagem do calçadão + "POST NOVO NO PERFIL · MISSÃO: POSTAR TODO DIA. Vê como terminou no meu perfil e me conta a sua missão impossível."
2. **Isca do prompt** (15 min depois): close + "MISSÃO EXTRA · QUER VIRAR PERSONAGEM DE GAME?" + botão amarelo "Responde com 💰 e eu te mando o prompt".
   - Emoji desenhado como imagem (fonte NotoColorEmoji), porque a fonte do texto não tem emoji.
   - Quem responde 💰 recebe no direct a mensagem pronta: `roteiros/resposta-prompt-game.md`.
   - Pedir para a pessoa marcar o perfil quando postar a imagem dela. Repostar.
3. **Conquista desbloqueada** (dia seguinte, depois do próximo Reels): terraço comemorando + dado real (ex.: "45 DIAS SEM UM DIA ZERADO").
4. **Escolhe o seu personagem** (2 dias depois, à noite): 3 versões numeradas + "Qual é o seu negócio? Me responde com 1, 2 ou 3." Serve para gerar direct e descobrir o público.

Por que funciona: resposta no story abre conversa no direct (sinal forte para o Instagram) e quem gera a imagem e marca leva o perfil para gente nova.

## 6. Como adaptar para a Dra. Shakti (dentista / harmonização, Niterói)
Usar só o que for verdade para ela e respeitar o código de ética do CFO: sem antes e depois, sem promessa de resultado, sem paciente identificável, sem preço na arte.

Ideias de missão (escolher uma por Reels):
- **MISSÃO INICIADA:** convencer o paciente a usar fio dental todo dia. **FALHOU:** "Dia 2. Fio dental na gaveta." **CONCLUÍDA:** a dica real dela para criar o hábito.
- **MISSÃO INICIADA:** descobrir há quanto tempo o paciente não vai ao dentista. **FALHOU:** "Desde a última vez que doeu." **CONCLUÍDA:** "Revisão a cada 6 meses" (só se for a orientação dela).
- **MISSÃO INICIADA:** fazer o paciente parar de ranger os dentes de noite. **FALHOU:** "Ele nem sabia que rangia." **CONCLUÍDA:** sinais para ficar atento + "chama no WhatsApp da bio".

Fecho do Reels (tela 4): "PRÓXIMA MISSÃO: cuidar do seu sorriso. Chama no WhatsApp da bio." Legenda: "[Profissão] em tempos de GTA 6 😂 Qual dessas missões é a sua? Me conta nos comentários." + hashtags locais dela.

Stories: os mesmos 4, com textos dela. Isca do prompt: só se ela topar responder o direct; senão, trocar por "Responde com 🦷 qual missão é a sua".

## 7. Checklist rápido
1. Pedir as fotos da cliente e gerar as 4 cenas no mesmo chat do ChatGPT.
2. Montar o Reels (4 telas, 15 s) e mandar para a cliente aprovar.
3. A cliente posta à mão com áudio em alta (ou agenda sem música no HighLevel).
4. Agendar os stories: chamada (logo depois), isca (+15 min), conquista (dia seguinte), personagem (2 dias depois). Pares sempre com 15 min de intervalo, nunca 1 ou 2 min.
5. Responder as reações no direct no mesmo dia.
