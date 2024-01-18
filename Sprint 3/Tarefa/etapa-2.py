def extract_gross_value(line):
    columns = line.strip().split(',')
    gross_column = columns[-1].replace('$', '').replace(',', '').strip()

    if gross_column.replace('.', '').isdigit() or (gross_column[0] == '-' and gross_column[1:].replace('.', '').isdigit()):
        return float(gross_column)
    else:
        return None


with open('actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()[1:] 

gross_values = []

for line in lines:
    gross_value = extract_gross_value(line)
    
    if gross_value is not None:
        gross_values.append(gross_value)
    else:
        print(f'Valor não numérico encontrado: {gross_value}')

if gross_values:
    average_gross = sum(gross_values) / len(gross_values)

    with open('etapa-2.txt', 'w') as file:
        file.write(f'Média de receita de bilheteria bruta dos principais filmes é de US${average_gross:.2f}')

