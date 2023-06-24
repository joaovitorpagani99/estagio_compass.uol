from functools import reduce

def calcula_saldo(lancamentos) -> float:
    #continue este código
    # Função lambda para realizar a soma dos valores
    soma_valores = lambda x, y: x + y

    # Mapeia os valores dos lançamentos com os sinais correspondentes
    valores = list(map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos))

    # Utiliza a função reduce para calcular o saldo final
    saldo_final = reduce(soma_valores, valores)

    return saldo_final
