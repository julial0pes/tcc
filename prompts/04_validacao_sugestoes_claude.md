# Prompt 4 — Validação dos requisitos sugeridos pelo Claude

**Etapa:** validação das sugestões para os casos sem consenso na rodada 2 (seção 8.4 do README).
**Usado com:** ChatGPT e Gemini, cada um em conversa nova.
**Entrada:** planilha com a aba "REQUISITOS DO TCC". Os textos sugeridos estão na coluna Q ("Requisito sugerido pelo Claude (Rodada 2)"), preenchida em 10 linhas.

O texto é o mesmo para as duas IAs. Cada uma escreve o próprio nome no cabeçalho das colunas que cria: R e S para o ChatGPT, T e U para o Gemini.

---

# PROMPT — VALIDAÇÃO DOS REQUISITOS SUGERIDOS PELO CLAUDE

Analise a planilha Excel anexada, especificamente a aba "REQUISITOS DO TCC". Ela faz parte de um Trabalho de Conclusão de Curso em Engenharia de Software que avalia a capacidade de modelos de IA de identificar erros inseridos intencionalmente em requisitos de software.

## 1. Objetivo

Verificar se cada requisito sugerido na coluna "Requisito sugerido pelo Claude (Rodada 2)" apresenta efetivamente o erro indicado na coluna "Situação", usando conceitos e boas práticas de Engenharia de Requisitos e, quando aplicável, a ISO/IEC/IEEE 29148.

Colunas a considerar:
- Coluna C, "Requisito": requisito original, em inglês.
- Coluna D, "Tradução": requisito original traduzido.
- Coluna E, "Situação": categoria do erro que deve estar presente.
- Coluna Q, "Requisito sugerido pelo Claude (Rodada 2)": texto que você deve avaliar.

Confirme a posição das colunas pelos cabeçalhos antes de começar. A coluna Q está preenchida em 10 linhas.

## 2. Independência — OBRIGATÓRIO

- Não consulte nenhuma outra coluna além de C, D, E e Q, nem avaliações, justificativas ou textos refinados de qualquer IA.
- Não concorde só porque o texto foi sugerido por outra IA ou porque já passou por revisões.
- Não presuma que a categoria da coluna E está correta para o texto sugerido.
- Não busque concordância nem discordância de propósito. Decida apenas por critério técnico.

## 3. Critérios

- Ambiguidade: o requisito permite duas ou mais interpretações plausíveis sobre o comportamento esperado. Não confunda com contradição ou mera falta de detalhe.
- Incompletude: o requisito omite informação essencial para compreender, implementar ou verificar o comportamento esperado. Não classifique como incompleto só porque poderia ter mais detalhes.
- Inviabilidade: o requisito exige algo tecnicamente impossível ou inviável no contexto. Não confunda com dificuldade ou custo alto.
- Redundância: o requisito repete desnecessariamente uma informação, um comportamento ou uma obrigação. O trecho repetido deve poder ser retirado sem nenhuma perda de significado. Não confunda com funcionalidades parecidas que têm finalidades diferentes.

## 4. Procedimento, para cada linha com texto na coluna Q

1. Leia o requisito original (C e D) para entender a funcionalidade.
2. Identifique a categoria indicada na coluna E.
3. Leia o texto da coluna Q.
4. Verifique se a alteração introduziu um defeito real de Engenharia de Requisitos.
5. Verifique se o defeito corresponde especificamente à categoria da coluna E e se não introduz, em vez disso ou além disso, um defeito de outra categoria.
6. Verifique se o defeito é perceptível para quem lê apenas o texto da coluna Q, sem comparar com o original. No experimento, os modelos avaliados não terão acesso ao requisito original.

Não basta o texto ter algum problema: o problema precisa corresponder à categoria da coluna E.

## 5. Preenchimento do Excel

Crie duas colunas novas logo após a última coluna preenchida da aba, sem alterar nenhuma coluna existente:

1. "Validação [seu nome] — Sugestão Claude", substituindo [seu nome] pelo nome do seu modelo (por exemplo, ChatGPT ou Gemini). Preencha somente com:
   - Concordo: o texto da coluna Q apresenta efetivamente o erro indicado na coluna E.
   - Discordo: o texto não apresenta o erro indicado, apresenta erro de outra categoria ou não há evidência técnica suficiente.
   - Não se aplica: a linha não tem texto na coluna Q.
   Formatação: verde para Concordo, vermelho para Discordo e cinza para Não se aplica.

2. "Justificativa [seu nome] — Sugestão Claude": uma justificativa técnica individual. Nas discordâncias, explique exatamente o que impede o enquadramento na categoria da coluna E e, se for o caso, qual categoria seria mais adequada. Nos casos "Não se aplica", escreva: "Requisito sem sugestão do Claude".

## 6. Preservação — OBRIGATÓRIO

- Preserve todas as abas, os 166 requisitos e a ordem das linhas.
- Não altere nenhum texto, nenhuma categoria e nenhuma avaliação existente.
- Não insira nem exclua linhas e não desloque colunas.
- Preserve cores, bordas, fontes, alinhamentos, larguras, fórmulas e filtros.
- Escreva somente nas duas colunas novas.

## 7. Relatório final

Ao concluir, apresente:
1. Quantidade de requisitos sugeridos avaliados.
2. Quantidade de concordâncias e de discordâncias.
3. Percentual de concordância.
4. Distribuição por categoria (Ambiguidade, Incompletude, Redundância), com concordâncias e discordâncias.
5. Lista das discordâncias, com a linha, a categoria e o motivo em uma frase.

## 8. Entrega

Devolva o arquivo Excel completo e atualizado, com a estrutura e a formatação originais.

REGRA FINAL: sua função é avaliar, não corrigir. Não reescreva nenhum requisito.
