nome = str(input("Digite seu nome completo: "))
print('Analisando seu nome: {}'.format(nome))
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome tem {} letras'.format(separa[0]))
