# dicionario e uma lista juntos
#aqui é um dicionario com lista dentro, melhor para itens
produtos = {
    "frutas": [],
    "verduras": []
    }
# exemplo de um dicionario onde vada chave guarda um valor tipo lista

#  COMO ACESSAR CORRETAMENTE??
#acessamos atraves da chave (variavel["chave"])
print(produtos) #mostrando as chaves e os valores - no caso, listas -
print(produtos["frutas"]) # acessando tudo de frutas, atraves da chave e os [] mostrando que é uma lista
produtos["frutas"].append("morango") #forma de adicionar item
print(produtos["frutas"])
print('-----------')




#DICIONARIO DENTRO DA LISTA
#aqui é uma lista com dicionarios, cada elemente é um dicionario
# imprtante para guardar  itens com dados especificos cada com chaves especificas
frutas = [
    {"nome": "morango", "preco": 15},
    {"nome": "banana", "preco": 5}
]

#COMO ACESSAR CORRETAMENTE?
#atraves do index, pois é uma lista
print(frutas[1]) # retorna o dicionario no index 1
#depois você pode buscar um item em uma chave em especifico dentro do dicionario
print(frutas[0]["nome"])# index + chave que você quer acessar
print('-----------')
