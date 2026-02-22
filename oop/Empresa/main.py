from funcionarios import Funcionarios as F
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


#metodos
def add_f():
    print("____"*2)
    nome = input("nome: ").lower()
    setor = input("setor: ").lower()
    cargo = input("cargo: ").lower()
    salario = input("salario: ")

    new_f = {"nome": nome, "setor": setor, "cargo": cargo, "salario": salario} # typagem que nao pode faltar kkkk
    add_to_dict = F.to_dict(new_f)
    print(add_to_dict) 

def list_f():
    pass

def del_f():
    pass
    
    
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
        F.add_f()
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass
    elif escolha == 0:
        break
    else:
        print('Valor Incorreto')


        
