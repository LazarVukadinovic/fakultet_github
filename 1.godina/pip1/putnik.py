t1 = float(input()); v1 = float(input())
t2 = float(input()); v2 = float(input())
t3 = float(input()); v3 = float(input())

s1 = t1 * v1
s2 = t2 * v2
s3 = t3 * v3

pola_puta = (s1+s2+s3)/3

if(pola_puta <= s1):
    t = pola_puta / v1
elif(pola_puta <= s2):
    t = t1 + (pola_puta-s1)/v2
else:
    t = t1+t2 + (pola_puta - s1-s2)/v3

print(t)
