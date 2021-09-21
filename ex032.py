from datetime import date
ano= int(input('Qual ano deseja analizar? \nColoque 0 para o ano atual.\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} Não é BISSEXTO!'.format(ano))
