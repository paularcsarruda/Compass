class Aviao():
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = 'azul'


avioes = []

avioes.append(Aviao('BOIENG456', '1500 km/h', '400'))
avioes.append(Aviao('Embraer Praetor 600', '863 km/h', '14'))
avioes.append(Aviao('Antonov An-2', '258 km/h', '12'))

for aviao in avioes:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidadeáxima de {aviao.velocidade_maxima}, capacidade para {aviao   .capacidade} e é da cor {aviao.cor}')
