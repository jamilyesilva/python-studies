from decimal import *
import os
import json
#Nível 1: Encapsulamento (Protegendo os Dados)
# testando encapsulamento

class Funcionarios:
    def __init__(self, nome: str, setor: str, cargo: str, salario: Decimal): # sempre typar as variaveis para evitar conflito DIQXY
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.salario = salario
    
    @property
    def salario(self):
        return self._salario 
    def salario(self, valor: Decimal): # sempre typar as variaveis para evitar conflito DIQXY
        if valor < 0: 
            raise ValueError("Salário inválido")
        self._salario = valor

    def apresentar(self):
        print(f"Sou {self.nome}, do setor de {self.setor} atuando como {self.cargo} e salario R${self.salario}")

    def to_dict(self) -> dict: # sempre tipar retornos DIQXY
        # for em 1 linha para remover _ do dict DIQXY
        return {
            key.lstrip('_'): value for key, value in self.__dict__.items()
        }
        

#Nível 2: Herança e Polimorfismo (Categorias de Dados)
#   usando de herança e polimorfismo para criar mais objetos e modificar a apresentação
class Gerentes(Funcionarios):
    # o *args e **kwargs pegam TUDO que sobrou e mandam para o pai DIQXY
    def __init__(self, *args, bonus: Decimal, **kwargs):
        super().__init__(*args, **kwargs) 
        self.bonus = bonus 

    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, valor: int): # sempre typar as variaveis para evitar conflito DIQXY
        if valor > 100 or valor < 1:
            raise ValueError('O valor não se refere a uma porcentagem')
        self._bonus = valor

    def aplicar_bonus(self):
        # quanto tipamos nossos atributos n precisamos converter nossa variaveis DIQXY
        salario = self.salario
        bonus = self.bonus * salario / 100
        salario_total = salario + bonus
        self.salario = salario_total

class DataBase(funcionarios):
    # def open_json(self):
    #     # to_dict
    #     if not os.path.exists("db_funcionarios.json"):
    #         with open("db_funcionarios.json", "w", encoding="utf-8") as arqv:
    #             json.dump([], arqv, ensure_ascii=False, indent=4)
    #     if os.path.exists("crud/tarefa.json"):
    #         with open("crud/tarefa.json", "r", encoding="utf-8") as arqv:
    #             pessoas = json.load(arqv) #json para objeto
    #             return pessoas
    
    # def add_dict_to_json(self):
    #     tarefas.append(nova_tarefa)
    #     with open("crud/tarefa.json", "w", encoding="utf-8") as arqv:
    #         json.dump(tarefas, arqv, ensure_ascii=False, indent=4) #dump = objeto para json
    #     print('Tarefa criada com sucesso!')
    # else:
    #     print('O título não pode ser vazio! Por favor, tente novamente.')
    #     return

    def apresentar(self):
        print(f'Sou {self.nome} sendo {self.cargo} da empresa com um salario de {self.salario} e atualmente com bonus de {self.bonus}%')

class Estagiarios(Funcionarios):
    def __init__(self, *args, limite_horas: int, **kwargs):
        super().__init__(*args, **kwargs) 
        self.limite_horas = limite_horas 

    @property
    def limite_horas(self):
        return self._limite_horas
    
    @limite_horas.setter
    def limite_horas(self, valor: int):
        if valor >= 6:
            raise ValueError("Horas Excedidas, apenas 6 horas")
        self._limite_horas = valor
        
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
print(p1.to_dict())

print("______"*2)
# como usamos kwargs entao temos que na assintura da classe definirmos o campo LIMITE_HORAS para não confundir o dict DIQXY
p2 = Estagiarios("jamily", "ti", "desenvolvedora- Estagiaria", 1200, limite_horas=5)
p2.apresentar()

print("______"*2)
# como usamos kwargs entao temos que na assintura da classe definirmos o campo BONUs para não confundir o dict DIQXY
p3 = Gerentes("juan", "rh", "gerente", 2000, bonus=5)
p3.aplicar_bonus()
p3.apresentar()




