class Calculo():
    def soma(self, x, y):
        return x + y
        
    def subtracao(self, x, y):
        return x - y
    
calc = Calculo()

resultado_soma = calc.soma(4, 5)
print(resultado_soma)

resultado_subtracao = calc.subtracao(4, 5)
print(resultado_subtracao)