a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))
c = int(input("Unesi broj c: "))

if(a >= b >= c):
    a *= 2
    b *= 2
    c *= 2
else:
    a = abs(a)
    b = abs(b)
    c = abs(c)

print(a, b, c)
