with open('actors.csv', 'r') as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')
    
    with open('etapa-3.txt', 'w') as txt:
        media = float(0)
        num = []
        actors = []
        max_fat = 0

        for valores in dados[1:]:
            campo1 = valores.strip().split(',')[3]
            campo2 = valores.strip().split(',')[0]
            num.append(float(campo1))
            actors.append(campo2)

        for valor in num:
            if valor >= media:
                media = valor
                actor=actors[max_fat]
            max_fat += 1
        
        txt.write( f'O(a) ator/atriz com a maior média de receita de bilheteria é {actor} com US${media:.2f}.')

