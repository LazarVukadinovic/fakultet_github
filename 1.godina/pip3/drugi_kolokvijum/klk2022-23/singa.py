import csv
import os
import subprocess
import time

folder = 'files'
extension = '.csv'

if not os.path.exists(folder):
     os.mkdir(folder)

def ucitajAutore(folder, extension):
    artists_dict = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension) and file.__contains__('authors'):
                file_path = os.path.join(path, file)
                with open(file_path, newline='') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                
                    for row in csv_reader:
                        artist_from_dict = row  #uzima jednog artista
                        ZbirnaPopularnost = float(artist_from_dict.get('ZbirnaPopularnost', 0)) + float(row['ZbirnaPopularnost'])
                        BrojPesama = int(artist_from_dict.get('BrojPesama', 0)) + int(row['BrojPesama'])

                        artist_from_dict['ZbirnaPopularnost'] = str(ZbirnaPopularnost)
                        artist_from_dict['BrojPesama'] = str(BrojPesama)
                        artists_dict[row['ImeAutora']] = artist_from_dict
    artists_list = sorted(artists_dict.values(), key=lambda artist: (-float(artist['ZbirnaPopularnost'])/float(artist['BrojPesama']), artist['ImeAutora']))
    return artists_list

def ucitajZanrove(folder, extension):
    godine_dict = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension) and file.__contains__('genres'):
                file_path = os.path.join(path, file)

                with open(file_path, newline='') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                
                    for row in csv_reader:
                        godina = godine_dict.get(row['Godina'], {})
                        godina[row['Zanr']] = godina.get(row['Zanr'], 0) + int(row['BrojPesama'])

                        godine_dict[row['Godina']] = godina
    return godine_dict

material_sub = subprocess.Popen(['python', 'material.py'])
infotools_sub = subprocess.Popen(['python', 'infotools.py'])

if material_sub.poll() == None or infotools_sub.poll() == None:
    time.sleep(1)

if material_sub.poll() != 0 or infotools_sub.poll() != 0:
    print('Greska u izvrsavanju')
    exit(0)

artists_list = ucitajAutore(folder, extension)
best_artist = artists_list[0]
print(f'{best_artist['ImeAutora']} {float(best_artist['ZbirnaPopularnost'])/float(best_artist['BrojPesama'])}')

lista = []
for godina, genres_dict in ucitajZanrove(folder, extension).items():
    zanrovi = list(genres_dict.items())
    zanrovi = sorted(zanrovi, key=lambda x: (-x[1], x[0]))
    lista.append(tuple([godina, zanrovi[0][0], zanrovi[0][1]]))

lista = sorted(lista, key=lambda x: int(x[0]))
for godina, zanr, num in lista:
    print(godina, zanr, num)