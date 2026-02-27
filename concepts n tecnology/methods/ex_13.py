estoque = []

estoque.append("banana")
estoque.append("uva")
estoque.append("morango") 

if len(estoque) > 2:
    estoque.pop(0)
    print(estoque)
else:
    print('Só há 2 itens')
    print(estoque)