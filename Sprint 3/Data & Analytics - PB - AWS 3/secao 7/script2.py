# Apresente a  media de faturamento bruto por ator.
with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

ator_bruto = {}
ator_filmes = {}


for line in linhas:
    
    data = line.strip().split(',')

    ator = data[0]
    total_bruto = float(data[1])
    num_filmes = int(data[2])
 
    ator_bruto[ator] = ator_bruto.get(ator, 0) + total_bruto
    ator_filmes[ator] = ator_filmes.get(ator, 0) + num_filmes


ator_media_bruto = {}
with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/etapa-2.txt', 'w') as arquivo:
    for ator in ator_bruto:
        media_bruto = ator_bruto[ator] / ator_filmes[ator]
        ator_media_bruto[ator] = media_bruto

    for ator in ator_media_bruto:
        print(f"{ator:25} | ${ator_media_bruto[ator]:.2f} ")
        arquivo.write(f"{ator:25} | ${ator_media_bruto[ator]:.2f}")
