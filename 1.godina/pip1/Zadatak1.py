
jaja = int(input("Unesite kolicinu jaja: "))
mleko = int(input("Unesite kolicinu mleka (l): "))
secer = int(input("Unesite kolicinu secera (kg): "))
brasno = int(input("Unesite kolicinu brasna (kg): "))

mleko *= 1000
secer *= 1000
brasno *= 1000

tura_jaja = jaja // 4
tura_mleka = mleko // 500
tura_secera = secer // 250
tura_brasna = brasno // 600

tura = min(tura_jaja, tura_mleka, tura_secera, tura_brasna)

print(str(tura))
