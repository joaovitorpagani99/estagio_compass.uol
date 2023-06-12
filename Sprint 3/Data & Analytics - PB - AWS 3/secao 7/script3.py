# Abrir o arquivo ators.csv e ler as linhas
with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

ator_faturamento = {}
ator_filme = {}

for linha in linhas:
    
    data = linha.strip().split(',')

    ator = data[0]
    total = float(data[1])
    num_filmes = int(data[2])

    ator_faturamento[ator] = ator_faturamento.get(ator, 0) + total
    ator_filme[ator] = ator_filme.get(ator, 0) + num_filmes

ator_media_bruto = {}

for ator in ator_faturamento:
    media_bruto = ator_faturamento[ator] / ator_filme[ator]
    ator_media_bruto[ator] = media_bruto

media_alta = max(ator_media_bruto, key=ator_media_bruto.get)
resul = ator_media_bruto[media_alta]

print(f"Ator/atriz: {media_alta}")
print(f"Media de faturamento por filme: ${resul:.2f}")


with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/etapa-3.txt', 'w') as arquivo:
    arquivo.write(f"Ator/atriz: {media_alta} | Media de faturamento por filme: ${resul:.2f}")
    
