import random

def GenerisiMatricu(m, n):
    matrica = [[random.randrange(2) for _ in range(n)] for _ in range(m)]
    return matrica

def UnesiMatricu(m, n):
    matrica = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrica[i][j] = int(input())
    return matrica

def IspisiMatricu(matrica, m, n):
    for i in range(m):
        for j in range(n):
            print(matrica[i][j], end='  ')
        print()
        
def ProveriOkolinu(matrica, i, j):
    brojMina = 0
    for q in range(-1, 2):
        for p in range(-1, 2):
            redInd = 0 <= i+q < len(matrica)        # da li je index reda u opsegu
            kolonaInd = 0 <= j+p < len(matrica[0])  # da li je index kolone u opsegu
            
            if(redInd and kolonaInd):
                if((q != 0 or p != 0) and matrica[i+q][j+p]):
                    brojMina += 1
    return brojMina 


m = int(input('Unesi broj redova: '))
n = int(input('Unesi broj kolona: '))
matrica = GenerisiMatricu(m, n)
#matrica = UnesiMatricu(m, n)

print("\nUneta matrica: ")
IspisiMatricu(matrica, m, n)

print("\nNova matrica: ")
matricaIspis = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        matricaIspis[i][j] = ProveriOkolinu(matrica, i, j)

IspisiMatricu(matricaIspis, m, n)
