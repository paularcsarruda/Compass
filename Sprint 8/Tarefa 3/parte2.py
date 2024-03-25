animais = ['cachorro', 'gato', 'onitorrinco', 'cavalo', 'lobo', 'sapo', 'lagarto', 'coelho', 'coala', 'urso', 
           'lontra', 'foca', 'beija-flor', 'coruja', 'peixe', 'tigre', 'leão', 'elefante', 'zebra', 'girafa',]

animais_ordenados = sorted(animais)

[print(animal) for animal in animais_ordenados]

with open('lista_animais.csv', 'w') as file:
    for animal in animais_ordenados:
        file.write(f"{animal}\n")