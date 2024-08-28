
cena_jakne = float(input("Cena jakne: "))
popust = float(input("Popust: "))
broj_dana = int(input("Posle koliko dana sledi drugo umanjenje: "))
umanjenje2 = float(input("Unesite drugo umanjenje: "))

prvo_umanjenje = cena_jakne - cena_jakne * (popust/100)
drugo_umanjenje = prvo_umanjenje - umanjenje2

print("Trenutna cena jakne je: " + str(prvo_umanjenje) + " a posle " + str(broj_dana) + " cena jakne je " + str(drugo_umanjenje) + " dinara")
