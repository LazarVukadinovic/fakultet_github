#import math as m
#x = float(input("Unesi realan broj x: "))
#
#if(x <= 4):
#    y = m.sqrt(m.pow(x+2, 4))
#else:
#    y = x - 12

#if(x*y*y<20):
#    z = 14 - x*y
#else:
#    z = 4*x*y
#
#print(x, y, z)


import math as m
x = float(input("Unesi realan broj x: "))

if(0 <= x*x < 5):
    y = x - 18
elif(5 <= x*x < 18):
    y = abs(x+4)
elif(18 <= x*x < 88):
    y = m.sqrt(x*x-10)
else:
    y = 20
print(x, y)

