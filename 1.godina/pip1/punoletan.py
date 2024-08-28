danRodjenja = int(input("Dan rodjenja: "))
mesecRodjenja = int(input("Mesec rodjenja: "))
godinaRodjenja = int(input("Godina rodjenja: "))

dan = int(input("Dan provere: "))
mesec = int(input("Mesec provere: "))
godina = int(input("Godina provere: "))

if(godina - godinaRodjenja > 18):
    print("Osoba je punoletna")
elif((mesec < mesecRodjenja) and (godina - godinaRodjenja == 18)):
    print("Osoba je punoletna")
elif((mesec == mesecRodjenja) and (dan <= danRodjenja) and (godina - godinaRodjenja == 18)):
    print("Osoba je punoletna")
else:
    print("Osoba nije punoletna")
