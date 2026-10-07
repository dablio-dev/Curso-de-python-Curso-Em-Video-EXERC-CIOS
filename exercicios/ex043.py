altura = float (input('Sua altura (metros): '))
peso = float (input('Seu peso (quilos): '))
imc = peso / (altura * altura)
print(f'Seu imc é {imc:.1f}')
msg = 0
if imc < 18.5:
    msg = 'abaixo do peso'
elif imc <= 25:
    msg = 'no peso ideal'
elif imc <= 30:
    msg = 'com sobrepeso'
elif imc < 40:
    msg = 'com obesidade'
elif imc >= 40:
    msg = 'com obesidade mórbida'
print (f'com este imc você esta {msg}')
