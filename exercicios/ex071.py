print('=' * 40)
print(' BANCO DABLIO '.center(40, ' '))
print('=' * 40)

dinheiro = int(input('Valor a ser sacado: '))
total = dinheiro
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} de R${cedula}')
        totcedula = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break

#este foi a solução que eu consegui, não consegui desenvolver uma forma de resolver usando laço, tive que copiar do professor, entendi como funciona mas ainda não estou afiado o suficiente para conseguir desenvolver esse tipo de solução
# notas50 = dinheiro // 50
# notas20 = (dinheiro - notas50 * 50) // 20
# notas10 = (dinheiro - notas50 * 50 - notas20 * 20) // 10
# notas1 = dinheiro - notas50 * 50 - notas20 * 20 - notas10 * 10
#
# if notas50 > 0:
#     print(f'''Total de {notas50} cédulas de R$50''')
# if notas20 > 0:
#     print(f'''Total de {notas20} cédulas de R$20''')
# if notas10 > 0:
#     print(f'''Total de {notas10} cédulas de R$10''')
# if notas1 > 0:
#     print(f'''Total de {notas1} cédulas de R$1''')



print('=' * 40)
print('Volte sempre ao BANCO DABLIO! Tenha um bom dia!')
