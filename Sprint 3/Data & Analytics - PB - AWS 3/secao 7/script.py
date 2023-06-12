# Abrir o arquivo actors.csv para leitura
with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

max_filme = 0
ator_max_filme = ""

for linha in linhas[1:]:
    columns = linha.split(',')

    ator = columns[0].replace('"', '')
    num_filmes = float(columns[2])

    if num_filmes > max_filme:
        max_filme = num_filmes
        ator_max_filme = ator

print(f"O ator/atrizes com o maior numero de filmes e {ator_max_filme}, com um total de {max_filme} filmes.")

with open('Sprint3\Data & Analytics - PB - AWS 3\secao 7\etapa-1.txt', 'w') as file:
    file.write(f"O ator/atrizes com o maior numero de filmes e {ator_max_filme}, com um total de {max_filme} filmes.")
