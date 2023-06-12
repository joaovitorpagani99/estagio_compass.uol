class Aviao:
    cor = "azul"

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
    
avioes = []

aviao1 = Aviao("BOIENG456", "1500 km/h", "400 passageiros")
avioes.append(aviao1)

aviao2 = Aviao("Embraer Praetor 600", "863 km/h", "14 passageiros")
avioes.append(aviao2)

aviao3 = Aviao("Antonov An-2", "258 km/h", "12 passageiros")
avioes.append(aviao3)

for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {Aviao.cor}.")
