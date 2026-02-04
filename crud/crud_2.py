#CRUD de Produtos 
def cadastrar_produto():
    #{"id": 1, "nome": "", "preco": 0.0, "estoque": 0}
    print('--- Cadastro Produtos ---')
    id = len(produtos) + 1 
    print(f'ID Produto : {id}')
    nome = input('Nome do Produto : ')
    preco = float(input('Preço : R$'))
    estoque = int(input('Estoque : '))
    produto = {"ID": id, "Nome": nome, "Preço": preco, "Estoque": estoque}
    produtos.append(produto)
    print(produtos)
    
def listar_produtos():
    pass
def atualizar_produto():
    pass
def deletar_produto():
    pass

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
        atualizar_produto()
    elif opcao == 4:
        deletar_produto()
    elif opcao == 0:
        print('Saindo do Sistema, Até mais!!')
        break
else: 
    print('Opção inválida')

