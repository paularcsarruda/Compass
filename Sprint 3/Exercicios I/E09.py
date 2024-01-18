primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[i]
    idade = idades [i]
    print(i, f'- {nome} {sobrenome} está com {idade} anos')