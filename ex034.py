sal = float(input('Qual seu salário? '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
    #print('Seu salário com aumento ficou R${}'.format(novo))
if sal > 1250:
    novo = sal + (sal * 10 / 100)
    #print('Seu salário com aumento ficou R${}'.format(novo))
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} '.format(sal, novo))


