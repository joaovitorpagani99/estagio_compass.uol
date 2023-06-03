# A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.
with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

dados_autor = []

for linha in linhas:
    dados = linha.strip().split(',')

    ator = dados[0]
    bruto_total = float(dados[1])

    dados_autor.append((ator, bruto_total))

ordenar = sorted(dados_autor, key=lambda x: x[1], reverse=True)

with open('Sprint3/Data & Analytics - PB - AWS 3/secao 7/etapa-5.txt', 'w') as arquivo:
    print("Lista de atores ordenada pelo faturamento bruto total (em ordem decrescente):")
    arquivo.write("Lista de atores ordenada pelo faturamento bruto total (em ordem decrescente):")
    arquivo.write("\n")
    for ator, bruto_total in ordenar:
        print(f"Ator: {ator}")
        print(f"Faturamento bruto total: {bruto_total}")
        arquivo.write(f"Ator: {ator}")
        arquivo.write(f"Faturamento bruto total: {bruto_total}")
        arquivo.write("\n")
        
    
