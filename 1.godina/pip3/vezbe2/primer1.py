def VremeUSekundama(ph, pm, ps):
    return ph*3600 + pm*60 + ps

def SekundeUVreme(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return h, m, s

vreme_pocetka = input('Unesi vreme pocetka: ').split(":")
vreme_zavrsetka = input('Unesi vreme zavrsetka: ').split(":")

ph, pm, ps = map(int, vreme_pocetka)
zh, zm, zs = map(int, vreme_zavrsetka)

ukupnoP = VremeUSekundama(ph, pm, ps)
ukupnoZ = VremeUSekundama(zh, zm, zs)
ukupno = ukupnoZ - ukupnoP

h, m, s = SekundeUVreme(ukupno)

print(h, m, s)