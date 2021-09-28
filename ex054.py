from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
if totmaior == 1:
    print('Ao todo tivémos {} pessoa maior de idade'.format(totmaior))
elif totmaior == 0:
    print('Não houve registo de pessoa maior de idade!')
else:
    print('Ao todo tivémos {} pessoas maiores de idade'.format(totmaior))
if totmenor == 1:
    print('Ao todo tivémos {} pessoa menor de idade'.format(totmenor))
elif totmenor == 0:
    print('Não houve registo de pessoa menor de idade!')
else:
    print('Ao todo tivémos {} pessoas menores de idade'.format(totmenor))
