# n1=float(input('Digite o valor em sua carteira para converter em dolar: R$'))
# n2= n1 / 3.27
# print ('Com R${:.2f} você pode comprar US${:.2f}!'.format(n1, n2))
#
# n1=float(input('Digite o valor em sua carteira: R$'))
# n2=float(input('Digite a cotação atual do dolar: US$'))
# result=n1 / n2
# print ('Com o valor disponivel na sua carteira R${:.2f} e a cotação atual do dolar US${:.2f} você pode comprar US${:.2f}'.format(n1, n2, result))


print ('Digite o valor em sua carteira em reais e depois a cotação atual de cada moeda citada para fazer a conversão ')
real=float(input('Digite o valor da sua carteira em reais: R$'))
d=float(input('digite a contação atua do dolar: US$'))
e=float(input('Digite a cotação atual do euro: €'))
l=float(input('Digite a cotação atual da libra esterlina: €'))
dolar= real / d
euro= real / e
libra= real / l
print ('Com a cotação atual você compra')
print ('US${:.2f} \n  €{:.2f} \n  £{:.2f}'.format(dolar, euro, libra))
