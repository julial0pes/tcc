"""Recalcula, a partir da planilha do experimento, os números citados no README e no TCC.

Uso:
    pip install openpyxl
    python scripts/conferir_numeros.py dados/planilha_do_experimento.xlsx
"""
import collections
import sys

import openpyxl

arquivo = sys.argv[1] if len(sys.argv) > 1 else 'dados/planilha_do_experimento.xlsx'
wb = openpyxl.load_workbook(arquivo, read_only=True)

# ---------------------------------------------------------------- aba APENAS FUNCIONAIS
linhas = list(wb['APENAS FUNCIONAIS'].iter_rows(min_row=2, values_only=True))
linhas = [ln for ln in linhas if ln[0]]
print(f'APENAS FUNCIONAIS: {len(linhas)} requisitos')


def classe_original(ln):
    texto = str(ln[0]).rstrip()
    resto = texto[texto.rfind("'") + 1:].replace(',', '').strip()
    return 'F' if resto == 'F' else 'NF'


avaliacoes = {'Promise+ (original)': [classe_original(ln) for ln in linhas],
              'Gemini': [ln[5] for ln in linhas], 'ChatGPT': [ln[6] for ln in linhas], 'Claude': [ln[7] for ln in linhas]}
for nome, valores in avaliacoes.items():
    c = collections.Counter(valores)
    print(f'  {nome:<20} F = {c["F"]:>5}   NF = {c["NF"]:>5}')
concordancia = collections.Counter()
for i in range(len(linhas)):
    votos = collections.Counter(v[i] for v in avaliacoes.values())
    concordancia[f'{max(votos.values())}/4'] += 1
print('  Concordância:', dict(sorted(concordancia.items(), reverse=True)))

# ---------------------------------------------------------------- aba REQUISITOS DO TCC
tcc = [ln for ln in wb['REQUISITOS DO TCC'].iter_rows(min_row=2, values_only=True) if ln[0] is not None]
print(f'\nREQUISITOS DO TCC: {len(tcc)} requisitos')
cat = lambda ln: str(ln[4]).replace('Com erro: ', '').strip()
print('  Por projeto e situação:')
for proj in sorted({int(ln[0]) for ln in tcc}):
    c = collections.Counter(cat(ln) for ln in tcc if int(ln[0]) == proj)
    print(f'    projeto {proj:>2}: {dict(c)}')
print('  Total por situação:', dict(collections.Counter(cat(ln) for ln in tcc)))

print('\n  Rodada 1 (Concordo/Discordo por modelo e categoria):')
for nome, col in (('ChatGPT', 6), ('Gemini', 7), ('Claude', 8)):
    res = {}
    for c in ('Ambiguidade', 'Incompletude', 'Inviabilidade', 'Redundância'):
        vals = collections.Counter(str(ln[col]).strip() for ln in tcc if cat(ln) == c)
        res[c] = (vals['Concordo'], vals['Discordo'])
    print(f'    {nome:<8} {res}')
com_discordancia = [ln for ln in tcc if 'Discordo' in (str(ln[6]).strip(), str(ln[7]).strip(), str(ln[8]).strip())]
print(f'  Requisitos com ao menos uma discordância: {len(com_discordancia)}')
print('  Rodada 2 - Gemini:', dict(collections.Counter(str(ln[13]).strip() for ln in com_discordancia)),
      '| Claude:', dict(collections.Counter(str(ln[14]).strip() for ln in com_discordancia)))
sugestoes = [ln for ln in tcc if ln[16]]
print(f'  Sugestões do Claude: {len(sugestoes)} | ChatGPT:', dict(collections.Counter(str(ln[17]).strip() for ln in sugestoes)),
      '| Gemini:', dict(collections.Counter(str(ln[19]).strip() for ln in sugestoes)))


def origem(ln):
    final = str(ln[21]).strip()
    if 'Sem erro' in str(ln[4]):
        return 'tradução'
    if ln[16] and final == str(ln[16]).strip():
        return 'sugerido pelo Claude'
    if ln[12] and final == str(ln[12]).strip():
        return 'refinado pelo ChatGPT'
    return 'inserido pela autora'


print('  Origem do texto final:', dict(collections.Counter(origem(ln) for ln in tcc)))

# ---------------------------------------------------------------- linha de base ingênua
com_defeito = sum(1 for ln in tcc if 'Com erro' in str(ln[4]))
precisao = com_defeito / len(tcc)
f1 = 2 * precisao * 1 / (precisao + 1)
print(f'\nLinha de base "marcar tudo como defeito": precisão {precisao:.3f}, revocação 1.000, F1 {f1:.3f}')
