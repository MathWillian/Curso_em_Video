print('\033[7;34;40m', '=' * 40, 'MATH STORE', '=' * 40, '\033[0m')
compra = float(input('Digite o valor da compra: R$ '))

print('''FORMAS DE PAGAMENTO
[1] À VISTA (PIX ou DINHEIRO)
[2] À VISTA NO DÉBITO
[3] EM ATÉ 2X SEM JUROS
[4] 3X OU MAIS NO CRÉDITO''')

pag = int(input('Digite a forma de pagamento: '))

if pag == 1:
    print('O valor final a ser pago À VISTA (PIX OU DINHEIRO) será: R$ {:.2f}'.format(compra * 0.9))
elif pag == 2:
    print('O valor final a ser pago À VISTA NO DÉBITO será: R$ {:.2f}'.format(compra * 0.95))
elif pag == 3:
    print('O valor final a ser pago PARCELADO SEM JUROS será 2 parcelas de R$ {:.2f}'.format(compra / 2))
elif pag == 4:
    par = int((input('Digite em quantas parcelas: ')))
    c1 = compra * 1.2
    print('O VALOR a ser pago PARCELADO EM {}x COM JUROS será: R$ {:.2f}, {} de R$ {:.2f}'
          .format(par, c1, par, c1 / par))
else:
    print('\033[7;31;40m', 'FORMA DE PAGAMENTO INVÁLIDA!', '\033[0m')
