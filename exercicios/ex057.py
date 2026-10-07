from time import sleep
sexo = 'vazio'
while sexo not in 'FfMm':
    sexo = str(input('Digite seu sexo[M/F]: ')).strip().lower()[0]
    if sexo != 'f' and sexo != 'm':
        print('Digite opção valida...')
        sleep(2)

if sexo == 'm':
    print('Olá menino seu sexo é masculino!')
else:
    print('Olá menina seu sexo é feminino!')
