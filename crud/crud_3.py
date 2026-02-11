#leitura de arquivo JSON - 1 exercicio
#id
#titulo
#concluida
import json
import os

def abrir_arquivo():
    if not os.path.exists("crud/tarefa.json"):
        with open("crud/tarefa.json", "w", encoding="utf-8") as arqv:
            json.dump([], arqv, ensure_ascii=False, indent=4)
    if os.path.exists("crud/tarefa.json"):
        with open("crud/tarefa.json", "r", encoding="utf-8") as arqv:
            pessoas = json.load(arqv)
            return pessoas
        
def valida_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")



def status(mensagem):
    while True:
        valor = input(mensagem).lower()
        if valor.strip() != "": #strip() tira os espaços em branco no início e no final da string, ou seja, verifica se a string não está vazia
            if valor == "s" or valor == "n":
                if valor == 's':
                    return True
                else:
                    return False
            else:
                print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
        else:
            print("Espaço em branco. Por favor, digite algo")
            
        

# funçoes create and read
def nova_tarefa(): 
    tarefas = abrir_arquivo()
    nova_tarefa = {}
    print('--- Nova Tarefa ---')
    if len(tarefas) == 0:
        nova_tarefa["id"] = 1
        print(f'ID| {nova_tarefa["id"]}')
    else:
        nova_tarefa["id"] = tarefas[-1]["id"] + 1
        print(f'ID| {nova_tarefa["id"]}')
    nova_tarefa["titulo"] = input('Título: ')
    if nova_tarefa["titulo"].strip() != "":
        nova_tarefa["concluida"] = status('Tarefa concluída? (s/n): ')
        tarefas.append(nova_tarefa)
        with open("crud/tarefa.json", "w", encoding="utf-8") as arqv:
            json.dump(tarefas, arqv, ensure_ascii=False, indent=4) #dump = objeto para json
        print('Tarefa criada com sucesso!')
    else:
        print('O título não pode ser vazio! Por favor, tente novamente.')
        return
    

def concluir_tarefa(tarefas):
    print('--- Editar Tarefa ---')
    opcao = valida_int('Infome o id da tarefa para concluir: ')
    for tarefa in tarefas:   
        if opcao == tarefa["id"]:
            tarefa["concluida"] = True
            with open("crud/tarefa.json", "w", encoding="utf-8") as arqv:
                json.dump(tarefas, arqv, ensure_ascii=False, indent=4)
            print('Tarefa editada com sucesso!')
        else:
            break
    else:
        print('ID não encontrado! Por favor, tente novamente.')



def visualizar_tarefas():
    tarefas = abrir_arquivo()
    print('--- Visualizar Tarefas ---')
    for tarefa in tarefas:
        print(f'ID: {tarefa["id"]}| Título: {tarefa["titulo"]}| Concluída: {tarefa["concluida"]}')
        print('---------------'*3)
    while True:
        print('1 - Editar Tarefa')
        print('0 - Sair')
        opcao = valida_int('Opção: ')
        if opcao == 1 or opcao == 0:
            if opcao == 1:
                concluir_tarefa(tarefas)
            elif opcao == 0:
                print('--Saindo do Sistema, Até mais!!--')
                break



def menu():
    # pessoas = []
    while True:
        print('--- Sistema Tarefas ---')
        print('1 - Nova Tarefa')
        print('2 - Visualizar Tarefas')
        print('0 - Sair')

        opcao = valida_int('Opção: ')
        if opcao == 1 or opcao == 2 or opcao == 0:
            if opcao == 1:
                nova_tarefa()
            elif opcao == 2:
                visualizar_tarefas()
            elif opcao == 0 :
                print('--Saindo do Sistema, Até mais!!--')
                break
        else:
            print('Valor inválido! Por favor, escolha uma valor válido.')

menu()