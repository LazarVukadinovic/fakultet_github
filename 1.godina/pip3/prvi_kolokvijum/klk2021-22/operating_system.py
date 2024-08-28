import re
import os
import shutil
import send2trash
import zipfile

# pattern = r'^[A-Z0-9][a-z@#$_]+\.core_dump'
pattern = r'^(\d|[A-Z]){1}[a-z@#$_]*\.core_dump$'
regex = re.compile(pattern)

if not os.path.isdir('core_dump_folder'):
    os.mkdir('core_dump_folder')

for folderName, subFolders, files in os.walk('operating_system_logs'):
    for file in files:
        path = os.path.join('.', folderName, file)
        matched = regex.search(file)
        if matched and 15 <= len(matched.group(0)) <= 30:
            shutil.move(path, 'core_dump_folder')
        else:
            os.remove(path)

with zipfile.ZipFile('core_dump.zip', 'w') as zip_file:
    for file in os.listdir('core_dump_folder'):
        path = os.path.join('.', 'core_dump_folder', file)
        zip_file.write(path, file, compress_type=zipfile.ZIP_DEFLATED)

for file in os.listdir('core_dump_folder'):
    path = os.path.join('.', 'core_dump_folder', file)
    send2trash.send2trash(path)

hard_disk = {}
lista_fajlova = []
for file in os.listdir('file_system'):
    path = os.path.join('.', 'file_system', file)
    if path.endswith('.txt'):
        with open(path, 'r') as f:
            for line in f:
                nazivFajla, idFizickogDiska, velicinaFajla = line.split(',')
                hard_disk[idFizickogDiska] = hard_disk.get(idFizickogDiska, 0) + int(velicinaFajla)
                lista_fajlova.append(nazivFajla)

with open('disk_usage.txt', 'w') as f:
    for key, data in hard_disk.items():
        f.write(f'{key},{data}\n')

with open('files.txt', 'w') as f:
    for file in lista_fajlova:
        f.write(f'{file}\n')
