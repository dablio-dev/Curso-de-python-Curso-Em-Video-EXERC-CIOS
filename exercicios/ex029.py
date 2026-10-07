velocidade = float (input('Digite a velocidade do seu carro '))
if velocidade >80:
    print ('Voce excedeu o limite de velocidade e foi multado ')
    multa = (velocidade - 80) * 7
    print (f'Voce foi multado em R${multa:.2f}')
else:
    print (f'Tenha um bom dia e dirija com segurança')


