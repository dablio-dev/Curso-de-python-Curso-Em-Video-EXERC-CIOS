from datetime import date
print ('''Qual é o seu sexo ?
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = input ('Sua opção: ')
if '1' != sexo and '2' != sexo:
    print('Opção de sexo \033[1;31mINVALIDA\033[m!')
elif sexo == '2':
    print('Você não precisa passar pelo alistamento obrigatorio!')
else:
    nasc = int(input('Ano de nascimento do candidato: '))

    ano = date.today()
    anofmt = str (ano)
    ano_atual = int (anofmt[:4])
    idade = ano_atual - nasc

    if sexo == '1':
        if idade == 18:
            print ('Você deve se alistar IMEDIATAMENTE')
        elif  idade < 18:
            print(f'Ainda falta {18 - idade} ano(s) para o seu alistamento, seu alistamento será em {18 - idade + ano_atual}')
        else:
            print(f'Você passou {idade - 18} ano(s) do tempo de alistamento, você deveria ter se alistado em {ano_atual - (idade - 18)}')

