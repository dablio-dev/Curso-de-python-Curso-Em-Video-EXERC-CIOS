expressao = input('Digite a expressão: ')
pilha = list()
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Esta expressão é valida!')
else:
    print('Esta expressão não é valida!')
#não consegui desenvolver esta logica por conta propria, esse ex eu precisei da resolução do para conseguir desenvolver