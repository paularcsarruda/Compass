class Passaro():
    def __init__(self, voar, emitir_som):
        self.voar = voar
        self.emitir_som = emitir_som
        
    
class Pato(Passaro):
    def __init__(self):
        super().__init__('Voando...', 'Pato emitindo som...\nQuack, Quack')
    
    
class Pardal(Passaro):
    def __init__(self):
        super().__init__('Voando...', 'Pardal emitindo som...\nPiu, Piu')
    
    
pato = Pato()
pardal = Pardal()

print("Pato")
print(pato.voar)
print(pato.emitir_som)

print("\nPardal")
print(pardal.voar)
print(pardal.emitir_som)
