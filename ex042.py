print('\033[7;30;45m-=-\033[m' * 20 )
print('Analisador de triângulos')
print('\033[7;30;45m-=-\033[m' * 20 )
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar TRIÂNGULO ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!!!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:print('Os segmentos acima não podem formar triângulo!!!')




