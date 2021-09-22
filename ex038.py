from termcolor import colored
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print(colored('O número {} é o maior.'.format(n1), 'green'))
elif n2 > n1:
    print(colored('O número {} é o maior.'.format(n2), 'red'))
else:
    print(colored('Os números são iguais!', 'yellow'))
