nomes = []

#adicionando nomes com append()
nomes.append("jami")
nomes.append("lua")
nomes.append("juan")
nomes.append("karol")
nomes.append("james")

print(nomes)
print(f'Primeiro nome = {nomes[0]}')# chamando de acoro com um index, por isso o []
print(f'Ultimo nome = {nomes[-1]}')

#adicionando toda uma coleção
novos_nomes = ["matthew", "rhaviv"]
nomes.extend(novos_nomes) #adicionando outra lista dentro da lista.
print(nomes)