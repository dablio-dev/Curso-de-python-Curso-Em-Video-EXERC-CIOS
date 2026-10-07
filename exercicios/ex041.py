from datetime import date
aluno = int (input ('Ano de nascimento do atleta: '))

ano = date.today().year
idade = ano - aluno
msg = 0

if idade <= 9:
    msg = 'MIRIM'
elif idade <= 14:
    msg = 'INFANTIL'
elif idade <= 19:
    msg = 'JÚNIOR'
elif idade <= 25:
    msg = 'SÊNIOR'
elif idade > 25:
    msg = 'MASTER'
print(f'Com {idade} anos atleta esta na categoria {msg}!')
