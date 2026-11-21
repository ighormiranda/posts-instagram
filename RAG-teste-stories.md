# RAG · Teste de stories · 21 a 27/11/2026

## Problema
- Os stories tinham cerca de 100 visualizações. Hoje (21/11) estão entre 12 e 17 nos de ontem, para cerca de 1.900 seguidores.
- Quase todos os stories atuais são arte com texto, postados automaticamente pelo HighLevel, sem figurinha (enquete, caixinha, link, música).
- O único story com resposta no print de 21/11 foi uma foto pessoal postada pelo celular.

## Checagem de restrição (21/11, 11h30)
- Status da Conta no Instagram: tudo verde. Sem conteúdo removido, sem restrição de recursos, **sem limite de recomendação** (qualificação de recomendação ok). Não há shadowban.
- O HighLevel publica pela API oficial da Meta. Testes públicos (Hootsuite, Agorapulse, Buffer) não acharam queda de alcance por agendar.

## Hipóteses (o que pode ter derrubado)
- **H1 · Sem figurinha = sem toque.** O HighLevel não põe figurinha. Sem interação, o Instagram empurra os stories para o fim da fila.
- **H2 · Arte com texto é pulada.** Formato que parece anúncio. Foto ou vídeo do dia a dia segura mais.
- **H3 · Volume.** Muitos stories por dia, cada um com pouco motivo para assistir.
- **H4 · Queda de alcance da conta toda** (não do formato). Só aparece se os manuais também caírem.

## Os 4 tipos testados
| Tipo | O que é | Postado por |
|---|---|---|
| **A** | Arte automática, sem figurinha (o que já está agendado) | HighLevel |
| **B** | A mesma arte do dia, postada pelo celular **com** enquete ou caixinha | Ighor |
| **C** | Foto ou vídeo pessoal, **sem** figurinha | Ighor |
| **D** | Foto ou vídeo pessoal, **com** enquete ou caixinha | Ighor |

Comparar A x B isola a figurinha (H1). B x D isola o formato (H2).

## Agenda da semana
| Dia | Manhã (até 12h) | Tarde/noite |
|---|---|---|
| sáb 21 | **D** (agora) | A (20h30, já agendado) |
| dom 22 | **C** | **B** (arte do "Black aviso" + enquete "Você vai comprar algo na Black? Sim / Só se valer") |
| seg 23 | **D** | A (Black abriu) |
| ter 24 | **B** | **C** |
| qua 25 | **D** | A |
| qui 26 | **C** | **B** |
| sex 27 | **D** | A |
- No máximo 4 stories por dia somando tudo.
- As respostas dos jogos (quiz, embaralhada, adivinha) saem 3 horas depois da pergunta, nunca 1 minuto depois.

## Como medir
- Toda noite, às 22h, o Ighor manda o print da lista de stories (a tela com o número de visualizações de cada um).
- Anotar por story: tipo, visualizações, respostas e toques na figurinha.
- Comparar sempre as **visualizações** e as **respostas** de cada tipo, não os números absolutos de dias diferentes.

## Regra de decisão (sex 27/11)
- **D ou B bem acima de A** (o dobro ou mais) → H1/H2 confirmadas. A automação passa a fazer só o feed. Os stories ficam: 1 pessoal por dia pelo celular + a arte do dia postada à mão com figurinha.
- **C igual a D** → a figurinha não é o que pesa, o formato pessoal é. Manter pessoal todo dia.
- **Todos baixos** → H4. Olhar o painel de alcance da conta e o feed.

## Resultados
| Data | Tipo | Story | Visualizações | Respostas | Toques |
|---|---|---|---|---|---|
| 20/11 | A | post 12h | 17 | 0 | 0 |
| 20/11 | A | missão conquista | 16 | 0 | 0 |
| 20/11 | C | foto pessoal | 15 | 1 | 0 |
| 20/11 | A | case ep. 3 | 12 | 0 | 0 |
