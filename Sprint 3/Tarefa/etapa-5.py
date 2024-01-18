def correct_actor_name(line):
    columns = line.strip().split(',')

    # Corrigir o erro no nome do ator "Robert Downey, Jr."
    if len(columns) > 6:
        column_diff = line.split('"')
        
        if len(column_diff) > 2:
            new_line = column_diff[0] + column_diff[1].replace(",", "") + column_diff[2]
            return new_line.strip().split(',')
        
    return columns


def extract_total_gross_value(line):
    columns = line.strip().split(',')
    total_gross_column = columns[-5].replace('$', '').replace(',', '').strip()

    if total_gross_column.replace('.', '').isdigit() or (total_gross_column[0] == '-' and total_gross_column[1:].replace('.', '').isdigit()):
        return float(total_gross_column)
    else:
        return None


actor_gross_list = []

with open('actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    header = lines[0].strip().split(',')
    actor_index = header.index('Actor')
    gross_index = header.index('Total Gross')

    for line in lines[1:]:
        columns = correct_actor_name(line)

        total_gross_value = extract_total_gross_value(line)

        if total_gross_value is not None and len(columns) > max(actor_index, gross_index):
            actor_name = columns[actor_index].strip()
            total_gross_str = columns[gross_index].replace('$', '').replace(',', '').strip()

            actor_gross_list.append((actor_name, total_gross_value))

sorted_actor_gross_list = sorted(actor_gross_list, key=lambda x: x[1], reverse=True)

with open('etapa-5.txt', 'w', encoding='utf-8') as output_file:
    for actor, total_gross in sorted_actor_gross_list:
        output_file.write(f'{actor} - US${total_gross:.2f}\n')
        print(f'{actor} - US${total_gross:.2f}')
