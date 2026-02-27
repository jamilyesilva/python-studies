# criar um objeto cliente para netflix
class Cliente:
    def __init__(self, nome, idade, email, plano):
        self.nome = nome #caracteristica nome do cliente é igual a variavel cliente que vai ser definida no parametro da instancia
        self.idade = idade
        self.email = email
        self.lista_planos = ['premium', 'basico', 'padrao'] # atibuto fixo para todos os clientes, só podem escolher essa opções
        if plano in self.lista_planos: #verificando se o plano escolhido pelo cliente é valido, se ele estiver na lista de planos
            self.plano = plano # se for valido, o plano do cliente é igual ao plano escolhido

    def trocar_plano(self, novo_plano): #
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print(f"Plano trocado para {novo_plano}")
        else:
            print("Plano inválido. Escolha entre: premium, basico, padrao.")

    def ver_filme(self, nome_filme, plano_filme):
        if self.plano == plano_filme:
            print(f"{self.nome} está assistindo {nome_filme}.")
        elif self.plano == "premium": #ela pode assistir todos os filmes
            print(f"{self.nome} está assistindo {nome_filme}.")
        elif self.plano == "padrao" and plano_filme == "premium": #ela pode assistir filmes basicos e padrao, mas não premium
            print(f"{self.nome} não tem acesso a {nome_filme}. Plano requerido: {plano_filme}.")
        else:
            print(f"{self.nome} o filme {nome_filme} não existe.")

cliente1 = Cliente("João", 30, "joao@email.com", "premium")
print(cliente1.nome) # acessando o atributo nome do cliente
print(cliente1.plano) # acessando o atributo plano do cliente

cliente1.ver_filme("Matrix", "premium")
#aqui teria um botão para trocar o plano
cliente1.trocar_plano("padrão") # trocando o plano do cliente1 para "padrao"
                                # se colocar valor errado, da erro
cliente1.ver_filme("Matrix", "premium") # tentando assistir o filme novamente com o plano basico, da erro porque o plano basico não tem acesso ao filme premium
print(cliente1.plano) # acessando o atributo plano do cliente para verificar a troca


cliente2 = Cliente("Maria", 25, "maria@email.com", "basico") #se colocar um valor diferente da variavel fixa nos atributos, da erro
print(cliente2.nome) # acessando o atributo nome do cliente
print(cliente2.plano) # acessando o atributo plano do cliente
