# Abrir o arquivo actors.csv e ler as linhas
with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

cont_filmes = {}

for linha in linhas:
    data = linha.strip().split(',')

    filme = data[4]

    cont_filmes[filme] = cont_filmes.get(filme, 0) + 1

filmes_frequentes = []
max_frequencia = max(cont_filmes.values())

for filme, frequencia in cont_filmes.items():
    if frequencia == max_frequencia:
        filmes_frequentes.append((filme, frequencia))

print("Filme(s) mais frequente(s):")

for filme, frequencia in filmes_frequentes:
    print(f"Filme: {filme}")
    print(f"Frequencia: {frequencia} vezes")


with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/etapa-4.txt', 'w') as arquivo:
    arquivo.write(f"Filme: {filme} | Frequencia: {frequencia} vezes")
