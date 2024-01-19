# primeira forma (correspondea resposta informada na Udemy)

from datetime import datetime

nome = 'Paula'
idade_atual = 37
ano_atual = datetime.now().year
centenario = ano_atual + (100 - idade_atual)

print(f"{centenario}")

# segunda forma

from datetime import datetime

nome = input('Informe o seu nome: ')
idade_atual = int(input('Informe a sua idade: '))
ano_atual = datetime.now().year
centenario = ano_atual + (100 - idade_atual)

print(f"{centenario}")
