num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[1;32mO nº {} foi divisível {} vezes\033[m'.format(num, tot))
if tot == 2:
    print('\n\033[1;32m Ele é PRIMO!\033[m')
else:
    print('\n\033[1;31m Ele não é PRIMO!\033[m')
