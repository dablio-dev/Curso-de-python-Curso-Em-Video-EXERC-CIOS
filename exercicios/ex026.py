frase=str(input('Digite uma frase: ')).strip().lower()
print (f'A letra "A" apare {frase.count('a')} vezes'
       f'\nEla aparece primeiro na posição {frase.find('a')+1}'
       f'\nEla aparece por ultimo na posição {frase.rfind('a')+1}')