d = float(input('Qual é s distância a ser percorrida?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    print('A viagem ficará no valor de: R$ {:.2f}'.format(d * 0.5))
else:
    print('A viagem ficará no valor de R$ {:.2f}'.format(d * 0.45))
print('Tenha uma excelente viagem!\nObrigado por escolher a Mateus Tur!')
