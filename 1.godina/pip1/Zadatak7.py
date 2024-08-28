
s1 = int(input("Sati1: "))
m1 = int(input("Minuti1: "))

s2 = int(input("Sati2: "))
m2 = int(input("Minuti2: "))

s3 = int(input("Sati3: "))
m3 = int(input("Minuti3: "))


minuti1 = s1 * 60 + m1
minuti3 = s3 * 60 + m3

razlika = minuti3 - minuti1

print("Prvoplasirani biciklista je cekao " + str(razlika) + " minuta treceplasiranog da zavrsi trku")
