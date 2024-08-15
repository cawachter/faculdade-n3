lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print (lista_mesclada)

lista_mesclada.append("Lista aninhada")
print (lista_mesclada)

lista_mesclada.insert(4, 5)
print (lista_mesclada)

print("Tamanho da lista: ", len(lista_mesclada))

del(lista_mesclada[1])
print (lista_mesclada)

nova_lista_mesclada = lista_mesclada[:5]
print("nova_lista_mesclada: ", nova_lista_mesclada)

