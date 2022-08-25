#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
vdc = float(input('Valor da casa R$ '))
salario = float(input('Salário do comprador R$ '))
anos = int(input('Quantos anos de financiamento: '))
mes = anos * 12
prest = vdc / mes
print('Para pagar uma casa de R${} em {} anos a prestação sera de R${:.2f}'.format(vdc, anos, prest))
a = salario * 30 / 100
if prest <= a:
    print('Empréstimo pode ser concedido!')
else:print('Empréstimo negado!!!')
