primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

dados = zip(primeirosNomes, sobreNomes, idades)

for indice, (primeiroNome, sobreNome, idade) in enumerate(dados):
    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")