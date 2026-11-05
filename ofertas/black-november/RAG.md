# RAG · Black November da Liga (atualizado 05/11/2026)

Resumo para continuar a campanha num chat novo do projeto Liga do Marketing.

## A oferta
- **Nome:** Black November da Liga
- **Frase principal (sempre em evidência):** "Audiência vale mais que dinheiro."
- **Produto:** carrosséis pro Instagram da clínica, todo dia, feitos com IA, com as fotos da equipe, legenda pronta e agendados no Instagram.
- **Planos (preço cheio, sem desconto):**
  - 30 carrosséis/mês: R$ 1.000 (1 por dia · R$ 33 cada)
  - 60 carrosséis/mês: R$ 1.500 (2 por dia · R$ 25 cada)
  - 90 carrosséis/mês: R$ 1.800 (3 por dia · R$ 20 cada) · "melhor custo"
- **Bônus (em vez de desconto):** 3 stories por dia no 1º mês, pra quem fechar até **30/11**.
- **Escassez:** só **5 vagas** em novembro.
- **Palavra-chave:** responder **BLACK**.
- **Prova usada nas artes:** +393% de visualizações no perfil @o.ighormiranda em 30 dias, postando todo dia (dado real do Instagram dele em 03/11).
- **Coerência:** a oferta segue o que ele ensina no carrossel de Black Friday (valor em vez de desconto, começar pela base, prazo de verdade).

## Artes prontas
Pasta `ofertas/black-november/` no GitHub `ighormiranda/posts-instagram`:
- `bn-story-1.jpg`, `bn-story-2.jpg`, `bn-story-3.jpg`: sequência de 3 stories (frase + prova · benefícios + bônus · planos + BLACK)
- `bn-status.jpg`: versão única pro status do WhatsApp
- `bn-clientes-atuais.jpg`: flyer "Só pra clientes da Liga"
- `bn-contagem-27/28/29/30.jpg`: contagem regressiva (já agendada no Instagram dia 27 a 30/11 às 10h)
Visual: fundo preto, verde-lima #9AE04C, fonte Plus Jakarta Sans, selo "BLACK NOVEMBER DA LIGA".

## Automação (HighLevel, subconta Liga do Marketing)
- Fluxo **"Black November: resposta BLACK"**, **publicado e ativo**.
- Gatilho: Cliente respondeu, com mensagem exatamente "BLACK", "Black" ou "black" (qualquer canal).
- Ações: etiqueta *black-november* → notificação interna pra todos os usuários ("Novo interessado na Black November", abre o chat).
- **Sem resposta automática por enquanto:** a DM do Instagram exige a conexão do Facebook, que está travada (verificação em 2 etapas num número antigo, final 31, nas duas contas ighor.sap e ighor.mv). Ighor vai recuperar pelo suporte da Meta (selfie ou documento). Quando conectar, recolocar o passo "DM do Instagram" com o texto abaixo.
- Resposta manual (texto aprovado):
  > Oi, {nome}! Que bom que você quer participar da Black November 😊
  > Funciona assim: a gente cria os carrosséis da sua clínica com IA, com as fotos da sua equipe, legenda pronta e já agendados no Instagram. E quem fechar até 30/11 ganha 3 stories por dia no primeiro mês.
  > Pra eu te mostrar exemplos e ver qual plano faz mais sentido, me passa o @ da sua clínica?

## Mensagem pros clientes atuais (WhatsApp, individual)
> Oi, {nome}! Como você já é cliente, quis te mostrar antes de abrir pro público. Abri 5 vagas em novembro. Se quiser, faço um carrossel de amostra com a {clínica} pra você ver como fica 😊
(enviar junto com `bn-clientes-atuais.jpg`)

## Próximos passos
1. Enviar o flyer + mensagem pros clientes atuais.
2. Postar os 3 stories da oferta e o status do WhatsApp.
3. Quem disser sim: pedir @ da clínica + 3 fotos da equipe → Claude faz 1 carrossel de amostra.
4. A cada vaga fechada: story "restam X vagas" / "última vaga".
5. Definir o que acontece com os 3 stories/dia depois do 1º mês (sai ou vira adicional pago).
6. Antes de entregar: decidir como agendar na conta de cada cliente (acesso ao Instagram ou subconta no HighLevel).
7. Recuperar o Facebook e reativar a DM automática.
