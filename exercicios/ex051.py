print('='*40)
print('10 TERMOS DE UMA PA'.center(40,' '))
print('='*40)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 10 * razao + termo

for c in range(termo, cont, razao):
    print(c, end=' → ')
print ('ACABOU')