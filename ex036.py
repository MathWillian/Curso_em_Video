from termcolor import colored
casa = float(input('Digite o valor da casa que deseja comprar: R$ '))
salario = float(input('Qual valor do salário de quem irá comprar? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
trinta = salario * 0.3
parcela = casa / anos / 12
print(colored('Para financiar uma casa de R$ {:.2f}, em {} anos, a parcela é de R$ {:.2f}'.format(casa, anos, parcela),
              'yellow'))
if parcela <= trinta:
    print(colored('PARABÉNS! Seu empréstimo foi aprovado!'.format(parcela), 'green'))
else:
    print(colored("Empréstimo Negado!", 'red'))
