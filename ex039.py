from termcolor import colored
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print(colored('Você tem que se alistar IMEDIATAMENTE!', 'green'))
elif idade < 18:
    saldo = 18 - idade
    print(colored('Ainda faltam {} anos para se alistar.'.format(saldo), 'yellow'))
    ano = atual + saldo
    print(colored('Seu alistamento será em {}.'.format(ano), 'yellow'))
elif idade > 19:
    saldo = idade - 18
    print(colored('ATENÇÃO!!! Você já deveria ter se alistado há {} anos!'.format(saldo), 'red'))
    ano = atual - saldo
    print(colored('Seu alistamento foi em {}!'.format(ano), 'red'))
elif idade == 19:
    saldo = idade - 18
    print(colored('ATENÇÃO!!! Você já deveria ter se alistado no ano passado, {}!'.format(saldo), 'red'))
    ano = atual - saldo
    print(colored('Seu alistamento foi em {}!'.format(ano), 'red'))
else:
    print('Digite um ano válido!')
