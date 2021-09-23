soma = 0
cont = 0
for impar in range(1, 500, 2):
    if impar % 3 == 0:
        soma += impar
        cont += 1
print('\n\033[1;30;41m', 'A soma dos {} valores que são divisíveis por 3 de 1 à 500 = {}'.format(cont, soma), '\033[0m')
