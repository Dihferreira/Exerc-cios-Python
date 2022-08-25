n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5.0:
    print('REPROVADO!!!')
elif media > 5.0 and media < 7.0:
    print('RECUPERAÇÃO!!!')
elif media > 7.0:
    print('!!!APROVADO!!!')

