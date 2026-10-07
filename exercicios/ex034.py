salario = float(input('Digite o valor do salario atual R$'))
if salario > 1250:
    result = salario / 100 * 10 + salario
    print (f'O salario anterior era R${salario:.2f} e passou a ser R${result:.2f} após acrescimo de 10%')
else:
    result = salario / 100 * 15 + salario
    print (f'O salario anterior era R${salario:.2f} e passou a ser {result:.2f} após acrescimo de 15%')
