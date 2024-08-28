import subprocess
import csv
import os
import time

def najboljiUFajlu(file_path):
    with open(file_path, newline='') as csv_file:
        studenti = csv.DictReader(csv_file)
        studenti_sorted = sorted(studenti, key=lambda student: float(student['Prosek']), reverse=True)
        najbolji_student = studenti_sorted[0]
    return najbolji_student

pera = subprocess.Popen(['python', 'pera.py'])
mika = subprocess.Popen(['python', 'mika.py'])

while pera.poll() == None or mika.poll() == None:
    time.sleep(1)

if pera.poll() != 0 or mika.poll() != 0:
    print("doslo je do greske")
    exit(0)

studenti = []
folder = 'najbolji_studenti'
for _, _, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(folder, file)
        studenti.append(najboljiUFajlu(file_path))

najbolji_student = sorted(studenti, key=lambda student: float(student['Prosek']), reverse=True)[0]
print(f'Najbolji student je {najbolji_student['Ime i Prezime']}, indeks: {najbolji_student['Indeks']} sa prosekom {najbolji_student['Prosek']}')