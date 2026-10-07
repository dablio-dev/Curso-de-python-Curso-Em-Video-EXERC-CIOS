from random import choice
nome1=input('Digite um nomer: ')
nome2=input('Digite um nome: ')
nome3=input('Digite um nome: ')
nome4=input('Digite um nome: ')
lista=[nome1, nome2, nome3 , nome4]
sorte=choice(lista)
print (f'O aluno sorteado foi {sorte}')
