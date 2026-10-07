from random import shuffle
from re import sub

n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
limpo1=str(lista)
limpo = sub(r'[^\w ]', '', limpo1)
print ('A ordem de apresentação será')
print(limpo)
