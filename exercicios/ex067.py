while True:
    numero = int(input('Quer ver a tabuada deu qual valor ?: '))
    print('-' * 20)
    if numero < 0:
        break
    for c in range (1, 11):
        print(f'{numero:<2} X {c:2d} = {numero * c:2d}')
    print('-' * 20)
print(f'programa de tabuada ENCERRADO. Volte sempre!')