import os
os.chdir(os.path.join('.', 'vezbe', 'vezbe4'))

pocetna = input("Unesi pocetnu putanju: ")
for putanjaFoldera, podfolderi, fajlovi in os.walk(pocetna):
    kod = "_".join(podfolder.lower() for podfolder in sorted(podfolderi))
    if not kod:
        kod = "_".join(fajl.lower() for fajl in sorted(fajlovi))
    
    velicinaFajlova = []
    for fajl in fajlovi:
        putanja = os.path.join(putanjaFoldera, fajl)
        velicinaFajlova.append(os.path.getsize(putanja))
    
    print("Folder: ", putanjaFoldera)
    print("Kod: ", kod)
    print("Velicina fajlova: ", sum(velicinaFajlova))