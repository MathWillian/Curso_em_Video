hvelho = 0
somaidade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('\33[7;31;30m', '=' * 15, '{}ª Pessoa'.format(p), '=' * 15, '\033[m')
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip().title()
    idade = int(input('Quantos anos a pessoa tem: '))
    sexo = str(input('É Homem - H ou Mulher - M? ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'H':
        hvelho = idade
        nomevelho = nome
    if sexo == 'H' and idade > hvelho:
        hvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade <= 20:
        totmulher20 += 1
media = somaidade / 4
print('\33[7;31;30m', '=' * 15, ' INDICES ', '=' * 15, '\033[m')
print('A média de idade do grupo é {:.0f} anos'.format(media))
if hvelho != 0:
    print('O homem mais velho do grupo tem {} anos e se chama {}'.format(hvelho, nomevelho))
if totmulher20 == 1:
    print('Ao todo temos 1 mulher com menos de 20 anos.')
elif totmulher20 == 0:
    print('Não temos mulheres com menos de 20 anos.')
else:
    print('Ao todo temos {} mulher com menos de 20 anos'.format(totmulher20))
