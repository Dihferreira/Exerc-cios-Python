dis = float(input('Qual a distância da sua viagem: '))
print('Vc esta prestes a começar uma viagem de {}km.'.format(dis))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('Valor da viagem é R${:.2f}'.format(preço))