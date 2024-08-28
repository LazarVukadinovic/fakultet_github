import os
import bs4

file_path = os.path.join('.', 'vezbe7', 'studenti.xml')
with open(file_path) as reader:
    xml_object = bs4.BeautifulSoup(reader.read(), features='html.parser')

studenti_dict = {}
studenti = xml_object.select('student')

for student in studenti:
    ime_prezime = student.find('ime').get_text() + ' ' + student.find('prezime').get_text()
    ocene = [int(o.get_text()) for o in student.find_all('ocena')]
    studenti_dict[ime_prezime] = studenti_dict.get(ime_prezime, []) + ocene

sortirani_studenti = sorted(studenti_dict.items(), key=lambda student: ( sum(student[1])/len(student[1]), student[0] ))

for student in sortirani_studenti:
    print(f'Student: {student[0]}, Prosek: {sum(student[1])/len(student[1])}')