#CRUD de Produtos 
def cadastrar_produto(produtos):
    #{"id": 1, "nome": "", "preco": 0.0, "estoque": 0}
    print('--- Cadastro Produtos ---')
    if len(produtos) == 0:
        id = 1
    else:
        maior_id = max(p['id'] for p in produtos)
        id = maior_id + 1
    print(f'ID Produto : {id}')
    nome = input('Nome do Produto : ').lower()
    preco = valida_float('Preço : ')
    estoque = valida_int('Estoque : ')
    produto = {"id": id, "nome": nome, "preço": preco, "estoque": estoque}
    if buscar_produto(nome, produtos):
        print('Dado duplicado!')
        print('Altere ou Remova!')
        return
    else:
        produtos.append(produto)


def listar_produtos(produtos):
    print('--- Produtos ---')
    if len(produtos) > 0:
        for produto in produtos:
            print(f'Id : {produto['id']} | Nome : {produto['nome']} | Preço : {produto['preço']} | Estoque : {produto['estoque']}')
    else:
        print('Lista de produtos vazia')


def atualizar_produto():
    print('--- Editar Produtos ---')
    produto = input('Informe o nome do produto para atualizar: ').lower()
    p = buscar_produto(produto, produtos)
    if p:
        print('---|Produto|---')
        print(f'1 - ID : {p['id']}')
        print(f'2 - Nome : {p['nome']}')
        print(f'3 - Preço : : {p['preço']}')
        print(f'4 - Estoque : {p['estoque']}')
        dado = int(input('Informe o numero do dado a ser atualizado: '))
        if dado == 1:
            dado_att = int(input('Novo ID: '))
            p['id'] = dado_att
            print(f'ID atualizado com sucesso!')
            print(p)
            return
        elif dado == 2:
            dado_att = input('Novo Nome: ').lower()
            p['nome'] = dado_att
            print(f'Nome atualizado com sucesso!')
            print(p)
            return
        elif dado == 3:
            dado_att = valida_float('Novo Preço: ')
            p['preço'] = dado_att
            print(f'Preço atualizado com sucesso!')
            print(p)
            return
        elif dado == 4:
            dado_att = valida_int('Quantia em Estoque: ') 
            p['estoque'] = dado_att
            print(f'Estoque atualizado com sucesso!')
            print(p)
            return
        else:
            print('Opção inválida! Retornando')
            return
    else :
        print('Produto não encontrado. Retornando a página principal')      

def deletar_produto():
    print('--- Excluir Produto ---')
    produto = input('Informe o nome do produto para a exclusão: ').lower()
    p = buscar_produto(produto, produtos)
    if p:
        print(f'Deletando {p}')
        produtos.remove(p)
        return
    else:
        print('Produto não encontrado. Por favor, verifique a informação e tente novamente!')


# funçoes auxiliadoras 

def buscar_produto(produto, produtos): #Parâmetro é aquilo que MUDA de uma execução para outra. Dados mudam, funçoes não
    for p in produtos:
        if p['nome'] == produto:  
            return p
    return 


def valida_int(mensagem):
    while True:
        estoque = input(mensagem)
        try:
            estoque = int(estoque)
            return estoque
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def valida_float(mensagem):
    while True:
        preco = input(mensagem)
        try:
            preco = float(preco)
            return preco
        except ValueError:
            print("Valor inválido. Digite um número natural.")


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
        cadastrar_produto(produtos)
    elif opcao == 2:
        listar_produtos(produtos)
    elif opcao == 3:
        atualizar_produto()
    elif opcao == 4:
        deletar_produto()
    elif opcao == 0 :
        print('Saindo do Sistema, Até mais!!')
        break
    else: # ou elif opcap not in(0,1,2,3,4):
        print('Opção Inválida!')
        print('Saindo do Sistema, Até mais!!')
        break


# validação de erro em inputs com int e float
# Id baseado no maior Id da lista
# lista padronizada lower()
# sem produtos duplicados
