import datetime

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade'))

dataAtual = datetime.datetime.now().year
ano100 = dataAtual + (100 - idade)

print(ano100)

