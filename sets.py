set_inicial = {11, 12, 13, 14}
print(set_inicial)

set_inicial.add(15)
print(set_inicial)

set_inicial.update({1,2,3,4,5})
print(set_inicial)

set_inicial.discard(13)
print(set_inicial)

novo_set = {20,21,23,1,2}
print("Conteúdo do novo_set:", novo_set)

uniao = set_inicial.union(novo_set)
print("União entre set_inicial e novo_set:", uniao)

intersecao = set_inicial.intersection(novo_set)
print("Interseção do set_inicial e novo_set:", intersecao)

diferenca = set_inicial.difference(novo_set)
print("Diferença do set_inicial e do novo_set:", diferenca)

diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre set_inicial e do novo_set:", diferenca_simetrica)


