import time

def calcProd():
    product = 1
    for i in range(1, 1000):
        product *= i
    return product

start_time = time.time()
print("Funkcija ja zapocela sa radom")
prod = calcProd()
end_time = time.time()
print("Funkcija ja zavrsila sa radom")
print("Potrebno vreme za izvrsavanje funkcije bilo je ", end_time-start_time)