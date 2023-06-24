# Abre o arquivo e lê os números
with open("number.txt", "r") as file:
    numbers = list(map(int, file.readlines()))

# Filtra apenas os números pares
ver_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Ordena em ordem decrescente
or_numbers = sorted(ver_numbers, reverse=True)

# Seleciona os 5 maiores números
top_5_numbers = or_numbers[:5]

# Calcula a soma dos 5 maiores números
sum_top_5_numbers = sum(top_5_numbers)

# Imprime os resultados
print(top_5_numbers)
print(sum_top_5_numbers)
