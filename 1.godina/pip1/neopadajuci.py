a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))
c = int(input("Unesi broj c: "))

if(a>b):
    t = a
    a = b
    b = t
if(b>c):
    t = b
    b = c
    c = t
if(a>c):
    t = a
    a = c
    c = t
    
print(c, b, a)
