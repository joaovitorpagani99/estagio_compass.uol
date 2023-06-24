import csv

# Lê o arquivo CSV e armazena os dados em uma lista
estudantes = []
with open('estudantes.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        estudantes.append(linha)

# Função para calcular a média das três maiores notas
def calcular_media(notas):
    maiores_notas = sorted(notas, reverse=True)[:3]
    media = sum(maiores_notas) / len(maiores_notas)
    return round(media, 2)

# Ordena os estudantes pelo nome
estudantes = sorted(estudantes)

# Gera o relatório
for estudante in estudantes:
    nome = estudante[0]
    notas = list(map(int, estudante[1:]))
    maiores_notas = sorted(notas, reverse=True)[:3]
    media = calcular_media(notas)

    print(f"Nome: {nome} Notas: {maiores_notas} Média: {media}")
