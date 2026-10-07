valor_casa = float(input('Valor da casa: R$ '))
salario = float (input('Salario do comprador: R$ '))
anos = int (input('Quantos anos de financiamento ?: '))

minimo = salario / 100 * 30
prestacao = valor_casa / (anos * 12)
msg = 0
if prestacao > minimo:
    msg = '\033[1;31mNEGADO\033[m'
else:
    msg = '\033[1;32mAPROVADO\033[m'
print (f'Para uma casa de R$ {valor_casa:.2f} '
       f'financiada em {anos} anos ficam com parcelas de R$ {prestacao:.2f} '
       f'\nSeu financiamento esta {msg}')
