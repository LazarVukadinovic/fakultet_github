import json, csv
import os

folder = 'podaci'
end_folder = 'files'
extension = '.json'

# obradjivanje fajlova
def obradiArtiste(folder, extension):
    artists_dict = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(path, file)

                with open(file_path, newline='') as json_file:
                    json_data = json.loads(json_file.read())
                
                for obj in json_data:
                    for artist in obj['artists']:
                        artist = artist.lower().strip()
                        artist_from_dict = artists_dict.get(artist, {})
                        ZbirnaPopularnost = float(artist_from_dict.get('ZbirnaPopularnost', 0)) + float(obj['popularity'])
                        BrojPesama = int(artist_from_dict.get('BrojPesama', 0)) + 1

                        artist_from_dict['ZbirnaPopularnost'] = str(ZbirnaPopularnost)
                        artist_from_dict['BrojPesama'] = str(BrojPesama)
                        artists_dict[artist] = artist_from_dict
    return artists_dict

def obradiZanrove(folder, extension):
    godine_dict = {}
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(path, file)

                with open(file_path, newline='') as json_file:
                    json_data = json.loads(json_file.read())
                
                for obj in json_data:
                    year = int(obj['year'])
                    year_from_dict = godine_dict.get(year, {})
                    for genre in obj['genres']:
                        genre = genre['name']
                        year_from_dict[genre] = int(year_from_dict.get(genre, 0)) + 1
                        godine_dict[year] = year_from_dict
    return godine_dict

# upisivanje u csv fajl
csv_path = os.path.join(end_folder, 'material-authors.csv')
with open(csv_path, 'w', newline='') as csv_file:
    header = ['ImeAutora', 'ZbirnaPopularnost', 'BrojPesama']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()
    for key, artist_dict in obradiArtiste(folder, extension).items():
        artist_dict['ImeAutora'] = key
        csv_writer.writerow(artist_dict)

csv_path = os.path.join(end_folder, 'material-genres.csv')
with open(csv_path, 'w', newline='') as csv_file:
    header = ['Godina', 'Zanr', 'BrojPesama']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()
    for godina, genres_dict in obradiZanrove(folder, extension).items():
        for genre, num in genres_dict.items():
            tmp_dict = {'Godina':godina, 'Zanr': genre, 'BrojPesama':num}
            csv_writer.writerow(tmp_dict)