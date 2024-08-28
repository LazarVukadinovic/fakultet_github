# radni_dani = {
#     1: 'Ponedeljak',
#     2: 'Utorak',
#     3: 'Sreda',
#     4: 'Cetvrtak',
#     5: 'Petak'
#     #6: 'Subota',
#     #7: 'Nedelja'
# }

s = 'jabuka, hleb, kruska, jabuka, sljiva, hleb, mleko, jabuka, hleb'

proizvodi = s.split(', ')
spisak = dict() # {}

for proizvod in proizvodi:
    kolicina = spisak.get(proizvod)  #uzima vrednost po kljucu
    if kolicina:
        spisak[proizvod] += 1
    else:
        spisak[proizvod] = 1

najvecaKolicina = tuple(spisak.items())[0]

#sortiranje po kolicini/abecedi
for proizvod, kolicina in spisak.items():
    #proverava da li je ista kolicina i da li je proizvod najvece kolicine veci od proizvod sa spiska
    abcd_prednost = najvecaKolicina[1] == kolicina and najvecaKolicina[0] > proizvod
    if(najvecaKolicina[1] < kolicina or abcd_prednost):
        najvecaKolicina = proizvod, kolicina
    
print(f'Najkupovaniji proizvod je {najvecaKolicina[0]} -> kolicina {najvecaKolicina[1]}')