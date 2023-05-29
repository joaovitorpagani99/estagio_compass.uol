def dividir_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3
    
    lista1 = lista[:tamanho_parte]
    lista2 = lista[tamanho_parte:2*tamanho_parte]
    lista3 = lista[2*tamanho_parte:]
    
    return f"{lista1} {lista2} {lista3}"

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = dividir_lista(lista)
print(resultado)
