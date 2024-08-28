import os
import bs4

file_path = os.path.join('.', 'vezbe7', 'knjige.xml')
with open(file_path) as reader:
    xml_object = bs4.BeautifulSoup(reader.read(), features='html.parser')

autor_recnik = {}
knjige = xml_object.select('book')

for knjiga in knjige:
    knjiga_autor = knjiga.find('author').get_text().strip()
    knjiga_naziv = knjiga.find('title').get_text().strip()

    autor_recnik[knjiga_autor] = autor_recnik.get(knjiga_autor, set([])) | set([knjiga_naziv])

for autor, knjige in autor_recnik.items():
    print(f'Autor: {autor} => Broj knjiga: {len(knjige)}')