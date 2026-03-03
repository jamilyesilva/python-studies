frutas = ["banana", "maça", "goiaba", "uva", "amora"]

fruta = input("informe a fruta").lower()
if fruta in frutas:
    print(f'Fruta {fruta} encontrada!')
else: 
    print(f'Fruta {fruta} não encontrada!')