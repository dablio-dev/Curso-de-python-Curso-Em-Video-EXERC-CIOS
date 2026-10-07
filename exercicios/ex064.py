verde = '\033[;32m'
azul = '\033[;34m'
amarelo = '\033[;33m'
reset = '\033[m'

somatorio = 0
contador = 0

print(f'{amarelo}')
print ('-=' * 25)
print('Digite quantos números quiser'.center(50, ' '))
print('O programa acaba ao digitar (999)'.center(50, ' '))
print ('-=' * 25)
print(f'{reset}')
valor = int(input('Digite um numero inteiro: '))
while valor != 999:
    somatorio += valor
    contador += 1
    valor = int(input('Digite um numero inteiro: '))
print(f'''{azul}Total de numeros digitados: {contador}{reset}
{verde}Soma de todos os valores digitados: {somatorio}{reset}''')

#sempre esqueço que posso usar condicionais dentro dos laços e as vezes fora deles, lembrando eu sei usar as condicionais mas as vezes esqueço da existencia delas, lembrar disso ao passar exercicios
'''tambem usei o while dessa forma a seguir...
while valor != 999:
    valor = int(input('Digite um numero inteiro: '))
    if valor != 999:
        contador += 1
        somatorio += valor
agora não sei qual logica seria mais valida, e qual exercita mais o assunto, mas me senti frustrado por achar que não consegui desenvolver o melhor caminho sozinho
(se é que o melhor caminho é esse que esta ativo em execução) tive que como eu ja disse a minha solução foi essa que esta nesse comenterio
a que esta ativa foi a solução do professor guanabara.'''
