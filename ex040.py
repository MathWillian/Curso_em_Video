from termcolor import colored

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('Média = {}'.format(média))

if média >= 7.0:
    print(colored('PARABÉNS! Aluno APROVADO!', 'green'))
elif 5 <= média < 7:
    print(colored('Aluno em RECUPERAÇÃO!', 'yellow'))
elif média < 5:
    print(colored('Aluno REPROVADO!', 'red'))
