#CRUD de Produtos 
def cadastrar_produto():
    #{"id": 1, "nome": "", "preco": 0.0, "estoque": 0}
    print('--- Cadastro Produtos ---')
    id = len(produtos) + 1 
    print(f'ID Produto : {id}')
    nome = input('Nome do Produto : ').capitalize()
    preco = float(input('Preço : R$'))
    estoque = int(input('Estoque : '))
    produto = {"ID": id, "Nome": nome, "Preço": preco, "Estoque": estoque}
    produtos.append(produto)


def listar_produtos(produto):
    print('--- Produtos ---')
    if len(produto) >= 1:
        for produto in produtos:
            print(f'ID : {produto['ID']} | Nome : {produto['Nome']} | Preço : {produto['Preço']} | Estoque : {produto['Estoque']}')
    else:
        print('Lista de produtos vazia')


def atualizar_produto(produtos):
    print('--- Editar Produtos ---')
    produto = input('Informe o nome do produto para atualizar: ').capitalize()
    for p in produtos:
        if p['Nome'] == produto:
            print('---|Produto|---')
            print(f'1 - ID : {p['ID']}')
            print(f'2 - Nome : {p['Nome']}')
            print(f'3 - Preço : : {p['Preço']}')
            print(f'4 - Estoque : {p['Estoque']}')
            dado = int(input('Informe o numero do dado a ser atualizado: '))
            while True:
                if dado == 1:
                    dado_att = int(input('Novo ID: '))
                    p['ID'] = dado_att
                    print(f'ID atualizado com sucesso!')
                    print(p)
                    return
                elif dado == 2:
                    dado_att = input('Novo Nome: ').capitalize()
                    p['Nome'] = dado_att
                    print(f'Nome atualizado com sucesso!')
                    print(p)
                    return
                elif dado == 3:
                    dado_att = float(input('Novo Preço: '))
                    p['Preço'] = dado_att
                    print(f'Preço atualizado com sucesso!')
                    print(p)
                    return
                elif dado == 4:
                    dado_att = int(input('Quantia em Estoque: '))
                    p['Estoque'] = dado_att
                    print(f'Estoque atualizado com sucesso!')
                    print(p)
                    return
                else:
                    print('Opção inválida! Retornando')
                    break
    else :
        print('Produto não encontrado. Retornando a página principal')      

def deletar_produto(produtos):
    print('--- Excluir Produto ---')
    produto = input('Informe o nome do produto para a exclusão: ').capitalize()
    for p in produtos:
        if p['Nome'] == produto:
           print(f'Deletando {p}')
           produtos.remove(p)
           return
    else:
        print('Produto não encontrado. Por favor, verifique a informação e tente novamente!')
            

produtos = []
while True:
    print('--- Sistema Mercadinho ---')
    print('1 - Cadastrar Produtos')
    print('2 - Produtos')
    print('3 - Atualizar Produto')
    print('4 - Deletar produto')
    print('0 - Sair')

    opcao = int(input('Opção: '))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos(produtos)
    elif opcao == 3:
        atualizar_produto(produtos)
    elif opcao == 4:
        deletar_produto(produtos)
    elif opcao == 0 :
        print('Saindo do Sistema, Até mais!!')
        break
    elif opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 0:
        print('Opção Inválida!')
        print('Saindo do Sistema, Até mais!!')
        break

