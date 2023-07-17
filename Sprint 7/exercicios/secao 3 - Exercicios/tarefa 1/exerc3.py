#Apresente o nome do ator/atriz com a maior média por filme.
import numpy as np
import pandas as pd

arquivo = pd.read_csv('Sprint 7/exercicios/secao 3 - Exercicios/tarefa 1/actors.csv', sep=',', quotechar='"')

index_Maior = np.argmax(arquivo['Average per Movie'])
ator = arquivo.loc[index_Maior, 'Actor']
media = arquivo.loc[index_Maior, 'Average per Movie']

print(f'ator com a maior media foi {ator} com a media: {media}')