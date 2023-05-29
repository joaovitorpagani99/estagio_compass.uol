def calcular_soma(string_numeros):
    numeros = string_numeros.split(',')
    soma = sum(map(int, numeros))
    return soma

string_numeros = "1,3,4,6,10,76"
soma = calcular_soma(string_numeros)
print(soma)
