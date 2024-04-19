import random

list = [random.randint(0,10000) for i in range(250)]

print ('Lista: ', list)

list.reverse()

print('Lista Invertida: ', list)