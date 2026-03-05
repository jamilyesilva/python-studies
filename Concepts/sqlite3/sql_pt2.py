# objetivo é avançar nos conceitos de sql
# 1 - importar sql
# 2 - criar banco de dados e guardar em uma variavel
def conexao_db():
    import sqlite3 as sql 
    with sql.connect("Concepts/sqlite3/Restarante.db"):
        conn = conn.cursor()
    return 

# 3 - abrir db e criar tabelas
def create_table():
    conn = conexao_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
                id INTENGER PRIMARY KEY AUTOINCREMENT
                 )
    """)
# 4 - conectar tabelas
# 5 - implementar CRUD