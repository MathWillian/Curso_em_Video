n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2 > n3:
    print('O número {} é o maior e {} é o menor'. format(n1, n3))
if n1 > n2 < n3 < n1:
        print('O número {} é o maior e {} é o menor'.format(n1, n2))
if n1 < n2 > n3 > n1:
    print('O número {} é o maior e {} é o menor'. format(n2, n1))
if n1 < n2 > n3 < n1:
    print('O número {} é o maior e {} é o menor'. format(n2, n3))
if n1 < n2 < n3:
    print('O número {} é o maior e {} é o menor'.format(n3, n1))
if n1 > n2 < n3 > n1:
    print('O número {} é o maior e {} é o menor'.format(n3, n2))
