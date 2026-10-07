'''n1 = int(input('Numero para o fatorial: '))
n2 = ''
n3 = n1
n4 = n1
for c in range(n1 - 1, 0, -1):
    n1 = n1 * c
    n2 += str(f'{n3} x ')
    n3 -= 1

print(f'{n4}! = {n2}1 = {n1}')'''

n1 = int(input('Digite um numero para o seu fatorial: '))
c = n1
result = 1
print(f'{n1}! = ', end= '')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    result *= c
    c -= 1
print(f'{result}')
