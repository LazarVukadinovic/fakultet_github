
from string import digits, punctuation

text = 'Free software, libre software, or libreware[1][2] is computer software distributed under terms that allow users to run software for any purpose as well as to study, change, and distribute it and any adapted versions.[3][4][5][6].'

slova = [c for c in text.lower() if c not in punctuation + digits]
reci = ''.join(slova).split()

recnik = {}

for rec in reci:
    # rec[0] vraca prvo slovo reci
    reci_slova = recnik.get(rec[0])
    if not reci_slova:
        recnik[rec[0]] = {rec: 1}
    else:
        reci_slova[rec] = reci_slova.get(rec, 0) + 1
        recnik[rec[0]] = reci_slova


slova = sorted(recnik.keys())

for slovo in slova:
    print('Slovo', slovo)
    print('-' * 5)
    reci = recnik[slovo].items()
    sortiraneReci = sorted(reci, key=lambda r: (len(r[0]), r[1], r[0]))
    for rec, ponavljanja in sortiraneReci:
        print(rec, ponavljanja)
    print()