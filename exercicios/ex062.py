termo = int(input('Primeiro  termo: '))
razao = int(input('Razão da PA: '))
mais_termo = 10
soma = termo
contador_de_termos = 0
total = 0
while razao != 0 and mais_termo != 0:
    total += mais_termo
    while contador_de_termos <= total:
        print(f'{soma}', end= '')
        print(f' → ', end= '')
        soma += razao
        contador_de_termos += 1
    print('Pausa')
    mais_termo = int(input('Quanto termos você quer mostrar mais? : '))
print(f'Progressão finalizada com {contador_de_termos} termos mostrados.')
