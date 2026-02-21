from funcionarios import Funcionarios 
#CRUD Funcionarios
# nome, setor, cargo, horario, salario
def valida_int(mensagem):
    valor = input(mensagem)
    Try:
      int(valor)
    

    
while True:
    print("----- Ala Funcionarios-----")
    print(""" 
          1 - Adicionar Novo Funcionario \n
          2 - Listar Funcionarios \n
          3 - Excluir Funcionario \n
          0 - Sair     
    """)
    escolha = input('escolha : ').lower
    if escolha == 1
