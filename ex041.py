from datetime import date

atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
dif = atual - ano

if 1 < dif <= 9:
    print('\033[1;34;40m', 'O atleta tem {} anos de idade.'.format(dif), '\33[0m')
    print('\033[1;34;40m', 'Classificação MIRIM!', '\33[0m')
elif dif == 1:
    print('\033[1;34;40m', 'O atleta tem {} ano de idade.'.format(dif), '\33[0m')
    print('\033[1;34;40m', 'Classificação MIRIM!', '\33[0m')
elif 14 >= dif > 9:
    print('\033[1;34;40m', 'O atleta tem {} anos de idade.'.format(dif), '\33[0m')
    print('\033[1;34;40m', 'Classificação INFANTIL!', '\33[0m')
elif 19 >= dif > 14:
    print('\033[1;34;40m', 'O atleta tem {} anos de idade.'.format(dif), '\33[0m')
    print('\033[1;34;40m', 'Classificação JÚNIOR!', '\33[0m')
elif 25 >= dif > 19:
    print('\033[1;34;40m', 'O atleta tem {} anos de idade.'.format(dif), '\33[0m')
    print('\033[1;34;40m', 'Classificação SÊNIOR!', '\33[0m')
elif dif > 25:
    print('\033[1;34;40m', 'O atleta tem {} anos de idade.'.format(dif), '\33[0m')
    print('\033[1;34;40m', 'Classificação MASTER!', '\33[0m')
else:
    print('\033[1;31;40m', 'Digite um ano válido!', '\33[0m')
