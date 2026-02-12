#CLASSES ALEATORIAS
#----- CLASSE PESSOA ---
class Pessoas:
    def __init__(self, user, nome, senha, plano):
        self.user = user
        self.nome = nome
        self.senha = senha
        self.lista_planos = ["basico", "estudantil", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
            print(f"Plano {plano}")
        else:
            print("Plano inexistente")

    def trocar_plano(self, novo_plano):
        if novo_plano in self.lista_planos: #novo_plano nao tem self porque ta fora da função __init__
            self.plano = novo_plano
            print(f"Plano atualizado para {self.plano}")
        else:
            print("Plano inexistente")

class Admin(Pessoas): #HERANÇA, a classe Admin herda os atributos e métodos da classe Pessoas, ou seja, ela é uma subclasse de Pessoas
    def __init__(self, user, nome, senha, plano):
       super().__init__(user, nome, senha, plano)
       self._equipe = [] #atributo privado, só pode ser acessado dentro da classe Admin
       #ENCAPSULAMENTO, o atributo _equipe é privado, não pode ser acessado diretamente fora da classe, só através dos métodos da classe Admin

#métodos para acessar e modificar a equipe do admin
    def equipe(self):
       return self._equipe

    def adicionar_membro_equipe(self, membro):
        if not membro in self._equipe:
            self._equipe.append(membro)
            print(f"{membro} adicionado a equipe")
        else:
            print(f"{membro} já é da equipe")

    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
            print(f"{membro} removido da equipe")
        else:
            print(f"{membro} não é da equipe")


pessoa1 = Pessoas("chromantico", "jamily", "1234", "premium")
print(pessoa1.user)
print(pessoa1.plano)
pessoa1.trocar_plano("estudantil")
print(pessoa1.plano)
print("--"*4)


pessoa2 = Pessoas("anoxido", "emanuel", "1234", "basico")
print(pessoa2.user)
print(pessoa2.plano)
pessoa2.trocar_plano("premium")
print(pessoa2.plano)
print("--"*4)

pessoa3 = Admin("kvortz", "Ana Cecilia", "1234", "premium") 
print(pessoa3.equipe()) # acessando a equipe do admin, que é uma lista vazia
pessoa3.adicionar_membro_equipe("Joao") # adicionando um membro a equipe do admin, o método adicionar_membro_equipe verifica se o membro já está na equipe, se não estiver, ele adiciona o membro e imprime uma mensagem de confirmação
pessoa3.adicionar_membro_equipe("Maria")
print(pessoa3.equipe())
pessoa3.remover_membro_equipe("Joao")
print(pessoa3.equipe())