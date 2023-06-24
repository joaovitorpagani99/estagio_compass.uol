def calcular_valor_maximo(operadores, operandos) -> float:
    resultados = list(map(lambda x: eval(str(x[0][0]) + x[1] + str(x[0][1])), zip(operandos, operadores)))
    # A função recebe os parâmetros operadores e operandos e retorna um valor float
    # A lista "resultados" será usada para armazenar os resultados das operações aplicadas aos pares de operandos
    
    return max(resultados)
    # A função retorna o maior valor presente na lista de resultados

