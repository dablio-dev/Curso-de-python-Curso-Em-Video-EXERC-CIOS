distancia = float (input ('Digite a distancia percorrida em km: '))
print (f'Você esta prestes a começar uma viajem de {distancia}Km ')
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print (f'O preço da sua passagem é R${valor:.2f}')
