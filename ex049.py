num = int(input('Digite um número para ver Tabuada: '))
print('-='*9)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-='*9)

