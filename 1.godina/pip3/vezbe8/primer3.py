import csv
import os

file_path = os.path.join('vezbe8', 'ljudi.csv')
file_ljudi = open(file_path, 'w', newline='')

ljudi_writer = csv.writer(file_ljudi, delimiter='|')
ljudi_writer.writerow(['Ime', 'Prezime'])
ljudi_writer.writerow(['Pera', 'Peric'])
ljudi_writer.writerow(['Mika', 'Mikic'])

file_ljudi.close()