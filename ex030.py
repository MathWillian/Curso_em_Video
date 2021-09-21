número = int(input("Me diga um número qualquer: "))
res = número % 2
if res == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR!'.format(número))
    