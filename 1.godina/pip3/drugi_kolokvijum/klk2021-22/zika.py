import bs4, csv
import os

folder = 'podaci'
extension = '.xml'
end_folder = 'izlaz'

def obradiRezisere(folder, extension):
    filmovi = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(path, file)

                with open(file_path, newline='', encoding='UTF-8') as xml_file:
                    soup = bs4.BeautifulSoup(xml_file, features='html.parser')

                    for obj in soup.select('Movie'):
                        director = obj.find('director').get_text().strip()
                        gross = float(obj.find('gross').get_text().strip())
                        filmovi[director] = filmovi.get(director, 0) + gross
    return filmovi

def obradiZanrove(folder, extension):
    zanrovi = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(path, file)

                with open(file_path, newline='', encoding='UTF-8') as xml_file:
                    soup = bs4.BeautifulSoup(xml_file, features='html.parser')

                    for obj in soup.select('Movie'):
                        for genre in obj.select('genre'):
                            genre = genre.get_text().strip()
                            zanrovi[genre] = zanrovi.get(genre, 0) + 1
    return zanrovi

csv_path = os.path.join(end_folder, 'zika.csv')
with open(csv_path, 'w', newline='') as csv_file:
    header = ['ImeReditelja', 'ukupnaZarada']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()
    for reditelj, zarada in obradiRezisere(folder, extension).items():
        csv_writer.writerow({'ImeReditelja':reditelj, 'ukupnaZarada':zarada})

csv_path = os.path.join(end_folder, 'zika-statistika.csv')
with open(csv_path, 'w', newline='') as csv_file:
    header = ['ImeZanra', 'brojFilmovaSaTimZanrom']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()
    for zanr, ukupno in obradiZanrove(folder, extension).items():
        csv_writer.writerow({'ImeZanra':zanr, 'brojFilmovaSaTimZanrom':ukupno})