from random import randint
from time import sleep
print('''ESCOLHA UMA OPÇÃO:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('Qual é a sua escolha? '))

print('\033[7;36;40m', '=' * 15, 'JO ', '=' * 14, '\033[0m')
sleep(1)
print('\033[7;36;40m', '=' * 15, 'KEM', '=' * 14, '\033[0m')
sleep(1)
print('\033[7;36;40m', '=' * 15, ' PÔ', '=' * 14, '\033[0m')
sleep(1)
print('  O computador escolheu {}'.format(itens[computador]))
print('  E o jogador escolheu {}'.format(itens[jogador]))
print('\033[7;36;40m', '=' * 34, '\033[0m')

if computador == 0: # PEDRA
    if jogador == 0:
        print('\033[7;30;43m', ' ' * 13, 'EMPATE', ' ' * 13, '\033[0m')
    elif jogador == 1:
        print('\033[7;32;40m', ' ' * 8, 'JOGADOR VENCEU!!!', ' ' * 7, '\033[0m')
    elif jogador == 2:
        print('\033[7;31;40m', ' ' * 6, 'COMPUTADOR VENCEU!!!', ' ' * 6, '\033[0m')
    else:
        print('\033[7;37;41m', ' ' * 7, 'JOGADA INVÁLIDA!!!', ' ' * 7, '\033[0m')

if computador == 1: # PAPEL
    if jogador == 0:
        print('\033[7;31;40m', ' ' * 6, 'COMPUTADOR VENCEU!!!', ' ' * 6, '\033[0m')
    elif jogador == 1:
        print('\033[7;30;43m', ' ' * 13, 'EMPATE', ' ' * 13, '\033[0m')
    elif jogador == 2:
        print('\033[7;32;40m', ' ' * 8, 'JOGADOR VENCEU!!!', ' ' * 7, '\033[0m')
    else:
        print('\033[7;37;41m', ' ' * 7, 'JOGADA INVÁLIDA!!!', ' ' * 7, '\033[0m')

if computador == 2: # TESOURA
    if jogador == 0:
        print('\033[7;32;40m', ' ' * 8, 'JOGADOR VENCEU!!!', ' ' * 7, '\033[0m')
    elif jogador == 1:
        print('\033[7;31;40m', ' ' * 6, 'COMPUTADOR VENCEU!!!', ' ' * 6, '\033[0m')
    elif jogador == 2:
        print('\033[7;30;43m', ' ' * 13, 'EMPATE', ' ' * 13, '\033[0m')
    else:
        print('\033[7;37;41m', ' ' * 7, 'JOGADA INVÁLIDA!!!', ' ' * 7, '\033[0m')
