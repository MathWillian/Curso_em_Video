pt = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = pt + (10 -1) * razão
for i in range(pt, décimo + razão, razão):
    print('\033[1;32;40m', '{}'.format(i), end='→')
print(' FIM!', '\033[0m')
