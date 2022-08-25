real = float(input('Quanto dinheiro vc tem em sua carteira? R$'))
print(f'Com R${real} vc pode comprar U${(real / 3.27)}')
euro = real / 4.35
print('Com R${} vc pode comprar U${}'.format(real, euro))


