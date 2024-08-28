import os

putanja = os.path.join('usr', 'bin', 'spam')  #kreira putanju
print(putanja)

cwd = os.getcwd()   #vraca putanju trenutnog direktorijuma
print(cwd)

os.chdir('../')     #promeni trenutni radni direktorijum
print(os.getcwd())

#os.makedirs('kreiraj/direktorijum')     #kreira direktorijume da bi putanja postojala

abs_path = os.path.abspath('.')    #vraca apsolutnu putanju trenutnog direktorijuma
print(abs_path)

rel_path = os.path.relpath('.', '../../')   #vraca relativnu putanju (path, start)
print(rel_path)

size = os.path.getsize('pip3/vezbe/vezbe3/primer1.py')  #vraca velicinu fajla
print(size)

dirs = os.listdir('.')  #vraca listu direktorijuma
print(dirs)

is_file = os.path.isfile('pip3')    #vraca True ako je argument fajl
print(is_file)

is_dir = os.path.isdir('pip3')      #vraca True ako je argument folder
print(is_dir)

file = open('fajl.txt', 'w')
file.write("Pozdrav svete!")
file.close()

file = open('fajl.txt', 'r')
#text = file.read()              #vraca jedan string
text_lista = file.readlines()   #vraca listu stringova
#print(text)
print(text_lista)
file.close()