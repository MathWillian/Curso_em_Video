vel = int(input("Digite a velocidade do carro: "))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você ultrapassou o limite de 80km/h, sua multa é de: R$ {:.792f}'.format(multa))
else:
    print('Você está na velociadade permitida.')
print("Tenha um bom dia, dirija com cuidado!")
