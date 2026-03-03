arquivo = open("json/manipulando_arqv/nomes.txt", "a", encoding="utf-8") 
#cria o arquivo se ainda não existir, abre para escrita
#encoding serve para evitar erros de acentos, caracteres especiais, etc



# ---TIPOS DE ABERTURA DE ARQUIVOS---
# o W não acrescenta, só substitue o conteúdo do arquivo, ou seja, apaga o que já tem e escreve o novo conteúdo
# o a acrescenta, ou seja, mantém o conteúdo do arquivo e acrescenta o novo conteúdo no final do arquivo
# o x cria um novo arquivo, mas se o arquivo já existir, ele gera um erro
# arquivo.write("Alana - 108\n") #escreve no arquivo, \n para pular linha
arquivo.close() #fecha o arquivo, é importante para evitar perda de dados e liberar recursos do sistema


#Você pode abrir o arquivo com o with, que é uma forma mais segura de lidar com arquivos, 
# pois garante que o arquivo será fechado corretamente, mesmo que ocorra um erro durante 
# a manipulação do arquivo. Exemplo:
with open("json/manipulando_arqv/nomes.txt", "a", encoding="utf-8") as arqv:
    # arqv.write("Miguel\n")
    pass


# --- Leitura de arquivos ---
with open("json/manipulando_arqv/nomes.txt", "r", encoding="utf-8") as arqv: 
    # conteudo = arqv.read() 
    #read() lê todo o conteúdo do arquivo e guarda na variável conteudo
    # content_lines = arqv.readlines()
    #readlines() lê o conteúdo do arquivo e guarda cada linha em uma lista, 
    #            ou seja, cada elemento da lista é uma linha do arquivo
    # print(type(conteudo))
    # print(type(content_lines))
    # for line in content_lines:
    #     print(line.strip()) #strip() remove os espaços em branco no início e no final da string, 
                            # ou seja, remove os caracteres de nova linha (\n) que são adicionados 
                            # ao final de cada linha lida do arquivo
    pass


# --- Leitura e escrita de arquivos ---
#se quer ler e escrever, basta muar o modo de abertura para "r+" ou "a+" ou "w+", 
# dependendo do comportamento desejado (leitura e escrita, leitura e escrita com 
# acréscimo, leitura e escrita com substituição, respectivamente). Exemplo:

# 01 - R+
# with open("json/manipulando_arqv/nomes.txt", "r+", encoding="utf-8") as arqv:
#     conteudo = arqv.read()
#     print(conteudo)
#     arqv.write("Alice\n")
#     print("---- ")

# 02 - W+
with open("json/manipulando_arqv/nomes.txt", "w+", encoding="utf-8") as arqv:
    arqv.write("Angel\n")
    arqv.seek(0)  # move o cursor para o início do arquivo
     # O método seek() é usado para mover o cursor de leitura/escrita para uma posição
     #                 específica no arquivo.
     # O argumento 0 indica que o cursor deve ser movido para o início do arquivo
    conteudo = arqv.read()
    #sem o seek(), aqui o conteudo nao iria mostrar pois o cursor fica parado no final do arquivo
    # depois de escrever, ou seja, o cursor está no final do arquivo, então quando 
    # você tenta ler o conteúdo do arquivo, ele não encontra nada para ler, pois o 
    # cursor já está no final do arquivo.
    print(conteudo) 
    
    