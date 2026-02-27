import sqlite3 as sql #importando sql para persistencia de dados
# print(dir(sql))

conexao = sql.connect("Escola.db")
cursor = conexao.cursor()

#table aluno
cursor.execute("""
    CREATE TABLE alunos(
            id INTENGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTENGER NOT NULL
            )
""")

cursor.execute("""
    INSERT INTO alunos VALUES(
            "jami", 18)
""")

