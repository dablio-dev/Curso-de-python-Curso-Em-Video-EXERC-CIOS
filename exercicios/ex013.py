# n1=float(input('Digite o salario atual para acrescentar 15%: R$'))
# porc= n1 + n1 / 100 * 15
# print ('Se o salarios atual é R${} ele será R${} após 15% de acrescimo!'.format(n1, porc))

n1=float(input('Digite o valor do salario atual: R$'))
n2=float(input('Digite o valor da porcentagem a ser acrescentada ao salario: '))
porc=n1/100*n2
print ('Se o salario atual é R${:.2f} após acrescimo de {:.2f}% o novo salario será R${:.2f} e foi acrescentado R${:.2f}'.format(n1, n2, n1+porc, porc))
