continua = 's'
contador = 0
somatorio = 0
valor = 0
maior = 0
menor = 0
while continua != 'n' and continua == 's':
    valor = int(input('Digite um valor: '))
    somatorio += valor
    if contador == 0:
        maior = valor
        menor = valor
    contador += 1
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    continua = str(input('Você quer continuar [S/N]: ')).lower().strip()[0]
media = somatorio / contador
print('-=' * 25)
print(f'''Números digitados: {contador}
Media entre todos os números: {media}
Maior entre eles: {maior}
Menor entre eles: {menor}''')
print('-=' * 25)

'''ainda não assistir a solução do professor, mas logo no começo do video ele diz que
esse foi o exercicio mais dificil, mas não tive dificuldades para resolver
pra min o mais dificil da aula 14 foi o da sequencia de fibonacci'''