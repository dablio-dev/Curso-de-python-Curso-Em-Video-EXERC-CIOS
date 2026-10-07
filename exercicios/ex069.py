maior_18 = 0
mulher_menor_20 = 0
total_homens = 0
while True:
    print('=' * 30)
    print('CADASTRE UMA PESSOA'.center(30, ' '))
    print('=' * 30)
    while True:
        idade = str(input('Idade: ')).strip()
        if idade.isnumeric() == True:
            idade = int(idade)
            if idade > 18:
                maior_18 += 1
                break
            if idade > 0:
                break
    while True:
        sexo = str(input('Sexo: [M/F]: ')).strip().lower()
        if sexo in 'FfMm':
            if sexo in 'Ff' and idade < 20:
                mulher_menor_20 += 1
            if sexo in 'Mm':
                total_homens += 1
            break
    while True:
        continua = str(input('Quer continuar?: [S/N]')).strip().lower()
        if continua in 'sSnN':
            break
    if continua in 'Nn':
        break
print('-' * 30)
print('FIM DO PROGRAMA'.center(30, ' '))
print('-' * 30)
print(f'''Total de pessoas 18+: {maior_18}
Total de homens cadastrados: {total_homens}
Mulheres com menos de 20 anos: {mulher_menor_20} ''')
