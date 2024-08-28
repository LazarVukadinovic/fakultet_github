import csv
import os

file_path = os.path.join('vezbe8', 'ljudi.csv')
ljudi = open(file_path, 'w', newline='')

header = ['Ime', 'Prezime']
ljudi_writer = csv.DictWriter(ljudi, fieldnames=header)
ljudi_writer.writeheader()
ljudi_writer.writerow({'Ime': 'Laza', 'Prezime': 'Lazic'})
ljudi_writer.writerows([{'Ime': 'Zika', 'Prezime': 'Zikic'},
                       {'Ime': 'Marko', 'Prezime': 'Markovic'}])

ljudi.close()