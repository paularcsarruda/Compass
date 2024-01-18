def correct_actor_name(line):
    columns = line.strip().split(',')

    # Corrigir o erro no nome do ator "Robert Downey, Jr."
    if len(columns) > 6:
        column_diff = line.split('"')
        
        if len(column_diff) > 2:
            new_line = column_diff[0] + column_diff[1].replace(",", "") + column_diff[2]
            return new_line.strip().split(',')
        
    return columns


actor_max_films = None
max_films = 0

with open('actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()[1:] 

    for line in lines:
        columns = correct_actor_name(line)

        columns = [column.strip() for column in columns]
        
        number_films = int(columns[-4])

        if number_films > max_films:
            max_films = number_films
            actor_max_films = columns[0]

with open('etapa-1.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f'O ator/atriz com mais filmes é {actor_max_films} com {max_films} filmes.')

