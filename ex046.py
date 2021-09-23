from time import sleep
for i in range(10, -1, -1):
    if i < 10:
        print('\033[7;32;40m', '', end='')
    print('\033[7;32;40m', '=' * 8, i,  '=' * 9, '\033[0m')
    sleep(1)
print('\033[7;31;40m', ' BOOM! BOOM! POOOW!!!', '\033[0m')
