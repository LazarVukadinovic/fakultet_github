#include <stdio.h>
#include <stdlib.h>

typedef struct cvor
{
	int broj;
	struct cvor *levi, *desni;
}Cvor;

Cvor *alocirajCvor(int broj)
{
	Cvor *novi = (Cvor*)malloc(sizeof(Cvor));
	novi->broj = broj;
	novi->levi = NULL;
	novi->desni = NULL;
	
	return novi;
}

void dodaj(Cvor **stablo, int broj)
{
	Cvor *novi = alocirajCvor(broj);
	
	if(*stablo == NULL)
	{
		*stablo = novi;
		return;
	}
	
	Cvor *trenutni = *stablo;
	Cvor *prethodni;
	while(trenutni)
	{
		prethodni = trenutni;
		if(broj >= trenutni->broj)
			trenutni = trenutni->desni;
		else
			trenutni = trenutni->levi;
	}
	if(broj >= prethodni->broj)
		prethodni->desni = novi;
	else
		prethodni->levi = novi;
}

void ispis(Cvor *stablo)
{
	if(stablo)
	{
		ispis(stablo->levi);
		printf("%d\t", stablo->broj);
		ispis(stablo->desni);
	}
}

void formiraj(Cvor **stablo)
{
	int k;
	scanf("%d", &k);
	while(k)
	{
		dodaj(stablo, k);
		scanf("%d", &k);
	}
}

int max(Cvor *stablo)
{
	while(stablo->desni)
		stablo = stablo->desni;
	return stablo->broj;
}

int sumaStabla(Cvor *stablo)
{
	int suma = stablo->broj;
	if(stablo->levi)	suma += sumaStabla(stablo->levi);
	if(stablo->desni)	suma += sumaStabla(stablo->desni);
	return suma;
}

int dubinaStabla(Cvor *stablo)
{
	int dubinaL = 0, dubinaD = 0;
	if(stablo)
	{
		if(stablo->levi)	dubinaL = dubinaStabla(stablo->levi);
		if(stablo->desni)	dubinaD = dubinaStabla(stablo->desni);
		if(dubinaL > dubinaD)	return dubinaL + 1;
		else	return dubinaD + 1;
	}
	return 0;
}

int nadji(Cvor *stablo, int broj)
{
	int dubina = 0;
	if(stablo->broj == broj) 		return 1;
	else if(broj < stablo->broj)	dubina = nadji(stablo->levi, broj);
	else 	dubina = nadji(stablo->desni, broj);
	
	if(dubina)	return dubina + 1;
	else 		return 0;
}

//skripte
Cvor *findMax(Cvor *stablo) {
    if(stablo == NULL) return NULL;

    while(stablo->desni) stablo = stablo->desni;

    return stablo;
}

int caluculateSum(Cvor *stablo) {
    if(stablo == NULL) return 0;

    int leftSum = caluculateSum(stablo->levi);
    int rightSum = caluculateSum(stablo->desni);

    return stablo->broj + leftSum + rightSum;
}

int treeDepth(Cvor *stablo) {
    if (stablo == NULL) return 0;

    int leftDepth = treeDepth(stablo->levi);
    int rightDepth = treeDepth(stablo->desni);

    return 1 + (leftDepth > rightDepth ? leftDepth : rightDepth);
}

int findX(Cvor *stablo, int target) {
    int depth = 0;

    while(stablo) {
        depth++;

        if (stablo->broj == target) return depth;
        if (target < stablo->broj) stablo = stablo->levi;
        else stablo = stablo->desni;
    }
    return -1;
}

int main()
{
	Cvor *stablo = NULL;
	formiraj(&stablo);
	ispis(stablo);
	//printf("\nNajveci broj je %d", max(stablo));
	//printf("\nSuma stabla je %d", sumaStabla(stablo));
	//printf("\nDubina stabla je %d", dubinaStabla(stablo));
	//printf("\nNadji dubinu elementa je %d", nadji(stablo, 4));
	
	printf("\nNajveci broj je %d", findMax(stablo)->broj);
	printf("\nSuma stabla je %d", caluculateSum(stablo));
	printf("\nDubina stabla je %d", treeDepth(stablo));
	printf("\nNadji dubinu elementa je %d", findX(stablo, 4));
}
