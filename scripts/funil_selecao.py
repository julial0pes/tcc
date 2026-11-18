"""Reproduz o funil de seleção dos projetos a partir do arquivo original da Promise+.

Uso:
    python scripts/funil_selecao.py dados/Promise+.arff

Critérios, aplicados em sequência sobre os requisitos funcionais (classe F) de cada projeto:
    1. pelo menos 35 requisitos funcionais;
    2. pelo menos 90% deles com verbo modal de obrigação (shall, must, should ou will);
    3. média de até 25 palavras por requisito.
As etapas 4 (projeto duplicado e documento em rascunho) e 5 (domínio de conhecimento geral)
foram aplicadas por leitura dos requisitos e estão listadas no fim da saída.
"""
import collections
import re
import sys

arquivo = sys.argv[1] if len(sys.argv) > 1 else 'dados/Promise+.arff'

requisitos = []
dentro_dos_dados = False
with open(arquivo, encoding='utf-8', errors='replace') as f:
    for linha in f:
        linha = linha.rstrip('\n')
        if linha.startswith('@DATA'):
            dentro_dos_dados = True
            continue
        if not dentro_dos_dados or not linha.strip():
            continue
        m = re.match(r"(\d+),'(.*)',?(\w+)\s*$", linha)
        if not m:
            raise ValueError(f'linha fora do padrão: {linha[:80]}')
        requisitos.append((int(m.group(1)), m.group(2), m.group(3)))

projetos = sorted({p for p, _, _ in requisitos})
funcionais = collections.defaultdict(list)
for p, texto, classe in requisitos:
    if classe == 'F':
        funcionais[p].append(texto)

print(f'Requisitos: {len(requisitos)} | projetos: {len(projetos)} | funcionais: {sum(len(v) for v in funcionais.values())}')


def obrigacao(texto):
    return bool(re.search(r'\b(shall|must|should|will)\b', texto, re.I))


resumo = {}
for p, textos in funcionais.items():
    n = len(textos)
    pct = 100 * sum(obrigacao(t) for t in textos) / n
    media = sum(len(t.split()) for t in textos) / n
    resumo[p] = (n, pct, media)

e1 = [p for p in resumo if resumo[p][0] >= 35]
e2 = [p for p in e1 if resumo[p][1] >= 90]
e3 = [p for p in e2 if resumo[p][2] <= 25]
print(f'Etapa 0 - projetos da base: {len(projetos)}')
print(f'Etapa 1 - pelo menos 35 funcionais: {len(e1)}')
print(f'Etapa 2 - pelo menos 90% com verbo de obrigação: {len(e2)}')
print(f'Etapa 3 - média de até 25 palavras: {len(e3)} -> {sorted(e3)}')
print()
print('Projeto | funcionais | % obrigação | média de palavras')
for p in sorted(e1):
    n, pct, media = resumo[p]
    print(f'{p:>7} | {n:>10} | {pct:>11.1f} | {media:>17.1f}')

excluidos_etapa4 = {46: 'cópia do projeto 67', 85: 'documento em rascunho, com marcadores como [company name]'}
excluidos_etapa5 = {55: 'controle de tráfego', 63: 'gestão de pontes (Pontis)', 68: 'sinalização ferroviária (ERTMS)',
                    70: 'dados de tráfego para órgão de transporte', 71: 'produtos de dados de satélite',
                    82: 'compras públicas eletrônicas (PEPPOL)'}
e4 = [p for p in e3 if p not in excluidos_etapa4]
e5 = [p for p in e4 if p not in excluidos_etapa5]
print()
print(f'Etapa 4 - sem duplicata nem rascunho: {len(e4)} (saem {excluidos_etapa4})')
print(f'Etapa 5 - domínio de conhecimento geral: {len(e5)} -> {sorted(e5)}')
print(f'Requisitos funcionais nos projetos escolhidos: {sum(resumo[p][0] for p in e5)}')
