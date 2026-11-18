# Prompt 2 — Validação técnica dos erros inseridos (rodada 1)

**Etapa:** validação dos erros pelas IAs, rodada 1 (seção 8.1 do README).
**Usado com:** ChatGPT, Gemini e Claude, nesta ordem, cada um em conversa nova.
**Entrada:** planilha com a aba "REQUISITOS DO TCC" (166 requisitos). Cada IA recebeu a planilha já com as colunas das IAs anteriores.

O mesmo texto foi enviado às três IAs. A versão abaixo é a que foi enviada ao Claude, a terceira a avaliar. O prompt pede que cada IA primeiro faça a própria análise e só depois compare com as avaliações que já estiverem na planilha. Para o ChatGPT, o primeiro a avaliar, ainda não havia avaliações anteriores.

---

# PROMPT — VALIDAÇÃO TÉCNICA DOS ERROS IMPUTADOS NOS REQUISITOS — CLAUDE

Analise criteriosamente a planilha Excel anexada, especificamente a aba **"REQUISITOS DO TCC"**, que contém 166 requisitos funcionais dos projetos 5, 10, 61 e 67.

Esta análise faz parte de um Trabalho de Conclusão de Curso (TCC) na área de Engenharia de Software, cujo objetivo é avaliar a capacidade de modelos de Inteligência Artificial de identificar erros intencionalmente inseridos em requisitos de software.

## 1. Objetivo

Avaliar individualmente se os erros intencionalmente inseridos nos requisitos são tecnicamente coerentes com as categorias atribuídas.

As categorias utilizadas são:

- **Ambiguidade:** requisito que permite duas ou mais interpretações plausíveis, comprometendo sua compreensão objetiva.
- **Incompletude:** requisito que omite informações necessárias para compreender, implementar ou verificar adequadamente o comportamento esperado.
- **Inviabilidade:** requisito que apresenta condições tecnicamente, operacionalmente ou fisicamente impossíveis ou comprovadamente inviáveis dentro do contexto estabelecido.
- **Redundância:** requisito que repete desnecessariamente informações, comportamentos ou obrigações já estabelecidos, sem acrescentar valor.
- **Sem erro:** requisito que não recebeu alteração intencional para introduzir um defeito.

Utilize conceitos e boas práticas de Engenharia de Requisitos, considerando, quando aplicável, a norma ISO/IEC/IEEE 29148.

## 2. Procedimento de avaliação

Para cada requisito:

1. Leia o requisito original e sua tradução.
2. Leia a versão modificada que será apresentada aos modelos de IA.
3. Identifique a alteração realizada.
4. Verifique se a alteração realmente introduziu o erro indicado.
5. Avalie se o erro é suficientemente claro e tecnicamente defensável.
6. Verifique se a alteração introduziu outro tipo de erro diferente do planejado.
7. Considere o contexto do projeto e não apenas palavras isoladas.

**Atenção:** a presença de expressões vagas, condições complexas ou informações adicionais não comprova automaticamente a existência de um erro. A classificação deve ser fundamentada no significado e no efeito da alteração.

## 3. Avaliações anteriores — ChatGPT e Gemini

A planilha poderá conter colunas com avaliações anteriores realizadas pelo ChatGPT e pelo Gemini.

Você DEVE considerar essas avaliações, mas somente após realizar sua própria análise.

Siga obrigatoriamente esta ordem:

**Etapa A — Avaliação independente**

Analise o requisito sem utilizar as avaliações do ChatGPT ou do Gemini como referência para sua decisão.

**Etapa B — Comparação**

Leia as avaliações anteriores e compare com sua conclusão.

**Etapa C — Decisão final**

Determine se concorda ou discorda da categoria de erro atribuída pela autora.

Você pode concordar ou discordar de ambos os modelos. Sua decisão deve ser fundamentada exclusivamente em critérios técnicos.

Não altere sua conclusão apenas para obter concordância entre os modelos.

## 4. Preenchimento da planilha

Na aba "REQUISITOS DO TCC", crie uma coluna chamada **"Claude"**, imediatamente após as colunas de avaliação das outras IAs, sem sobrescrever os dados existentes.

Preencha a nova coluna utilizando exclusivamente:

- **Concordo:** quando o erro imputado corresponder tecnicamente à categoria indicada.
- **Discordo:** quando o erro não corresponder à categoria indicada, não tiver sido efetivamente introduzido ou não estiver suficientemente demonstrado.
- **Não se aplica:** quando o requisito estiver classificado como "Sem erro", ou seja, quando não houver erro intencional a ser validado.

**REGRA OBRIGATÓRIA:** todos os requisitos classificados como "Sem erro" devem receber "Não se aplica" na coluna Claude, independentemente de apresentarem possíveis problemas preexistentes.

Adicione também uma coluna **"Justificativa Claude"**, com uma explicação técnica objetiva para cada decisão.

Quando discordar, explique qual é o problema da classificação e, quando possível, indique a categoria mais adequada.

Nos casos de "Não se aplica", informe apenas que não houve erro intencional imputado. Caso identifique um defeito preexistente, poderá mencioná-lo na justificativa, sem alterar a resposta "Não se aplica".

Não reescreva os requisitos e não corrija os erros intencionais.

## 5. Preservação obrigatória do Excel

- Preserve integralmente todas as abas existentes.
- Não exclua requisitos.
- Não altere a ordem das linhas.
- Não modifique os identificadores dos projetos.
- Não altere os textos originais, traduções ou erros imputados.
- Não sobrescreva as avaliações do ChatGPT ou do Gemini.
- Preserve cores, bordas, fontes, mesclagens, larguras, fórmulas, filtros e demais formatações.
- Modifique exclusivamente o necessário para adicionar sua avaliação.

## 6. Relatório final

Após concluir a avaliação dos 166 requisitos, apresente:

1. Quantidade total de requisitos avaliados.
2. Quantidade de classificações com as quais concordou.
3. Quantidade de classificações com as quais discordou.
4. Quantidade de requisitos classificados como "Não se aplica".
5. Percentual de concordância com os erros imputados, excluindo os requisitos "Sem erro" do denominador.
6. Percentual de concordância entre Claude, ChatGPT e Gemini, considerando somente os casos com decisões comparáveis.
7. Distribuição das concordâncias e discordâncias por categoria de erro.
8. Identificação dos requisitos com erros mal caracterizados.
9. Recomendações para melhorar a qualidade técnica do experimento.

**IMPORTANTE:** não confunda concordância entre modelos com correção técnica. Dois ou mais modelos podem concordar e ainda assim estar tecnicamente equivocados.

## 7. Entrega

Devolva a planilha Excel completa, editada e pronta para download, preservando sua formatação original.

Não apresente apenas uma tabela no chat. A avaliação deve ser registrada diretamente no arquivo Excel.

Analise todos os 166 requisitos, sem pular linhas ou preencher avaliações por aproximação.

A qualidade técnica da análise é mais importante do que a concordância com as avaliações existentes.
