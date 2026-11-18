# Prompt 1 — Classificação dos requisitos em Funcionais (F) e Não Funcionais (NF)

**Etapa:** validação dos requisitos funcionais (seção 5 do README).
**Usado com:** ChatGPT, Gemini e Claude, um de cada vez, sempre em conversa nova.
**Entrada:** planilha com a aba "APENAS FUNCIONAIS" (3.677 requisitos da Promise+).

O mesmo texto foi enviado às três IAs. A versão abaixo é a que foi enviada ao Claude. Para o ChatGPT e o Gemini, mudam apenas o nome do modelo e a coluna a preencher (F para o Gemini, G para o ChatGPT e H para o Claude).

---

Analise a planilha Excel anexada, especificamente a aba **"APENAS FUNCIONAIS"**, e realize uma avaliação técnica, criteriosa e completamente independente de todos os requisitos apresentados.

## Objetivo

Classificar individualmente todos os requisitos como **Funcionais (F)** ou **Não Funcionais (NF)**, utilizando exclusivamente seu próprio conhecimento técnico sobre Engenharia de Requisitos e Engenharia de Software.

Esta será uma **quarta avaliação independente**, realizada pelo Claude, sem influência das classificações anteriores.

## 1. Identificação dos requisitos

- Localize a coluna que contém as descrições dos requisitos na aba "APENAS FUNCIONAIS".
- Leia integralmente cada requisito, considerando seu significado, finalidade e comportamento esperado.
- Analise todas as linhas preenchidas, sem ignorar ou agrupar requisitos.
- Não utilize as classificações existentes em outras colunas para interpretar os requisitos.

## 2. Independência da análise — REGRA OBRIGATÓRIA

A planilha contém classificações realizadas anteriormente pelo autor original, pelo Gemini e pelo ChatGPT.

**Você deve ignorar completamente todas essas classificações.**

- Não utilize as respostas do Gemini como referência.
- Não utilize as respostas do ChatGPT como referência.
- Não utilize a classificação original do autor.
- Não compare suas conclusões com as classificações existentes durante a análise.
- Não tente produzir respostas semelhantes ou diferentes propositalmente.
- Não considere a quantidade de requisitos classificados como F ou NF pelas outras avaliações.

**Sua única fonte para decidir a classificação deve ser a descrição textual do requisito, interpretada a partir dos conceitos técnicos de Engenharia de Requisitos.**

## 3. Classificação — Coluna H

Preencha exclusivamente a **coluna H**, com o cabeçalho **"Claude"**, utilizando:

- **F — Funcional:** Requisitos que especificam funcionalidades, comportamentos, operações, regras de negócio, processos ou serviços que o sistema deve executar.
- **NF — Não Funcional:** Requisitos que estabelecem atributos de qualidade, desempenho, segurança, confiabilidade, disponibilidade, usabilidade, escalabilidade, manutenibilidade ou restrições técnicas e operacionais.

Cada requisito deverá receber uma única classificação: F ou NF.

## 4. Critérios técnicos

Utilize conceitos consolidados de Engenharia de Software e Engenharia de Requisitos, considerando, quando aplicável, a ISO/IEC/IEEE 29148.

Para cada requisito:

1. Identifique o que está sendo solicitado.
2. Determine se o requisito descreve um comportamento ou funcionalidade do sistema ou uma característica de qualidade/restrição.
3. Considere o contexto e o significado completo da descrição.
4. Não classifique com base apenas em palavras-chave.
5. Quando houver características funcionais e não funcionais simultaneamente, identifique a natureza predominante.
6. Realize uma avaliação individual, evitando generalizações ou classificações em massa.

**Importante:** Requisitos relacionados a segurança, autenticação, validação, desempenho ou integração não são automaticamente funcionais ou não funcionais. A classificação depende do comportamento ou atributo efetivamente especificado.

## 5. Qualidade e profundidade da análise

Não quero uma classificação superficial baseada em padrões de palavras ou expressões.

Quero uma **análise semântica individual de cada requisito**, considerando sua finalidade e natureza técnica.

Não utilize regras simplificadas, como classificar automaticamente requisitos que contenham determinados verbos ou termos.

Caso existam milhares de requisitos, processe-os em lotes, se necessário, garantindo que todos sejam efetivamente analisados.

Priorize a precisão técnica, mesmo que isso exija maior tempo de processamento.

## 6. Preservação da planilha

- Não altere nenhuma informação das colunas A até G.
- Não modifique as descrições originais.
- Não altere as classificações do autor, Gemini ou ChatGPT.
- Não exclua linhas ou colunas.
- Não reorganize a ordem dos requisitos.
- Preserve as demais abas e a formatação existente.
- Preencha exclusivamente a coluna H.

## 7. Verificação final

Após concluir todas as classificações:

- Verifique se todos os requisitos receberam uma classificação na coluna H.
- Confirme que não existem linhas com requisitos sem classificação.
- Confira se cada resposta corresponde à linha correta.
- Verifique se nenhuma informação das colunas A até G foi modificada.
- Não altere suas classificações para coincidir com as avaliações anteriores.

## Resultado esperado

Entregue a planilha Excel atualizada contendo a coluna H preenchida com suas próprias classificações.

Ao final, informe também:

- Quantidade total de requisitos analisados.
- Quantidade classificada como Funcional (F).
- Quantidade classificada como Não Funcional (NF).
- Quantidade de requisitos que apresentaram ambiguidade técnica, se identificados.

## ORIENTAÇÃO FINAL — EXTREMAMENTE IMPORTANTE

**Claude, esta avaliação deve representar exclusivamente seu próprio julgamento técnico.**

Não quero que você valide o Gemini, o ChatGPT ou o autor original.

Quero que você atue como um especialista independente em Engenharia de Requisitos, analisando cada descrição e chegando às suas próprias conclusões.

**Não consulte as classificações anteriores antes de finalizar todas as suas decisões.**

O objetivo é obter quatro avaliações independentes que poderão ser comparadas posteriormente, sem que uma influencie a outra.

Ao finalizar, disponibilize o arquivo Excel atualizado para download.
