nota1 = float (input ('Digite a primeira nota: '))
nota2 = float (input ('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
msg = 0

if media < 5:
    msg = '\033[1;31mREPROVADO\033[m'
elif 5 <= media <= 6.9:
    msg = '\033[1;33mEM RECUPERAÇÃO\033[m'
else:
    msg = '\033[1;32mAPROVADO\033[m'
print(f'Com a media {media:.1f} o aluno esta {msg}!')
