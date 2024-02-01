# Python Higher Order Functions

Uma função é chamada de Higher Order Function em dois momentos:

- quando contêm uma outra função ou
- quando retorna uma função em seu output

exemplo:

```python
def shout(text):  
    return text.upper()  
    
print(shout('Hello'))  
    
# Assigning function to a variable 
yell = shout  
    
print(yell('Hello'))
```

### Passando Funções como argumento de outras Funções

Funções são como objetos em Python, mas elas também podem ser passadas como argumento de outras funções.

```python
def shout(text):  
    return text.upper()  
    
def whisper(text):  
    return text.lower()  
    
def greet(func):  
    # storing the function in a variable  
    greeting = func("Hi, I am created by a function \ 
    passed as an argument.")  
    print(greeting)   
    
greet(shout)  
greet(whisper)
```

### Retornando Funções

Nós também podemos passar as funções como função de uma outra função,  complicado?

```python
def create_adder(x):  
    def adder(y):  
        return x + y  
    
    return adder  
    
add_15 = create_adder(15)  
    
print(add_15(10))
```

# **Funções mais comuns**

Existem várias funções higher-order functions em Python como: as `map`, `filter`, and `reduce`:

- `map`: `map` vai aplicar uma função em cada item de uma lista de itens, ou seja, é um for com uma chamada da função para aplicá-la a cada item da sua lista. Ela é basicamente uma estrutura de repetição que vai aplicar uma função para cada item dentro da sua lista. Então ele vai facilitar a utilização dessas funções para que você consiga ser mais eficiente na hora de escrever o seu código.

```
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
```

- `filter`: é uma funcionalidade poderosa que permite filtrar dados específicos em uma lista ou em um dataframe usando a linguagem de programação Python. Esses valores estão submetidos a uma condição que pode alterar ou não alguns desses valores, então, os que retornam positivo → True, serão os resultados mostrados no filter.

```
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # [2, 4]
```

- `reduce`: é utilizada para combinar elementos de um objeto iterável em um único valor. Ele é útil para realizar operações como soma, multiplicação, concatenação e encontrar o máximo ou mínimo valor em uma lista.

```python
reduce(function, sequence[, initial])
```

```
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers) # 15
```

- `zip`:  Ela permite agrupar elementos de diversas listas em tuplas, criando uma nova lista combinada. Essa função pode ser aplicada em diferentes situações, desde a manipulação de dados até a criação de algoritmos complexos.

```python
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

lista_combinada = zip(lista1, lista2)

for item in lista_combinada:
    print(item)

# Output:
# (1, 'a')
# (2, 'b')
# (3, 'c')
```

A função zip em Python oferece flexibilidade e várias possibilidades para manipulação de listas. Aqui estão algumas dicas e truques para otimizar o uso dessa função:

- **É possível passar mais de duas listas como argumento para a função zip.**

```
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

lista_combinada = zip(lista1, lista2, lista3)

for item in lista_combinada:
    print(item)

# Output:
# (1, 'a', True)
# (2, 'b', False)
# (3, 'c', True)
```

- **Se as listas tiverem tamanhos diferentes, a função zip irá parar quando o tamanho da menor lista for atingido.**

```
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c']

lista_combinada = zip(lista1, lista2)

for item in lista_combinada:
    print(item)

# Output:
# (1, 'a')
# (2, 'b')
# (3, 'c')
```

- `lambda`: são chamadas de funções anônimas. São funções que o usuário não precisa definir.

```python
lambda {argumentos}: {expressão}
```

```python
soma = lambda x, y: x + y
print(soma(2, 3))

ou

print((lambda x, y: x + y)(2, 3))
```
