
pocetna_plata = float(input("Pocetna plata profesora: "))
uvecanje = float(input("Unesite procenat povecanja: "))

prvo_povecanje = pocetna_plata + pocetna_plata * (uvecanje / 100)
drugo_povecanje = prvo_povecanje + prvo_povecanje * (uvecanje / 100)
trece_povecanje = drugo_povecanje + drugo_povecanje * (uvecanje / 100)

print("Plata profesora u decembru ce biti: " + str(trece_povecanje) + " dinara")
