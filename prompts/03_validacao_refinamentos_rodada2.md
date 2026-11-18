# Prompt 3 — Validação independente dos refinamentos (rodada 2)

**Etapa:** validação dos erros pelas IAs, rodada 2 (seção 8.3 do README).
**Usado com:** Gemini e Claude, cada um em conversa nova. O ChatGPT não participou desta rodada porque foi ele quem fez o refinamento avaliado aqui.
**Entrada:** planilha com a aba "REQUISITOS DO TCC". O texto refinado está na coluna M ("CHATGPT - Erro refinado após discordância (rodada 2)").

O mesmo texto foi enviado às duas IAs. A versão abaixo é a que foi enviada ao Claude. Para o Gemini, mudam apenas o nome do modelo e as colunas a preencher (N para o Gemini; O e P para o Claude).

---

# PROMPT PARA CLAUDE — VALIDAÇÃO INDEPENDENTE DOS REFINAMENTOS (RODADA 2)

Analise a planilha Excel anexada, especificamente a aba **"REQUISITOS DO TCC"**, e realize uma avaliação técnica, criteriosa e totalmente independente dos requisitos refinados.

## 1. Objetivo

Verificar se cada requisito refinado apresenta efetivamente o erro indicado na coluna **E — Situação**, utilizando os conceitos e as boas práticas de Engenharia de Requisitos, considerando, quando aplicável, a norma ISO/IEC/IEEE 29148.

A análise deverá considerar:

- **Coluna C:** requisito original.
- **Coluna E:** situação ou categoria do erro.
- **Coluna F:** erro imputado manualmente.
- **Coluna M:** texto refinado que deverá ser avaliado.

**Atenção:** utilize os cabeçalhos para confirmar a localização do texto refinado. Caso ele esteja em outra coluna, identifique a posição correta antes de iniciar a avaliação.

## 2. Independência da avaliação — OBRIGATÓRIO

Sua avaliação deverá ser realizada exclusivamente com base no seu próprio julgamento técnico.

**Não considere as classificações, avaliações ou justificativas anteriores do ChatGPT, Gemini ou Claude.**

Os requisitos foram refinados após avaliações anteriores, mas isso NÃO significa que os erros estejam corretos.

Portanto:

- Não concorde apenas porque o requisito foi refinado.
- Não procure confirmar decisões anteriores.
- Não utilize as justificativas das outras IAs como fundamento.
- Não presuma que a situação indicada na coluna E está correta.
- Não tente alcançar consenso artificial entre os modelos.
- Não favoreça a concordância ou a discordância.

Se identificar que um refinamento continua tecnicamente inadequado, registre **"Discordo"**, independentemente de qualquer avaliação anterior.

## 3. Critérios técnicos

**Ambiguidade:** o requisito permite duas ou mais interpretações plausíveis sobre o comportamento esperado. Não confunda ambiguidade com contradição ou mera ausência de detalhes.

**Incompletude:** o requisito omite informações essenciais para compreender, implementar ou verificar o comportamento esperado. Não classifique como incompleto apenas porque poderia conter mais detalhes.

**Inviabilidade:** o requisito estabelece uma condição tecnicamente impossível ou inviável no contexto apresentado. Não confunda inviabilidade com dificuldade de implementação ou custo elevado.

**Redundância:** o requisito apresenta repetição desnecessária de uma informação, comportamento ou obrigação. Não confunda redundância com funcionalidades semelhantes que possuem finalidades diferentes.

**Sem erro:** não apresenta erro intencional imputado.

## 4. Procedimento de validação

Para cada linha:

1. Leia o requisito original para compreender a funcionalidade.
2. Identifique a categoria indicada na coluna E.
3. Leia o texto refinado.
4. Avalie se a modificação introduziu um defeito real de Engenharia de Requisitos.
5. Verifique se o defeito corresponde especificamente à categoria indicada.
6. Registre sua conclusão independente.

Não basta o requisito apresentar algum problema: **o problema precisa corresponder à categoria da coluna E**.

## 5. Preenchimento obrigatório do Excel

### Coluna O — Validação Claude (Rodada 2)

Preencha exclusivamente com uma das seguintes opções:

- **Concordo:** o texto refinado apresenta efetivamente o erro indicado na coluna E.
- **Discordo:** o texto não apresenta o erro indicado, apresenta outro tipo de erro ou não há evidências técnicas suficientes para confirmar a classificação.
- **Não se aplica:** não existe texto refinado naquela linha.

### Coluna P — Justificativa Claude (Rodada 2)

Apresente uma justificativa técnica individualizada, explicando o motivo da concordância ou discordância.

Para as discordâncias, identifique precisamente o problema e explique o que impede o enquadramento na categoria indicada.

Para os casos "Não se aplica", utilize: "Requisito não submetido à segunda rodada de refinamento".

**Não escreva avaliações em nenhuma outra coluna.**

## 6. Preservação da planilha — OBRIGATÓRIO

- Preserve todas as abas existentes.
- Preserve todos os 166 requisitos e sua ordem.
- Não altere nenhum texto original.
- Não altere os erros imputados manualmente.
- Não modifique os textos refinados.
- Não altere a coluna E.
- Não altere as avaliações anteriores das outras IAs.
- Não insira ou exclua linhas.
- Não desloque as colunas existentes.
- Não sobrescreva fórmulas ou informações.
- Preserve cores, bordas, fontes, alinhamentos, filtros, larguras e alturas das células.

**Somente as colunas O e P poderão ser preenchidas ou atualizadas.**

Utilize a seguinte formatação na coluna O:

- Verde: Concordo.
- Vermelho: Discordo.
- Cinza: Não se aplica.

## 7. Relatório final

Após concluir, apresente:

1. Total de requisitos analisados.
2. Quantidade de refinamentos efetivamente avaliados.
3. Quantidade de concordâncias.
4. Quantidade de discordâncias.
5. Quantidade de casos "Não se aplica".
6. Percentual de concordância entre os refinamentos avaliados.
7. Distribuição das discordâncias por categoria de erro.
8. Identificação dos requisitos que ainda precisam de ajustes.

## 8. Entrega

Devolva o arquivo Excel completo e atualizado, mantendo sua estrutura e formatação original.

**REGRA FINAL:** sua função é avaliar, e não corrigir os requisitos. Não modifique nenhum refinamento. Caso discorde, registre "Discordo" na coluna O e apresente a justificativa na coluna P.

A independência e o rigor técnico da avaliação são mais importantes do que a quantidade de concordâncias.