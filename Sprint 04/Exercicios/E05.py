import csv

def notas_estudantes(nome, notas):
    notas = list(sorted(map(int, notas), reverse=True)[:3]) 
    media = round(sum(notas) / 3, 2)
    print(f"Nome: {nome} Notas: {notas} Média: {media}")


estudantes = []

with open('estudantes.csv', 'r') as file:
    reader = csv.reader(file)
    for linha in reader:
        nome = linha[0]
        notas = linha[1:]  
        estudantes.append((nome, notas))

estudantes = sorted(estudantes, key=lambda x: x[0])

for estudante in estudantes:
    notas_estudantes(estudante[0], estudante[1])