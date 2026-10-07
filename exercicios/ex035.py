seg1 = float(input('Digite um segmento: '))
seg2 = float(input('Digite um segmento: '))
seg3 = float(input('Digite um segmento: '))
if (seg1 + seg2) > seg3 and (seg2 + seg3) > seg1 and (seg1 + seg3) > seg2:
    print ('Pode formar um triângulo')
else:
    print ('Não pode formar um triângulo')
