![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JSON](https://img.shields.io/badge/json-5E5E5E?style=for-the-badge&logo=json&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Object--Oriented-brightgreen?style=for-the-badge)
# 👥 Sistema de Gerenciamento de Funcionários (CRUD)
* Este é um projeto para estudos de Python  
<img width="324" height="198" alt="image" src="https://github.com/user-attachments/assets/ddc14ed8-5d92-4063-9532-40b273c947e0" />
  
> Sistema CLI (comand line system) para gerenciar funcionários, utilizando os conceitos avançados de OOP em Python com persistência de dados em JSON.

## Funcionalidades:
* __Cadastro de Funcionários__: _Diferenciação entre Gerentes e Estagiários._
* __Persistência de Dados__: _Salva as informações em arquivos .json separados por categoria._
* __Validação de Dados__: _Sistema robusto de validação de tipos __(int, float)__ e regras de negócio __( encapsulamento de salário positivo, limite de horas )__._
* __Listagem e Exclusão__: _Interface simples para visualizar e remover registros do "banco de dados" verificando a compatibilidade do nome indicado para exclusão com integrados a lista de funcionários._

## Conceitos Aplicados
_Este projeto foi construído para praticar_:
* Encapsulamento:
Uso de @property e setters para proteger atributos como salário e bônus.

* Herança e Polimorfismo:
Classes Gerentes e Estagiarios herdando da base Funcionarios.
```
class Gerentes(Funcionarios):
    def __init__(self, *args, bonus: Decimal, **kwargs):
        super().__init__(*args, **kwargs)
```
* Abstração (Camada de Repositório):
A classe Config centraliza toda a lógica de manipulação de arquivos.
* Tratamento de Exceções:
Uso de try/except e raise ValueError para garantir que o programa não quebre com entradas inválidas.
*Type Hinting (DIQXY):
```
def __init__(self, *args, bonus: Decimal, **kwargs):
```
Tipagem de dados para melhor legibilidade e suporte da IDE.
```
def __init__(self, nome: str, setor: str, cargo: str, salario: Decimal):
```
## Teconologias Utilizadas
* Python 3
* Modulo json _(nativo)_
* Modulo os  _(nativo)_
* Modulo Decimal  _(nativo)_
* OOP

## 📂 Estrutura dos arquivos
>main.py  
>funcionarios.py
>>json  
>>>Gerente_db.json  
>>>Estagiaro_db.py

**by: Jamily Em. Silva**  
_Utilize para fins educacionais_

