salario = float(input('Insira o seu salário: '))
aumento = salario * 1.15
# pode ser feito a % tbm com essa fórmula : salário + (salário * 15 / 100)

print('O salário de R$ {:.2f} com o aumento de 15% fica R$ {:.2f}.'.format(salario, aumento))
