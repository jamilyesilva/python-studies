import requests #importando a biblioteca requests para fazer requisições HTTP

#fazendo uma requisição GET para a URL fornecida
requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") #fazendo uma requisição GET para a URL fornecida
print(requisicao) #imprimindo o objeto de resposta da requisição
print(requisicao.json()) #imprimindo o conteúdo JSON da resposta
dicionario = requisicao.json() #armazenando o conteúdo JSON da resposta em um dicionário
print(dicionario["USDBRL"]["bid"]) #imprimindo o valor associado ao 'bid' dentro do USDBRL no dicionário
print("-"*30)

