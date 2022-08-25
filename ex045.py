print('{:=^40}'.format('Lojas Digão'))
preco = float(input('Valor do produto R$ '))
print('''Escolha forma de pagamento:
[ 1 ] A vista dinheiro/cheque 10% desconto
[ 2 ] A vista no cartão 5% desconto
[ 3 ] 2 vezes sem juros no cartão
[ 4 ] 3 x ou mais no cartão 20% juros''')
opção = int(input('Forma de pagamento? '))
if opção == 1:
    total = preco - (preco * 10 / 100)

elif opção == 2:
    total = preco - (preco * 5 / 100)

elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    nparc = int(input('Quantas parcelas? '))
    parcela = total / nparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(nparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
print('O valor de R${:.2f} custará R${:.2f}'.format(preco, total))


