#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
import numpy as np
import pandas as pd

arquivo = pd.read_csv('Sprint 7/exercicios/secao 3 - Exercicios/tarefa 1/actors.csv', sep=',', quotechar='"')

frequencia_de_filmes = arquivo['#1 Movie'].value_counts()
frequencia_maxima= frequencia_de_filmes.max()
filmes_mais_frequentes = frequencia_de_filmes[frequencia_de_filmes == frequencia_maxima]
print("Nome do(s) filme(s) mais frequente(s) e sua respectiva frequencia:")
for nome_filme, frequencia in filmes_mais_frequentes.items():
    print(f"{nome_filme}: {frequencia}")
