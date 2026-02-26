from funcionarios import Gerentes as G
from funcionarios import Estagiarios as E
from funcionarios import Config as C
#CRUD Funcionarios
# nome, setor, cargo, horario, salario
#config
def valida_tipo(tipo, mensagem): #evitando funções repetitivas
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

#metodos
def add_f(): # fazer uma função aq
    print("____"*2)
    tipo = valida_tipo(int," (1) - Gerente | (2) - Estágiario\n opção= ")
    if tipo == 1:
        nome = input("nome: ").lower()
        setor = input("setor: ").lower()
        cargo = input("cargo: ").lower()
        salario = valida_tipo(float, "salario: ")
        bonus = valida_tipo(int, "bonus (%): ")
        new_f = G(nome, setor, cargo, salario, bonus = bonus) # utilizamos kwargs, logo na assintura da classe definirmos o campo LIMITE_HORAS para não confundir o dict DIQXY
        add = C("oop/Empresa/Gerente_db.json")
        add.open_json()
        add.add_f(new_f.to_dict())
    elif tipo == 2:
        nome = input("nome: ").lower()
        setor = input("setor: ").lower()
        cargo = input("cargo: ").lower()
        salario = valida_tipo(float, "salario: ")
        limite_horas = valida_tipo(int, "carga horaria (d): ")
        new_f = E(nome, setor, cargo, salario, limite_horas = limite_horas)
        add = C("oop/Empresa/Estagiario_db.json")
        add.open_json()
        add.add_f(new_f.to_dict())
    else:
        print("Valor Incorreto, Por Favor, digite apenas (1) ou (2)")
   

def list_f():
    print('----Lista de Usuarios ----')
    print(" -- Gerentes --")
    lista = C("oop/Empresa/Gerente_db.json")
    lista.open_json()
    for funcionario in lista.to_list_f():
        print(f"""Nome: {funcionario['nome']}| Setor: {funcionario['setor']} | Cargo: {funcionario['cargo']}""")
    print(" -- Estágiarios --")
    lista = C("oop/Empresa/Estagiario_db.json")
    lista.open_json()
    for funcionario in lista.to_list_f():
        print(f"""Nome: {funcionario['nome']}| Setor: {funcionario['setor']} | Cargo: {funcionario['cargo']}""")


def del_f():
    print('----Deletando Usuario ----')
    tipo = valida_tipo(int," (1) - Gerente | (2) - Estágiario\n opção= ")
    if tipo == 1:  
        f = input('Informe o nome do Gerente para exclusão:\n nome = ').lower()
        delete_f = C("oop/Empresa/Gerente_db.json")
        delete_f.open_json()
        delete_f.remove_f(f)
    elif tipo == 2:  
        f = input('Informe o nome do Estagiarios para exclusão:\n nome = ').lower()
        delete_f = C("oop/Empresa/Estagiario_db.json")
        delete_f.open_json()
        delete_f.remove_f(f)

    
    
while True:
    print("----- Ala Funcionarios-----")
    print(""" 
          1 - Adicionar Novo Funcionario \n
          2 - Listar Funcionarios \n
          3 - Excluir Funcionario \n
          0 - Sair    
    """)
    escolha = valida_tipo(int,'escolha : ')
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


        
