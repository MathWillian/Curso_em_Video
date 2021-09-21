dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
aluguel = (dias * 60) + (km * 0.15)

print('Um carro alugado por {} dias, que rodou {}km, terá um aluguel de R$ {:.2f}'.format(dias, km, aluguel))
