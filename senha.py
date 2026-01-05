#senha correta
sc = str(12345)
sd = input('Digite a senha:')

while sd != sc:
    sd = input('Digite a senha novamente:')
if sd == sc:
    print('Acesso permitido')


