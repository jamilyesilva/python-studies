import sqlite3 as sql #importando sql para persistencia de dados
# print(dir(sql))
#dentro do python, para voce conversar com o arquivo, você utiliza um cursor
# ex: a conexão é o tunel e o cursor é o carrinho trazendo e levando dados

# UTILIZAR 
def conexao_db():
    conexao = sql.connect("Concepts/sqlite3/Escola.db")
    # para não se preocupar em fechar a conexã, utilize o with como no JSON
    # with sql.connect("Concepts/sqlite3/Escola.db") as coon:
        # cursor = coon.cursor() # e ai voce vai seguindo em frente b
    return conexao 

def create_table():
    conn = conexao_db()
    cursor = conn.cursor()
    #pt 1 - CRIANDO O BD, INSERINDO DADOS E ATUALIZANDO
    table = cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
                    )
            """)
    conn.commit()
    conn.close()

def cadastro_db(name, age):
    conn = conexao_db()
    cursor = conn.cursor()
# INSERINDO dados
    cursor.execute("""
        INSERT INTO alunos
                (nome, idade)  VALUES (?,?)""", (name, age))
    # SALVANDO alteração
    conn.commit()
    #Fechando conexão
    conn.close()
    # conexao.close()

def read_db():
    conn = conexao_db()
    cursor = conn.cursor()
    # PT 2 - LENDO DADOS 
    cursor.execute("""  SELECT * FROM alunos""") # puxando todos os dados
    resultados = cursor.fetchall() 
    for linha in resultados:
        print(f"ID: {linha [0]} | Nome: {linha [1]} | Idade: {linha [2]}")

    conn.commit()
    conn.close()

