import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
#hi =  (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))
