sal = float(input('Qual o salário do funcionário? R$ '))
aum = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passara a ganhar R${:.2f}.'.format(sal, aum))

