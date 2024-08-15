meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

print(meu_dicionario)

print(type(meu_dicionario))

# As chaves precisam ser unicas
# Nao tem como imprimir o valor da chave linguagem
# O campo chave nao pode se chamar linguagem
# imprimindo o valor da chave 1
print(meu_dicionario.get(1))

print("tamanho do dicionario: ", len(meu_dicionario))

dicionario_frutas = dict(
    {
        1: {"nome": "limao", "tipo": "acida"},
        2: {"nome": "laranja", "tipo": "acida"},
        3: {"nome": "manda", "tipo": "semiacida"},
        4: {"nome": "maça", "tipo": "semiacida"},
        5: {"nome": "banana", "tipo": "doce"},
        6: {"nome": "mamão", "tipo": "doce"},     
    
    }

)

chave_1 = dicionario_frutas[1]
chave_2 = dicionario_frutas[2]

print(f"Chave 1: Nome: {chave_1['nome']}, Tipo: {chave_1['tipo']}")
print(f"Chave 2: Nome: {chave_2['nome']}, Tipo: {chave_2['tipo']}")

for chave, fruta in dicionario_frutas.items():
    print(f"Nome: {fruta['nome']} | Tipo: {fruta['tipo']}")