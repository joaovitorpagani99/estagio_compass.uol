import json

novo_arquivo = "person.json"

with open(novo_arquivo, 'r') as arquivo:
    conteudo = json.load(arquivo)

print(conteudo)