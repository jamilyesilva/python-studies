#CRUD simples para gerenciamento de alunos sem o salvamento de dados em arquivos
def cadastrar():
    print("--- Cadastro de aluno ---")
    nome = input("Nome do aluno: ").capitalize()
    nota = float(input("Nota do aluno: "))
    aluno = {"nome": nome, "nota": nota}
    alunos.append(aluno)

def listar():
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")
        print("-----")

def atualizar_nota():
    aluno = input("Nome do aluno a ser atualizado: ").capitalize()
    for a in alunos:
        if a["nome"] == aluno:
            nova_nota = float(input("Nova nota: "))
            a["nota"] = nova_nota
            print("Aluno atualizado com sucesso!")
            
def deletar():
    aluno = input("Nome do aluno a ser deletado: ").capitalize()
    for a in alunos:
        if a["nome"] == aluno:
            alunos.remove(a)
            print("Aluno deletado com sucesso!")


alunos = [] # lista para armazenar os alunos cadastrados - utilização de dicionarios para cada aluno-
print("Bem-vindo ao sistema de gerenciamento de alunos!")
print("Escolha uma opção:")
while True: # loop infinito para menu, sendo quebrado apenas quando o usuario escolhe sair
    print("-----"*2)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar nota do aluno")
    print("4 - Deletar aluno")
    print("5 - Sair")
    print("-----"*2)
    opcao = input("Opção: ")
    if opcao == "1": #Utilizando das funcoes para cada operacao
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar_nota()
    elif opcao == "4":
        deletar()
    elif opcao == "5":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
