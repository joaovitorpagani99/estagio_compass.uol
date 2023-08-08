#[Warm up]  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. 
# Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

import random 

lista = []

for i in range(260):
    lista.append(random.randint(0, 10000))
    
lista.reverse()

print(lista)