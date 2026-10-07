palavra = str (input('Digite uma palavra: ')).strip().upper().split()
palavra2 = str (''.join(palavra))
len1 = int (len(palavra2))
inverso = ''
print('Frase ao contrario: ')
for c in range (len1 -1 , -1, -1):
    print(f'{palavra2[c]}', end='')
    inverso += palavra2[c]
if palavra2 == inverso:
    msg = 'é um palíndromo'
else:
    msg = 'não é um palíndromo'
print(f'\n\nA frase digitada {msg}!')
