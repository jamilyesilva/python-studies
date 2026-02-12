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