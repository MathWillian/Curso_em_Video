frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantidade de vezes ou vez que a letra A aparece? {} '.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
