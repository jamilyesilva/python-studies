#utilizado para SALVAR e COMPARTILHAR dados
# "chaves":"valores" como em um dicionário Python
import json #biblioteca padrão python
#serve para transformar de objeto a JSON e de JSON a objeto Python, 
#   ou seja, para converter entre os dois formatos de dados.

import os #biblioteca para manipulação de arquivos e diretórios,
#   como criar, ler, escrever, excluir arquivos e diretórios e verificar a sua existencia  
#os.path.exists(comidas.txt) #verifica se o arquivo existe 
#--- bloco de codigo ---
#   if not os.path.exists("dados.json"):
#   with open("dados.json", "w") as arquivo:
#       json.dump([], arquivo) 


comidas = {
    "frutas": [
        {
            "nome": "maçã",
            "preco": 1.50
        },
        {
            "nome": "banana",
            "preco": 0.50
        }
    ]
}



# --- Usando DUMP e LOAD  ---
#json.dump() é usado para escrever um objeto Python em um arquivo JSON,
with open("json/comidas.json", "w", encoding="utf-8") as arqv:
     json.dump(comidas, arqv, ensure_ascii=False, indent=4)  
              #objeto, arquivo, caracteres especiais, indentação
              #indent=4 para formatar o JSON com indentação de 4 espaços,
              #ensure_ascii=False para permitir caracteres especiais, como acentos, no JSON.

#json.load() é usado para ler um arquivo JSON e convertê-lo em um objeto Python.
with open("json/comidas.json", "r", encoding="utf-8") as arqv:
    comidas_lidas = json.load(arqv)
    print(comidas_lidas)