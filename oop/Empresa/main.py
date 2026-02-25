from funcionarios import Gerentes as G
from funcionarios import Estagiarios as E
from funcionarios import Config as C
#CRUD Funcionarios
# nome, setor, cargo, horario, salario
#config
def valida_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

def valida_decimal(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")


#metodos
def add_f():
    print("____"*2)
    tipo = valida_int(" (1) - Gerente | (2) - Estágiario\n opção= ")
    if tipo == 1:
        nome = input("nome: ").lower()
        setor = input("setor: ").lower()
        cargo = input("cargo: ").lower()
        salario = valida_decimal("salario: ")
        bonus = valida_int("bonus (%): ")
        new_f = G(nome, setor, cargo, salario, bonus = bonus) # typagem que nao pode faltar kkkk
        add = C("oop/Empresa/database_f.json", [])
        add.add_f(new_f.to_dict())
    elif tipo == 2:
        nome = input("nome: ").lower()
        setor = input("setor: ").lower()
        cargo = input("cargo: ").lower()
        salario = valida_decimal("salario: ")
        limite_horas = valida_int("carga horaria (d): ")
        new_f = E(nome, setor, cargo, salario, limite_horas = limite_horas)
        add = C("oop/Empresa/database_f.json", [])
        add.open_json()
        add.add_f(new_f.to_dict())
    else:
        print("Valor Incorreto, Por Favor, digite apenas (1) ou (2)")
   

def list_f():
    print('----Lista de Usuarios ----')
    lista = C("oop/Empresa/database_f.json", [])
    lista.open_json()
    print(lista.to_list_f())

def del_f():
    print('----Deletando Usuario ----')
    f = input('Informe o nome do usuario para exclusão:\n nome = ')
    delete_f = C("oop/Empresa/database_f.json", [])
    delete_f.open_json()
    delete_f.remove_f()

    
    
while True:
    print("----- Ala Funcionarios-----")
    print(""" 
          1 - Adicionar Novo Funcionario \n
          2 - Listar Funcionarios \n
          3 - Excluir Funcionario \n
          0 - Sair    
    """)
    escolha = valida_int('escolha : ')
    if escolha == 1:
      #chamar metodo para colocar os atributos e depois salvar 
        add_f()
    elif escolha == 2:
        list_f()
    elif escolha == 3:
        del_f()
    elif escolha == 0:
        break
    else:
        print('Valor Incorreto')


        
