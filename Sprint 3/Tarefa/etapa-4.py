with open('actors.csv', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

cabecalho = linhas[0].strip().split(',')
num_filmes = {}

for linha in linhas[1:]:
    filme = linha.strip().split(',')[-2]

    num_filmes[filme] = num_filmes.get(filme, 0) + 1

num_filmes_sorted = sorted(num_filmes.items(), key=lambda x: (-x[1], x[0]))

with open('etapa-4.txt', 'w', encoding='utf-8') as txt:
    txt.write("Lista de filmes e a quatidade de vezes que aparecem no dataset:\n\n")
    sequencia = 1

    for filme, num_filmes in num_filmes_sorted:
        txt.write(f'{sequencia} - O filme {filme} aparece {num_filmes} vez(es) no dataset.\n')
        sequencia += 1
