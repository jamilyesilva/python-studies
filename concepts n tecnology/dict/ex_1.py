#criando iterator
#como funciona por tras do for que utilizamos

# Iterator = anda para frente e não volta, ele nao volta sozinho
# Iterable = pode gerar novos iterators, por isso ele pode percorrer uma lista varias vezes
#generador = é como o iterator, mas mais sofisticado. Ele vai marcando points 

# numeros = [10, 20, 30]

# valor = iter(numeros)

# while True:
#     try:
#         print(next(valor))
#         print(next(valor))
#         print(next(valor))
#         print(next(valor))
#         print(next(valor))
#     except StopIteration:
#         print("acabaram os elementos")
#     break


numeros = [10, 20, 30]
it = iter(numeros)

for n in it:
    print(n)

for n in it:
    print(n)

def gerar_numeros():
    yield 1
    yield 2
    yield 3
    yield 4


g = gerar_numeros() #Generators é uma forma elegante de criar iterators
for i in g:
    print(i)
    print(type(g)) 

# Lista → coleção pronta
# Iterable → algo que pode gerar iterator, algo a ser percorrido
# Iterator → objeto que sabe andar elemento por elemento, que percorre
# Generator → forma automática de criar iterator usando yield

# #o iterator serve para percorrer item por item um de cada vez
# os iterator percorrem um item d ecada vez, e é comumente utilizado em CRUD, DB, API ao utilizarmos o for