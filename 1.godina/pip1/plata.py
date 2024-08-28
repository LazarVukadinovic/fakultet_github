bruto_plata = float(input("Unesite bruto platu: "))


if(bruto_plata > 1000):
    neto_plata = bruto_plata - bruto_plata * 0.2
else:
    neto_plata = bruto_plata - bruto_plata * 0.15

print("Neto plata iznosi", neto_plata)
