import csv
import os

file_path = os.path.join('.', 'vezbe8', 'gradovi.csv')
with open(file_path, newline='') as file:
    gradovi_reader = csv.reader(file)
    gradovi = list(gradovi_reader)

print(gradovi[0])       # nulti red - zaglavlje
print(gradovi[1])       # prvi red
print(gradovi[1][8])    # konkretna celija
