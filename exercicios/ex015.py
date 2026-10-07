n1=int(input('Quantos dias vocês utilizou o carro: '))
n2=float(input('Quantos km você rodou com o carro: '))
result=n1*60 + (n2*0.15)
print ('Você deve pagar R${:.2f}'.format(result))
