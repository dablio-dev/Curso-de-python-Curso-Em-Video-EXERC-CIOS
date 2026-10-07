velho = 0
nome_velho = ''
mulher_menor = 0
totidade = 0
totpessoas = 0
for pess in range(1,5):
    print(f' {pess}ª pessoa '.center(30,'-'))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().lower()
    totidade += idade
    totpessoas += 1
    if sexo == 'm' and idade > velho:
        velho = idade
        nome_velho = nome
    else:
        if sexo == 'f' and idade < 20:
            mulher_menor += 1

media_idade = totidade / totpessoas
print(' Resultados '.center(35, '-'))
print(f'Media de idade do grupo: {media_idade:.1f}'
      f'\nNome do homem mais velho: {nome_velho}'
      f'\nIdade do homem mais velho: {velho}'
      f'\nQuantidade de mulheres abaixo do 20 anos: {mulher_menor}')
print('-' * 35)
