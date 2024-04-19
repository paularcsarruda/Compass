from functools import reduce

def calcula_saldo(lancamentos) -> float:
    def calcular_lancamento(lancamento):
        valor, tipo = lancamento
        return valor if tipo == 'C' else -valor

    saldos = map(calcular_lancamento, lancamentos)
        
    saldo_final = reduce(lambda x, y: x + y, saldos)
    return saldo_final

# Teste
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

saldo_final = calcula_saldo(lancamentos)
print(saldo_final)