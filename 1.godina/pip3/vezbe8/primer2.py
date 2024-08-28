import csv
import os

file_path = os.path.join('.', 'vezbe8', 'gradovi.csv')
with open(file_path, newline='') as file:
    gradovi_reader = csv.reader(file)
    for row in gradovi_reader:
        print(gradovi_reader.line_num, row, sep=' - ')
