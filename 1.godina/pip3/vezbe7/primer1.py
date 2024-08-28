import os
import bs4

file_path = os.path.join('.', 'vezbe7', 'knjige.xml')
with open(file_path) as reader:
    xml_object = bs4.BeautifulSoup(reader.read(), features='html.parser')

knjige = xml_object.select('book')
knjige_recnik = {}

for knjiga in knjige:
    knjiga_id = knjiga.get('id')
    knjiga_naziv = knjiga.find('title').get_text().strip()
    knjiga_cena = float(knjiga.find('price').get_text().strip())
    knjige_recnik[knjiga_id] = {'naziv':knjiga_naziv, 'cena':knjiga_cena}

sorted_knjige = sorted(knjige_recnik.values(), key=lambda knjiga: knjiga['cena'], reverse=True)
najskuplja_knjiga = sorted_knjige[0]
print(najskuplja_knjiga['cena'], najskuplja_knjiga['naziv'])