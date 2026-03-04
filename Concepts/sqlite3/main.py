from ex_db_1 import create_table, cadastro_db, read_db
#executando o que foi aprendido 

#nome
#idade
def valid_type(tipo, mensagem):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print("Tipo de valor incorreto")
    

def cadastro():
        print("---- Formulário ----")
        name = input("Nome: ").lower()
        age = valid_type(int, "Idade: ")
        cadastro_db(name, age)


def read_dates():
    read_db()

def menu():
    create_table()
    while True:
        print("Bem-Vindo!")
        print("1 - Cadastrar Usuário")
        print("2 - Ver Dados")
        print("0 - Sair")
        opcao = valid_type(int, "opção: ")
        if opcao == 1:
            cadastro()
        elif opcao == 2:
            read_db()
        elif opcao == 0:
            print("Saindo")
            break
        else: 
            print("Opção inexistente ou incorreta")

menu()