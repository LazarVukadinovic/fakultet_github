import csv
import os

file_path = os.path.join('vezbe8', 'gradovi.csv')
csv_file = open(file_path, newline='')
csv_data = csv.reader(csv_file)

for row in csv_data:
    grad = row[8]
    if len(grad) > 10 and grad.__contains__('ll'):
        print(grad)

csv_file.close()