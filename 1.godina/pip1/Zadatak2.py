
sat1 = int(input("Unesite sat1: "))
min1 = int(input("Unesite min1: "))

sat2 = int(input("Unesite sat2: "))
min2 = int(input("Unesite min2: "))

min1_ukupno = sat1*60 + min1
min2_ukupno = sat2*60 + min2

razlika = min2_ukupno - min1_ukupno
sati = razlika // 60
minuti = razlika % 60

print("Sati " + str(sati) + " minuti " + str(minuti))
