def remover_duplicados(lista):
    nova_lista = list(set(lista))
    return nova_lista

lista_exemplo = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista_sem_duplicados = remover_duplicados(lista_sem_duplicados)
print(lista_sem_duplicados)