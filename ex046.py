from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')
print('-=' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('JOGADOR VENCEL!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('Jogada imválida!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')
    else:
        print('Jogada imválida!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('Jogada imválida!')
