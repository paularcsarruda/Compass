from collections import Counter

count_films = Counter()

with open("actors.csv") as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."', "Robert Downey Jr.").split('\n')
    with open('etapa-4.txt', 'w') as txt:

        freq = Counter()

        for a in dados[1:]:
            campo1 = a.strip().split(',')[4]

            if campo1:
                freq[campo1] += 1

        if freq:
            result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
            txt.write("Lista de todos os filmes e suas frequências no dataset:\n\n")
            for sequencia, (nome_filme, quantidade) in enumerate(result, start=1):
                txt.write(f'{sequencia} - O filme "{nome_filme}" aparece {quantidade} vez(es) no dataset.\n')
        else:
            txt.write('Nenhum filme encontrado no dataset.\n')
