import random

# Napomena: Konvencija u Python-u je da se nazivi funkcija pisu malim slovom, tj.
#           da budu u "snake case"-u, npr. lower_case_with_underscores

def generisi_matricu(m, n):
    matrica = [[random.randrange(2) for _ in range(n)] for _ in range(m)]
    return matrica

def unesi_matricu(m, n):
    # Napomena: moze da se zapise i kao: matrica = [[0]*n]*m 
    matrica = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrica[i][j] = int(input())
    return matrica

def ispisi_matricu(matrica, m, n):
    for i in range(m):
        for j in range(n):
            print(matrica[i][j], end='  ')
        print()
        
def proveri_okolinu(matrica, i, j):
    broj_mina = 0
    # Napomena: mozemo da koristimo i skupove, npr. `{-1, 0, 1}`. Znamo koje su vrednosti, one se ne menjaju i
    # redosled nam nije bitan. Time ne moramo da pravimo range. u svakoj iteraciji prve petlje.
    # Pristup sa range je takodje u redu.
    offsets = {-1, 0, 1}
    for q in offsets:
        for p in offsets:
            # Napomena:
            # * promenljive takodje treba pisati u snake_case stilu, npr. redInd -> red_ind
            # * u Python-u zagrade nisu neophodne u if-u. Ideja je da se sto manje pise nesto
            #   sto se podrazumeva i sto otezava citanje koda
            # 
            # redInd = 0 <= i+q < len(matrica)        # da li je index reda u opsegu
            # kolonaInd = 0 <= j+p < len(matrica[0])  # da li je index kolone u opsegu
            
            red_ind = 0 <= i+q < len(matrica)        # da li je index reda u opsegu
            kolona_ind = 0 <= j+p < len(matrica[0])  # da li je index kolone u opsegu
            
            # Napomena:
            # * izbacene nepotrebne zagrade
            # * spojeni uslovi
            # * umesto dodavanja jedinice, dodali smo vrednost polja matrice jer sadrzi
            #   0 ili 1, pa ako nema bombe onda ce biti dodata 0 na broj mina, odnosno nece
            #   doci do neke promene
            # 
            # if(redInd and kolonaInd):
            #     if((q != 0 or p != 0) and matrica[i+q][j+p]):
            #         brojMina += 1

            if red_ind and kolona_ind and (q != 0 or p != 0):
                broj_mina += matrica[i+q][j+p]
    return broj_mina 


m = int(input('Unesi broj redova: '))
n = int(input('Unesi broj kolona: '))
matrica = generisi_matricu(m, n)
#matrica = unesi_matricu(m, n)

print("\nUneta matrica: ")
ispisi_matricu(matrica, m, n)

print("\nNova matrica: ")
# Napomena: moze da se zapise i kao: matrica = [[0]*n]*m 
# matrica_ispis = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        ispisi_matricu[i][j] = proveri_okolinu(matrica, i, j)

ispisi_matricu(ispisi_matricu, m, n)
