with open('actors.csv', 'r') as file:
    dados = file.read().replace('"Robert Downey, Jr."', "Robert Downey Jr.").split('\n')

    with open('etapa-1.txt', 'w') as txt:
        qnt = 0
        atores = ""

        for i in dados[1:]:
            columns = i.strip().split(',')
            campo1 = columns[2]
            campo2 = columns[0]
            num_filmes = int(columns[-4])

            if num_filmes > qnt:
                qnt = num_filmes
                atores = campo2
        
        txt.write(f'O(a) ator/atriz com maior número de filmes é {atores} com {qnt} filmes')
