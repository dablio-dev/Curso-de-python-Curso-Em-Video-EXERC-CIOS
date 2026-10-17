palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for posicao in palavras:
    print(f'\nNa palavra {posicao.upper()} temos as vogais', end=' ')
    for letra in posicao:
        if letra in 'aeiou':
            print(f'|{letra}|'.upper(), end='')

