import subprocess, time
import csv
import os

extension = '.csv'
end_folder = 'izlaz'
if not os.path.exists(end_folder):
    os.mkdir(end_folder)

def ucitajFilmove(folder, extension):
    filmovi = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension) and not file.__contains__('statistika'):
                file_path = os.path.join(path, file)
                with open(file_path, newline='') as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    for row in csv_reader:
                        filmovi[row['ImeReditelja']] = filmovi.get(row['ImeReditelja'], 0) + float(row['ukupnaZarada'])
    return filmovi

def ucitajZanrove(folder, extension):
    zanrovi = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension) and file.__contains__('statistika'):
                file_path = os.path.join(path, file)
                with open(file_path, newline='') as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    for row in csv_reader:
                        zanrovi[row['ImeZanra']] = zanrovi.get(row['ImeZanra'], 0) + int(row['brojFilmovaSaTimZanrom'])
    return zanrovi

pera_sub = subprocess.Popen(['python', 'pera.py'])
zika_sub = subprocess.Popen(['python', 'zika.py'])

if pera_sub.poll() == None or zika_sub.poll() == None:
    time.sleep(1)

if pera_sub.poll() != 0 or zika_sub.poll() != 0:
    print('Greska pri izvrsavanju fajlova')
    exit(0)

lista = ucitajFilmove(end_folder, extension).items()
lista = sorted(lista, key=lambda x: x[1], reverse=True)
print(f'{lista[0][0]} {lista[0][1]}')

lista = ucitajZanrove(end_folder, extension).items()
lista = sorted(lista, key=lambda x: x[1], reverse=True)
for genre, num in lista:
    print(f'{genre} {num}')