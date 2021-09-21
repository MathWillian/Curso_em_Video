salário = float(input('Digite o salário do funcionário: R$ '))
if salário >= 1250.00:
    print('O funcionário passará a ganhar R$ {:.2f}'.format(salário * 1.1))
else:
    print('O funcionário passará a ganhar R$ {:.2f}'.format(salário * 1.15))
