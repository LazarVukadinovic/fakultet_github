import bs4, csv
import os

if not os.path.exists('najbolji_studenti'):
    os.mkdir('najbolji_studenti')

def obradiFajl(xml_path):
    with open(xml_path, newline='') as xml_file:
        soup = bs4.BeautifulSoup(xml_file, features='html.parser')

    studenti = soup.select('student')
    studenti_list = []
    
    for student in studenti:
        ocene = [int(ocena.get_text()) for ocena in student.select('ocena')]
        prosek = sum(ocene)/len(ocene)
        puno_ime = student.find('ime').get_text() + ' ' + student.find('prezime').get_text()
        indeks = student.get('indeks') + ' ' + student.get('godina')
        
        student_dict = {}
        student_dict['Ime i Prezime'] = puno_ime
        student_dict['Indeks'] = indeks
        student_dict['Prosek'] = prosek
        student_dict['Grupa'] = os.path.basename(xml_path)[:-4]

        studenti_list.append(student_dict)
    
    najbolji_student = sorted(studenti_list, key=lambda student: student['Prosek'], reverse=True)[0]
    return najbolji_student


csv_path = os.path.join('najbolji_studenti', 'pera.csv')
csv_file = open(csv_path, 'w', newline='')
header = ['Ime i Prezime', 'Indeks', 'Prosek', 'Grupa']
csv_writer = csv.DictWriter(csv_file, fieldnames=header)
csv_writer.writeheader()

file_path = os.path.join('spiskovi')
for _, _, files in os.walk(file_path):
    for file in files:
        if file.endswith('.xml'):
            xml_path = os.path.join(file_path, file)
            csv_writer.writerow(obradiFajl(xml_path))
            