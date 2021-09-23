peso = float(input('Digite o peso: '))
alt = float(input('Digite a altura: '))
IMC = peso / (alt ** 2)
print('O IMC dessa pessoa é {}'.format(IMC))

if IMC < 18.4:
    print('\33[1;31;40m', 'A pessoa está ABAIXO DO PESO!!!', '\033[0m')
elif 18.5 <= IMC < 25:
    print('\033[1;32;40m', 'A pessoa está no PESO IDEAL!', '\033[0m')
elif 25 <= IMC < 30:
    print('\033[1;33;40m', 'A pessoa está com SOBREPESO!', '\033[0m')
elif 30 <= IMC < 40:
    print('\033[1;35;40m', 'A pessoa está com OBESIDADE! Se cuide e busque um especialista.', '\033[0m')
else:
    print('\033[1;31;40m', 'A pessoa está com OBESIDADE MÓRBIDA!!! Deve procurar um especialista URGENTE!', '\033[0m')
