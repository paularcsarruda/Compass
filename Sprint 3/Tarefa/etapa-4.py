from collections import Counter

def correct_actor_name(line):
    columns = line.strip().split(',')

    # Corrigir o erro no nome do ator "Robert Downey, Jr."
    if len(columns) > 6:
        column_diff = line.split('"')
       
        if len(column_diff) > 2:
            new_line = column_diff[0] + column_diff[1].replace(",", "") + column_diff[2]
            return new_line.strip().split(',')
        
    return columns


count_films = Counter()

with open('actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    header = lines[0].strip().split(',')
    movie_index = header.index('#1 Movie')

    for line in lines[1:]:
        columns = line.strip().split(',')

        if len(columns) > movie_index:
            max_bilheteria = columns[movie_index].strip()

            if max_bilheteria:
                count_films[max_bilheteria] += 1

result = sorted(count_films.items(), key=lambda x: (-x[1], x[0]))

with open('etapa-4.txt', 'w', encoding='utf-8') as output_file:
    for sequencia, (nome_filme, quantidade) in enumerate(result, start=1):
        output_file.write(f'{sequencia} - O filme "{nome_filme}" aparece {quantidade} vez(es) no dataset.\n')
