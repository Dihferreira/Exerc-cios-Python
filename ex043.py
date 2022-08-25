peso = float(input('Qual seu peso? (kg) '))
alt = float(input('Qual sua altura: '))
imc = peso / (alt ** 2)
print('Seu imc é de {:.2f}'.format(imc))
if imc < 18.5:
    print('VC esta abaixo do seu peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:print('Obesidade Mórbida!')

