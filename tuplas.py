primeira_tupla = (1, 2, 3, 4, "Olá, tupla")
print(primeira_tupla)
print("O elemento 4 esta no indice: ", primeira_tupla.index(4))

print(3 in primeira_tupla)

if 3 in primeira_tupla:
    print("O elemento 3 esta na tupla!")
else:
    print("O elemento 3 nao esta na tupla!")

if 33 in primeira_tupla:
    print("O elemento 33 esta na tupla!")
else:
    print("O elemento 33 nao esta na tupla!")
