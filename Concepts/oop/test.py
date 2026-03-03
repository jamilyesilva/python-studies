class ControleRemoto: # o que tem que ter de informação no cliente
    #atributos são as caracteristicas fixas, tudo o que ele tem que ter assim que existir no __init__
        # exe: cor, altura, tamanho
        def __init__(self, cor, altura, largura): # sempre voce tem que me passar esses valores na instancia
            self.cor = cor
            self.altura = altura
            self.largura = largura
            # o self referencia a caracteristica, o valor é o parametro/ valor que vc vai colocar na instancia
            #self só existe dentro da criação da classe e em todas as funçoes

        # o que o meu controle consegue fazer
        # metodos são açoes que o controle terá, são funçoes
        # exe: passar canal, desligar tv, etc
        def passar_canal(self, botao):
            if botao == '>':
                print('aumentar canal')
            else:
                 print('Diminuir canal')
            

# depois o objetivo é como vou interagir essas classes
controle1 = ControleRemoto('vermelho', 12, 3) # passar os valores que a classe chamada pede
#substituir o self pelo nome da instancias criada
controle1.passar_canal('>')
controle2 = ControleRemoto('azul', 12, 3)