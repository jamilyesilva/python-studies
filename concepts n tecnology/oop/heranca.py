class Jogador:
    def __init__(self, altura, velocidade, passe, drible, precisao):
        #todos os jogadores terao esse tipo de caracteristicas com valores diferentes
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.drible = drible
        self.precisao = precisao

    def chutar(self):
        print('Chutar')

    def passar_bola(self):
        print('passou bola ')
        
    def driblar(self):
        print('driblar')
        
    #todos os jogadores vao conseguir fazer essas tres funcoes que eu coloquei acima
    # mas temos goleiros e linhas, que fazem funçoes diferentes.
    # então vamos criar um objeto proprio para o goleiro/linha

class Jogador_Goleiro(Jogador): #tem Jogador como parametro pois ele ainda faz tudo que um jogadore faz, ele tem essas habilidades 
    def agarrar(self):
        
        self.altura * 2
        print('pular')
        print('estender maos e pegar')

class Jogador_Linha():
    def fazer_gol(self):
        print('chutar para gol')

jogador1 = Jogador(1.70, '2km/hr', 'lateral', 'pouco', 'boa')
print(jogador1.altura)
jogador1.passar_bola()

jogador2 = Jogador_Goleiro(1.88, '4km/hr', 'pivo', 'media', 'boa') 
print(jogador2.altura) # jogador 2 tem os mesmos atributos e metodos que a classe Jogador
jogador2.driblar()
jogador2.agarrar()
