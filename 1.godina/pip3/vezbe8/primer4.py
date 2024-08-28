import csv
import os

file_path = os.path.join('vezbe8', 'gradovi.csv')
file_gradovi = open(file_path, newline='')

gradovi_reader = csv.DictReader(file_gradovi, quotechar='"')
# svaki row je zaseban recnik
for row in gradovi_reader:
    print(f"Grad: {row['City']}, State: {row['State']}")

file_gradovi.close()