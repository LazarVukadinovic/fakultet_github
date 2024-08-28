import re
import send2trash
import os
import shutil
import zipfile

if not os.path.isdir('transfers'):
    os.mkdir('transfers')

pattern = r'^\d{4}-\d{2}-\d{2}_[A-Za-z-_]{9,19}\.trans(fer)?$'
regex = re.compile(pattern)

for folderName, subFolders, files in os.walk('all_data'):
    for file in files:
        path = os.path.join('.', folderName, file)
        if regex.search(file):
            shutil.move(path, 'transfers')
        elif file.endswith('.xml'):
            send2trash.send2trash(path)
        else:
            os.remove(path)

igraci = {}
with open('players-teams.txt') as f:
    for line in f:
        id_igraca, id_tima = map(int, line.strip().split(','))
        igraci[id_igraca] = id_tima

#sorted(lista, key=lambda x: x.split('_')[0])
for file in sorted(os.listdir('transfers')):
    with open(os.path.join('.', 'transfers', file)) as f:
        for line in f:
            id_igraca, id_tima = map(int, line.strip().split(','))
            igraci[id_igraca] = id_tima

with open('player_teams_final.txt', 'w') as f:
    for key in igraci:
        f.write(f'{key},{igraci[key]}\n')

with zipfile.ZipFile('transfers.zip', 'w') as file_zip:
    for file in os.listdir('transfers'):
        path = os.path.join('.', 'transfers', file)
        file_zip.write(path, file, compress_type=zipfile.ZIP_DEFLATED)
    file_zip.write('player_teams_final.txt', compress_type=zipfile.ZIP_DEFLATED)
