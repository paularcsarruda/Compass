with open('actors.csv', 'r') as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')
    
    with open('etapa-3.txt', 'w') as txt:
        max_fat = float(0)
        lista = []
        atores = []
        media = 0

        for valores in dados[1:]:
            campo1 = valores.strip().split(',')[3]
            campo2 = valores.strip().split(',')[0]
            lista.append(float(campo1))
            atores.append(campo2)

        for valor in lista:
            if valor >= max_fat:
                max_fat = valor
                actor=atores[media]
            media += 1
        
        txt.write( f'O(a) ator/atriz com a maior média de receita de bilheteria é {actor} com US${max_fat:.2f}.')
