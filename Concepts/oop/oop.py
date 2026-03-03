class ControleRemoto:
    def __init__(self, cor, altura, largura_controle): # 1 coisa que faz é criar essa função que vai ser o 
        self.cor = cor                        #construtor da classe, tudo o que ele tem que ter para poder 
        self.altura = altura                 # existir, Caracteristicas para ele existir
        self.largura = largura_controle #só para mostrar que é da variavel que estamos falando aqui

    def passar_canal(self, botao): # 2 coisa que faz é criar as funções, o que ele pode fazer, o comportamento dele
        if botao == ">": #parametros que a função recebe, o que ela precisa para funcionar, nesse caso o botao que foi apertado
                print("Passando para o próximo canal") 
        elif botao == "<": 
                print("Voltando para o canal anterior")
                



controle_remoto1 = ControleRemoto("preto", 10.5, 5.5) # criando a instancia do controle remoto, passando os parametros/caracteristicas para o construtor da classe
print(controle_remoto1.cor) # acessando o atributo cor do controle remoto
print(controle_remoto1.altura) # acessando o atributo altura do controle remoto
controle_remoto1.passar_canal(">") # chamando a função passar canal do controle remoto, passando o parametro botao


controle_remoto2 = ControleRemoto("branco", 12.0, 6.0) # criando outra instancia do controle remoto, passando outros parametros/caracteristicas para o construtor da classe
print(controle_remoto2.cor) # acessando o atributo cor do controle remoto
print(controle_remoto2.altura) # acessando o atributo altura do controle remoto
controle_remoto2.passar_canal("<") # chamando a função passar canal do controle remoto, passando o parametro botao