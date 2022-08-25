from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-' * 20)
print('Pense em um número de 0 a 5, eu vou tentar adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?  '))
print('PROCESSANDO.....')
sleep(3)
if jogador == computador:
    print('PARABÉNS!!! vc me venceu!!!')
else:
    print('GANHEI!!! eu pensei no número {} e nao no {}'.format(computador, jogador))

