def conta_vogais(texto:str) -> int:
    vogais = "aeiouAEIOU"
    contador = len(list(filter(lambda char: char in vogais, texto)))
    return contador

# Teste 
print(conta_vogais("CompassUOL"))