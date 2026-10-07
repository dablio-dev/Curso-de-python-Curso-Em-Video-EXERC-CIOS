termos = int(input('Quantidade de termos: '))
cont = 3
total = 0
total2 = 1
print(f'{total} → {total2} → ', end= '')
while cont <= termos:
    total3 = total + total2
    print(f'{total3} → ', end= '')
    total = total2
    total2 = total3
    cont += 1
#tive dificuldade em desenvolver a logica deste exercicio
#depois que o prefessor fez uma analogia onde enle mostrava visualmente que o total1 vira o total2 e o total2 vira o total3 foi que eu entendi como transformar uma sequencia de fibonacci em logica
