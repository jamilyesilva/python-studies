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
    
def listar_produtos():
    print('--- Produtos ---')
    for produto in produtos:
        print(f'ID : {produto['ID']} | Nome : {produto['Nome']} | Preço : {produto['Preço']} | Estoque : {produto['Estoque']}')
    
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
            dado = input('Informe o nome do dado a ser atualizado: ')
            if dado == 1:
                dado = 'ID'
                dado_att = int(input('Novo ID: '))
                p[dado] = dado_att
                print(f'Nome atualizado com sucesso!')
                print(p)
            break
    else :
        print('Produto não encontrado')
            

def deletar_produto():
    print('--- Excluir Produto ---')
    produto = input('Informe o nome do produto para a exclusão: ')
    for p in produtos:
        if p['Nome'] == produto:
           print(f'Deletando {p}')
           produtos.remove(p)
            

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
        listar_produtos()
    elif opcao == 3:
        atualizar_produto(produtos)
    elif opcao == 4:
        deletar_produto()
    elif opcao == 0:
        print('Saindo do Sistema, Até mais!!')
        break
else: 
    print('Opção inválida')

