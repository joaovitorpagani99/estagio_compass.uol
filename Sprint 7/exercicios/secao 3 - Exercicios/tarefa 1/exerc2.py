#Apresente a média da coluna contendo o número de filmes.
import numpy as np
import pandas as pd

arquivo = pd.read_csv('Sprint 7/exercicios/secao 3 - Exercicios/tarefa 1/actors.csv', sep=',', quotechar='"')

media = np.mean(arquivo['Number of Movies'])

print(f"A media da coluna que contem o numero de filmes e: {media}")