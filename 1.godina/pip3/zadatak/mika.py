import json, csv
import os

if not os.path.exists('najbolji_studenti'):
    os.mkdir('najbolji_studenti')

def obradiFajl(json_path):
    najbolji_student = {}
    with open(json_path, newline='') as json_file:
        studenti = json.loads(json_file.read())['studenti']
        sorted_lista = sorted(studenti, key=lambda student: (sum(student['ocene'])/len(student['ocene'])), reverse=True)
        student = sorted_lista[0]
        najbolji_student['Ime i Prezime'] = student['ime'] + ' ' + student['prezime']
        najbolji_student['Indeks'] = str(student['indeks']) + '/' + str(student['godina'])
        najbolji_student['Prosek'] = sum(student['ocene'])/len(student['ocene'])
        najbolji_student['Grupa'] = os.path.basename(json_path)[:-5]
    return najbolji_student


csv_path = os.path.join('najbolji_studenti', 'mika.csv')
csv_file = open(csv_path, 'w', newline='')
header = ['Ime i Prezime', 'Indeks', 'Prosek', 'Grupa']
csv_writer = csv.DictWriter(csv_file, fieldnames=header)
csv_writer.writeheader()

file_path = os.path.join('spiskovi')
for _, _, files in os.walk(file_path):
    for file in files:
        if file.endswith('.json'):
            json_path = os.path.join(file_path, file)
            csv_writer.writerow(obradiFajl(json_path))
            