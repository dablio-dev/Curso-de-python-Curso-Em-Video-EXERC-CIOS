# n1=float(input('Digite o valor do produto para aplicar 5% de desconto: R$'))
# n2=n1/100*5
# print ('O produto que custa R${:.2f} passará a custar R${:.2f} após desconto de 5%'.format(n1, n1-n2))

n1=float(input('Digite o preço: R$'))
n2=float(input('Digite quantos % de desconto deve ser dado: '))
porc=n1/100*n2
print ('Se o preço atual é R${:.2f} ele passará a ser {:.2f} após {:.2f}% de desconto, nesta operação foi descontado RS{:.2f}'.format(n1, n1 - porc, n2, porc))
