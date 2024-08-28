import json, csv
import os

folder = 'podaci'
extension = '.json'
end_folder = 'izlaz'

def obradiRezisere(folder, extension):
    filmovi = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(path, file)

                with open(file_path, newline='', encoding='UTF-8') as json_file:
                    json_data = json.loads(json_file.read())

                for obj in json_data:
                    filmovi[obj['Director']] = filmovi.get(obj['Director'], 0) + float(obj['Gross'])
    return filmovi

def obradiZanrove(folder, extension):
    zanrovi = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(path, file)

                with open(file_path, newline='', encoding='UTF-8') as json_file:
                    json_data = json.loads(json_file.read())

                for obj in json_data:
                    for genre in obj['Genres']:
                        zanrovi[genre] = zanrovi.get(genre, 0) + 1
    return zanrovi

csv_path = os.path.join(end_folder, 'pera.csv')
with open(csv_path, 'w', newline='') as csv_file:
    header = ['ImeReditelja', 'ukupnaZarada']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()
    for reditelj, zarada in obradiRezisere(folder, extension).items():
        csv_writer.writerow({'ImeReditelja':reditelj, 'ukupnaZarada':zarada})

csv_path = os.path.join(end_folder, 'pera-statistika.csv')
with open(csv_path, 'w', newline='') as csv_file:
    header = ['ImeZanra', 'brojFilmovaSaTimZanrom']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()
    for zanr, ukupno in obradiZanrove(folder, extension).items():
        csv_writer.writerow({'ImeZanra':zanr, 'brojFilmovaSaTimZanrom':ukupno})