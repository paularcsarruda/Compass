def extrair_valor(line):
    columns = line.strip().split(',')
    gross_column = columns[-1].replace('$', '').replace(',', '').strip()

    if gross_column.replace('.', '').isdigit() or (gross_column[0] == '-' and gross_column[1:].replace('.', '').isdigit()):
        return float(gross_column)
    else:
        return None


with open('actors.csv') as file:
    data = file.read().replace('"Robert Downey, Jr."', "Robert Downey Jr.").split('\n')

    gross_values = []

    for line in data[1:]:
        value = extrair_valor(line)

        if value is not None:
            gross_values.append(value)
        else:
            print(f'Valor não numérico encontrado: {line}')

    if gross_values:
        media_valor = sum(gross_values) / len(gross_values)

        with open('etapa-2.txt', 'w') as txt:
            txt.write(f'Média de receita de bilheteria bruta dos principais filmes é de US${media_valor:.2f}')
    else:
        print('Nenhum valor numérico de receita de bilheteria encontrado.')


