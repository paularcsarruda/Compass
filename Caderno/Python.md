# Python

### Aplicações da Linguagem

Por causa de sua simplicidade e praticidade, Python popularizou-se entre os desenvolvedores das mais diversas áreas. 
Python é uma linguagem de programação imperativa, interpretada, de alto nível e com tipagem forte e dinâmica. 

### Funções

A sintaxe de uma função é definida por três partes: nome, parâmetros e corpo, o qual agrupa uma sequência de linhas que representa algum comportamento.

```
 def hello(meu_nome):
    print('Olá',meu_nome!')
```
Para executar a função, de forma semelhante ao que ocorre em outras linguagens, devemos simplesmente chamar seu nome e passar os parâmetros esperados entre parênteses, 
conforme o código a seguir.

```
hello('Paula')
Olá, Paula!
```

## POO

A Programação Orientada a Objetos (POO) é ​​um paradigma de programação baseado no conceito de Classes e Objetos.

- Classes podem conter dados e código:

Dados na forma de campos (também chamamos de atributos ou propriedades); e Código, na forma de procedimentos (frequentemente conhecido como métodos). Uma importante característica dos objetos é que seus próprios métodos podem acessar e frequentemente modificar seus campos de dados: objetos mantém uma referência para si mesmo, o atributo self no Python.

### Classes, Objetos, Métodos e Atributos

As **Classes** são tipos de dados definidos pelo desenvolvedor que atuam como um modelo para objetos. Pra não esquecer mais: Classes são fôrmas de bolo e bolos são objetos.

**Objetos** são instâncias de uma **Classe**. **Objetos** podem modelar entidades do mundo real (Carro, Pessoa, Usuário) ou entidades abstratas (Temperatura, Umidade, Medição, Configuração).

**Métodos** são funções definidas dentro de uma **classe** que descreve os comportamentos de um objeto. Em Python, o primeiro parâmetro dos métodos é sempre uma referência ao próprio objeto.

Os **Atributos** são definidos na **Classe** e representam o estado de um **objeto**. Os objetos terão dados armazenados nos campos de atributos. 

### Polimorfismo

Quando utilizamos Herança, teremos Classes filhas utilizando código comum da Classe acima, ou Classe pai. Ou seja, as Classes vão compartilhar atributos e comportamentos (herdados da Classe).

Assim, Objetos de Classes diferentes, terão métodos e atributos compartilhados que podem ter implementações diferentes, ou seja, um método pode possuir várias formas e atributos podem adquirir valores diferentes.

Daí o nome: **Poli (muitas) morfismo (formas)**.

Por exemplo uma entidade Carro que herda de Automóvel.

```
class Automovel:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O automóvel está ligado.")

    def desligar(self):
        print("O automóvel está desligado.")

class Carro(Automovel):
    def __init__(self, marca, modelo, cor):
        # Chamando o construtor da classe pai (Automovel)
        super().__init__(marca, modelo)
        self.cor = cor

    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")

# Exemplo de uso
meu_carro = Carro(marca="Toyota", modelo="Corolla", cor="Prata")
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Cor: {meu_carro.cor}")

meu_carro.ligar()
meu_carro.acelerar()
meu_carro.frear()
meu_carro.desligar()
```

### ETL
