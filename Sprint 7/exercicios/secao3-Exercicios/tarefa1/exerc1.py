#Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
import pandas as pd
import numpy as np

arquivo = pd.read_csv('Sprint 7/exercicios/secao 3 - Exercicios/tarefa 1/actors.csv', sep=',', quotechar='"')

index = np.argmax(arquivo['Number of Movies'])

ator = arquivo.loc[index, 'Actor']
nm_filmes = arquivo.loc[index, 'Number of Movies']

print(f'O ator/atrizes com o maior numero de filmes e {ator} com {nm_filmes} filmes.')
