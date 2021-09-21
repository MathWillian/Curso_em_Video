l = float(input("Qual a largura da parede? "))
a = float(input('Qual a altura da parede? '))
area = l * a
tinta = area / 2

print('Em uma parede de area {}, usa-se {:.2}l de tinta para pinta-la'.format(area, tinta))
