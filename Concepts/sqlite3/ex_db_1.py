import sqlite3 as sql #importando sql para persistencia de dados
# print(dir(sql))
#dentro do python, para voce conversar com o arquivo, você utiliza um cursor
# ex: a conexão é o tunel e o cursor é o carrinho trazendo e levando dados

# UTILIZAR 

conexao = sql.connect("Concepts/sqlite3/Escola.db")
# para não se preocupar em fechar a conexã, utilize o with como no JSON
# with sql.connect("Concepts/sqlite3/Escola.db") as coon:
    # cursor = coon.cursor() # e ai voce vai seguindo em frente 
cursor = conexao.cursor() # criar o cursor para executar comandos

#pt 1 - CRIANDO O BD, INSERINDO DADOS E ATUALIZANDO
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
            )
""")
# INSERINDO dados
cursor.execute("""
    INSERT INTO alunos
               (nome, idade)  VALUES ("jamily", 18), ("jay", 17)
""")
# SALVANDO alteração
conexao.commit()
#Fechando conexão

# conexao.close()


# PT 2 - LENDO DADOS 
cursor.execute("""
                SELECT * FROM alunos
""") # puxando todos os dados
resultados = cursor.fetchall() 

for linha in resultados:
    print(f"ID: {linha [0]} | Nome: {linha [1]} | Idade: {linha [2]}")

