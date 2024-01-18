def correct_actor_name(line):
    columns = line.strip().split(',')

    # Corrigir o erro no nome do ator "Robert Downey, Jr."
    if len(columns) > 6:
        column_diff = line.split('"')
        if len(column_diff) > 2:
            new_line = column_diff[0] + column_diff[1].replace(",", "") + column_diff[2]
            return new_line.strip().split(',')
    return columns


ator_com_maior_media = None
maior_media_receita = 0

with open('actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    header = lines[0].strip().split(',')
    media_receita_index = header.index('Average per Movie')

    for line in lines[1:]:
        values = line.strip().split(',')
        media_receita_str = values[media_receita_index].strip('$').replace(',', '')

        if media_receita_str:
            media_receita = float(media_receita_str)

            if media_receita > maior_media_receita:
                maior_media_receita = media_receita
                ator_com_maior_media = values[0]

with open('etapa-3.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f'O ator/atriz com a maior média de receita de bilheteria é {ator_com_maior_media} com uma média de US${maior_media_receita:.2f}.')
