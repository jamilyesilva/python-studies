from decimal import *
#Nível 1: Encapsulamento (Protegendo os Dados)
# testando encapsulamento
class Funcionarios:
    def __init__(self, nome, setor, cargo, salario):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.salario = salario
    
    @property # transforma metodo em atributo/propriedade, acessa como variavel mas está tem uma função por tras
    def salario(self):
        return self._salario #  getter controla a leitura, sem o setter o salario só pode ser lido, não modificado, ou seja, é um atributo somente leitura

    @salario.setter # permite controlar o que acontece quando alguem tenta modificar o atributo
    def salario(self, valor): # controla a escrita, nao funciona sem o getter, é para criar modificaçoes ou coisas a fazer para que o dado nao seja errado ou fique inseguro
        if valor < 0: 
            raise ValueError("Salário inválido") #break so funciona em loop while
        self._salario = valor

    def apresentar(self):
        print(f"Sou {self.nome}, do setor de {self.setor} atuando como {self.cargo} e salario R${self.salario}")

    def __getstate__(self):
        return f'{
            "nome": self.nome, 
            "setor": self.setor, 
            "cargo": self.cargo, 
            "salario": self.salario, 
            }'
        

#Nível 2: Herança e Polimorfismo (Categorias de Dados)
#   usando de herança e polimorfismo para criar mais objetos e modificar a apresentação
class Gerentes(Funcionarios):
    def __init__(self, nome, setor, cargo, salario, bonus): # tem que informar os atributos pai que você utilizará
        super().__init__(nome, setor, cargo, salario) #super() chama o construtor da classe pai (Funcionarios) para inicializar os atributos herdados
        self.bonus= bonus #atributo específico da classe Gerentes

    @property
    def bonus(self): # ler dado e retornar como variavel
        return self._bonus
    
    @bonus.setter
    def bonus(self, valor):
        if valor > 100 or valor < 1:
            raise ValueError('O valor não se refere a uma porcentagem')
        self._bonus = valor

    def aplicar_bonus(self):
        salario = float(self.salario) 
        bonus = float(self.bonus) * salario/100
        salario_total = salario + bonus
        self.salario = salario_total

    def apresentar(self):
        print(f'Sou {self.nome} sendo {self.cargo} da empresa com um salario de {self.salario} e atualmente com bonus de {self.bonus}%')

class Estagiarios(Funcionarios):
    def __init__(self, nome, setor, cargo, salario, limite_horas):
        super().__init__(nome, setor, cargo, salario) # peguei esses da classe pai
        self.limite_horas = limite_horas # sem _ no inicio para passar pelo getter e setter

    @property
    def limite_horas(self):
        return self._limite_horas
    
    @limite_horas.setter
    def limite_horas(self, valor):
        if valor > 6:
            raise ValueError("Horas Excedidas, apenas 6 horas")
        self._limite_horas = valor #informando que é var interna
        
    def apresentar(self):
        print(f"Sou {self.nome}, um {self.cargo}  com {self.salario} de salario por {self.limite_horas} horas de trabalho")

#O Grande Desafio: Nível 3 (Abstração / Repositório)
# class Gerenciador(Funcionarios):
#     def __init__(self, funcionarios):
#         self.funcionarios =[] # bd temporario

#     def adicionar(funcionario):

    #listar_todos()
    #remover(nome)
    #salvar_em_json()



p1 = Funcionarios ("jamily", "ti", "desenvolvedora", 10)
print(p1.salario)

p2 = Estagiarios("jamily", "ti", "desenvolvedora- Estagiaria", 1200, 5)
p2.apresentar()

p3 = Gerentes("juan", "rh", "gerente", 2000, 5)
p3.aplicar_bonus()
p3.apresentar()




