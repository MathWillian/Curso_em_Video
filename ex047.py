for par in range(2, 51, 2):
    if par < 50:
        print('\033[1;30;41m', par, '\033[0m', end=',')
    if par == 50:
        print('\033[1;30;41m', par, '\033[0m')
print('\033[1;30;41m', '-=' * 28, 'FIM!' , '=-' * 28, '\033[0m')
