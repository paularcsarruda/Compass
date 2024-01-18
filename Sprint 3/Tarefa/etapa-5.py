def extrair_valor(line):
    columns = line.strip().split(',')
    col_total_gross = columns[-5].replace('$', '').replace(',', '').strip()

    if col_total_gross.replace('.', '').isdigit() or (col_total_gross[0] == '-' and col_total_gross[1:].replace('.', '').isdigit()):
        return float(col_total_gross)
    else:
        return None


lista = []

with open('actors.csv') as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."', "Robert Downey Jr.").split('\n')

    for linha in dados[1:]:
        ator = linha.split(",")[0].strip()
        valor = extrair_valor(linha)
        
        if valor is not None:
            lista.append({'ator': ator, 'valor': valor})

    lista = sorted(lista, key=lambda dicionario: dicionario["valor"], reverse=True)

    with open('etapa-5.txt', 'w') as txt:
        for dicionario in lista:
            txt.write(f'{dicionario["ator"]} - US$ {dicionario["valor"]:.2f}\n')


            