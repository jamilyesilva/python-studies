#iterar categorias
#um objeto/coleção que pode retornar seus valores, no caso, pode ser percorrido em um loop
#EXEMPLOS = 
lista = [1, 2, 3]
string = "jami"
dicionario = {"a": 1, "b": 2}
tupla = (10, 20)
#range() e set() tambem são iterable

#keys(), values(), items()
for item in dicionario.values():
    print(item)
for item in dicionario.keys():
    print(item)
for item in dicionario.items():
    print(item)
# usado para percorrer itens, repetção, processar dados

#ITERABLE VS ITERATOR
#   iterable é o objeto que pode percorrido, se funciona com for é iterable
#   iterator é o objeto que entrega valor um por um, o for usa o iterator automaticamente
iterador = iter(tupla)

print(next(iterador))  # 1
print(next(iterador))  # 2



# iterar categorias + listas

