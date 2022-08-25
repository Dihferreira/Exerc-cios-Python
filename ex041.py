from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria Mirim!')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil!')
elif idade > 14 and idade <= 19:
    print('Categoria Junior!')
elif idade > 19 and idade <= 25:
    print('Categoria Sênior!')
else:print('Master!!!')


