from datetime import datetime

nome = 'Paula'
idade_atual = 37
ano_atual = datetime.now().year
centenario = ano_atual + (100 - idade_atual)

print(f"{centenario}")
