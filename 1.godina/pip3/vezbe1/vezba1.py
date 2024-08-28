
# def Kvadrat_Kub(n):
#     return n*2, n**3

# n = int(input('Unesi broj:'))


# kvadrat, kub = Kvadrat_Kub(n)
# print(f'kvadrat={kvadrat}, kub={kub}')

# #1. zadatakL
# def PronadjiBrojeve(n, m):
#     br = 0
#     for i in range(n, m+1):
#         s = str(i)
#         flag = False
#         for x in s:
#             if(s.count(x) > 1):
#                 flag = True
#                 break
#         if(not flag):
#             br += 1
#             flag = False
#     return br

# n = int(input('Unesi broj n:'))
# m = int(input('Unesi broj m:'))

# print(PronadjiBrojeve(n, m))

# #1. zadatak
# def Ima_Duplikate(broj):
#     cifre = []
#     while broj:
#         cifra = broj % 10
#         if cifra in cifre:
#             return True
#         cifre.append(cifra)
#         broj //= 10



# n = int(input('Unesi broj n:'))
# m = int(input('Unesi broj m:'))

# brojevi = [broj for broj in range(n, m+1) if not Ima_Duplikate(broj)]
# print(len(brojevi))

# #2. zadatak
# def round_robin(lista_listi):
#     max_len = max(len(lists) for lists in lista_listi)

#     rezultat = []
#     idx = 0
#     while(idx < max_len):
#         for zahtevi_korisnika in lista_listi:
#             if idx < len(zahtevi_korisnika):
#                 rezultat.append(zahtevi_korisnika[idx])
#         idx += 1
#     return rezultat

# lista = ['AB', 
#         'CD', 
#         'EFGIH', 
#         'I', 
#         'JKL', 
#         'NM'
#     ]

# print(round_robin(lista))

#  # 3. zadatak
# from string import digits, punctuation

# reci = input('Unesi tekst: ').lower().split()

# palindromi = []
# for rec in reci:
#     if len(rec) < 3:
#         continue

#     rec = ''.join([c for c in rec if c not in punctuation and c not in digits])
#     obrnuta_rec = rec[::-1]

#     if(rec == obrnuta_rec and rec not in palindromi):
#         palindromi.append(rec)

# print(palindromi)


# def stampaj_matricu(matrica):
#     for red in matrica:
#         for element in red:
#             print(element, end=' ')
#         print()

# def unesi_matricu(m, n):
#     matrica = m*[n*[0]]
#     for i in range(m):
#         for j in range(n):
#             matrica[i][j] = int(input('Unesi broj: '))
#     return matrica

# def proveriRedove(matrica, magicnaKonstanta):
#     for red in matrica:
#         if sum(red) != magicnaKonstanta:
#             return False
#     return True

# def proveriKolone(matrica, magicnaKonstanta):
#     for i in range(len(matrica)):
#         suma = 0
#         for red in matrica:
#             suma += red[i]
#         if suma != magicnaKonstanta:
#             return False
#     return True

# def proveriGlavnuDijagonalu(matrica, magicnaKonstanta):
#     n = len(matrica)
#     return sum(matrica[i][i] for i in range(n)) == magicnaKonstanta

# def proveriSporednuDijagonalu(matrica, magicnaKonstanta):
#     n = len(matrica)
#     suma = sum(matrica[i][n-1-i] for i in range(n))
#     return suma == magicnaKonstanta

# def magicanKvadrat(matrica, magicnaKonstanta):
#     return all([
#         proveriRedove(matrica, magicnaKonstanta),
#         proveriKolone(matrica, magicnaKonstanta),
#         proveriGlavnuDijagonalu(matrica, magicnaKonstanta),
#         proveriSporednuDijagonalu(matrica, magicnaKonstanta)
#     ])

# matrica = [
#     [2, 7, 6],
#     [9, 5, 1],
#     [4, 3, 8]
# ]

# magicnaKonstanta = int(input('Unesite konstantu: '))

# stampaj_matricu(matrica)
# rezultat = magicanKvadrat(matrica, magicnaKonstanta)

# print(rezultat)
# print(f"Uneta matrica {'jeste' if rezultat else 'nije'} magican kvadrat")



brojPredmeta = int(input('Unesite broj predmeta po polici: '))

listaMasa = input("Unesi mase: ").split(' ')
listaMasa = list(map(int, listaMasa))

listaMasaPoPolici = []

masa = 0
for i in range(len(listaMasa)):
    masa += listaMasa[i]
    if(i%brojPredmeta == brojPredmeta-1):
        listaMasaPoPolici.append(masa)
        masa = 0

if masa:
    listaMasaPoPolici.append(masa)

print(' '.join(str(x) for x in listaMasaPoPolici))
print(listaMasaPoPolici.index(max(listaMasaPoPolici))+1)


