a1 = float(input('Unesti koeficijent a1: '))
b1 = float(input('Unesti koeficijent b1: '))

a2 = float(input('Unesti koeficijent a2: '))
b2 = float(input('Unesti koeficijent b2: '))

if(a1 == a2):
    if(b1 == b2):
        print("Prave su paralelne")
    else:
        print("Prave su podudarne")
else:
    x = (b1-b2)/(a2-a1)
    y = a1 * x + b1

    print("Presek je: (" + str(x) + "," + str(y) + ")")
