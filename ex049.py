tabuada = int(input("Tabuada do número: "))
for count in range(10):
    print('{} x {:>2} = {:>2}'.format(tabuada, count+1, tabuada*(count+1)))
