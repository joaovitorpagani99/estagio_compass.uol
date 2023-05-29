def my_map(lista, f):
    nova_lista = []
    for elemento in lista:
        resultado = f(elemento)
        nova_lista.append(resultado)
    return nova_lista

def potencia_de_2(numero):
    return numero ** 2

lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_resultado = my_map(lista_entrada, potencia_de_2)

print(lista_resultado)