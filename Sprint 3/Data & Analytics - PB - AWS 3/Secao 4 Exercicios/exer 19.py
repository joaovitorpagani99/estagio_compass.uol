import random

random_list = random.sample(range(500), 50)


mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0


random_list.sort();

valor_minimo = random_list[0]

valor_maximo = random_list[-1]

meio = len(random_list) // 2
if len(random_list) % 2 == 0:
    mediana = (random_list[meio - 1] + random_list[meio]) / 2
else:
    mediana = random_list[meio]
    
media = sum(random_list) / len(random_list)

#Media: 232.64, Mediana: 221.0, Mínimo: 3, Máximo: 491

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")