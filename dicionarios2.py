dicionario = {
    1: {"nome": "Maria", "idade": 26, "nacionalidade": "brasileira"}
}

print("Primeiro dicionario: ", dicionario)

mais_chaves = {
    1: {"nome": "Maria", "idade": 26, "nacionalidade": "brasileira", "cidade": "Porto Alegre", "profissao": "Professora"},
    2: {"nome": "Carla", "idade": 30, "nacionalidade": "brasileira", "cidade": "Canoas", "profissao": "Advogada"},
    3: {"nome": "Lucas", "idade": 22, "nacionalidade": "francesa", "cidade": "Lyon", "profissao": "Professor"},
    4: {"nome": "Carlos", "idade": 50, "nacionalidade": "espanhola", "cidade": "Madrid", "profissao": "Engenheiro"},
}
dicionario.update(mais_chaves)

print("Dicionario apos update: ",dicionario)

dicionario_copia = dicionario.copy()

print("Dicionario copia: ", dicionario_copia)

dicionario.pop(1)
print("Dicionario apos remover primeiro elemento: ", dicionario)

dicionario.popitem()
print("Dicionario apos remover ultimo elemento: ", dicionario)

dicionario.clear()
dicionario_copia.clear()

novas_chaves = ["chave1", "chave2", "chave3", "chave4"]
dicionario_novo = dict.fromkeys(novas_chaves, "sem valor")
print(dicionario_novo)

print(dicionario_novo.items())
print(dicionario_novo.keys())
print(dicionario_novo.values())