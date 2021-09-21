from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print('A hipotenusa dos catetos {} e {}, é {:.2f}'.format(co, ca, hypot(co, ca)))
