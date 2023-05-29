class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

calculo = Calculo()

resultado_soma = calculo.soma(5, 3)
print("Resultado da soma:", resultado_soma)

resultado_subtracao = calculo.subtracao(10, 4)
print("Resultado da subtração:", resultado_subtracao)
