class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiquetar()

#pessoa
class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        subtipos = ['adulto', 'adolescente']
        if idade >= 18:
            self.idade = subtipos[0]
            print('maior de idade')
        else:
            self.idade = subtipos[1]
            print("Menor de idade")
            
    
def sis_escola():
    lista_disciplinas = {"matematica": ["algebra", "calculo"], "fisica": ["vetores", "constantes"], "portugues": ["poema", "crases"]}
    disciplina = input("informe a disciplina: ").lower()
    if disciplina in lista_disciplinas:
        print(f"disciplinas disponiveis: {lista_disciplinas[disciplina]}")
        conteudo = input("informe o conteudo: ").lower()
        if conteudo in lista_disciplinas[disciplina]:
            print(f"conteudo {conteudo} encontrado")
        else:
            print(f"conteudo {conteudo} nao encontrado")
    else:
        print("disciplina inexistente")


class Usuarios():
    usuarios = {
        "admin":["ler", "escrever", "excluir", "adicionar"],
        "user": ["ler"]
                }
    tipo_usuario = input("informe o tipo de usuario: ").lower()
    if tipo_usuario in usuarios:
        print(f"permissoes disponiveis: {usuarios[tipo_usuario]}")
        permissao = input("informe a permissao: ").lower()
        if permissao in usuarios[tipo_usuario]:
            print(f"permissao {permissao} concedida")
        else:
            print(f"permissao {permissao} negada ou inexistente")
    else:
        print("usuario inexistente")
