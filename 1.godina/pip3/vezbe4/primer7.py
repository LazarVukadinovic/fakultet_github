import os
os.chdir(os.path.join('.', 'vezbe', 'vezbe4'))

for putanjaFoldera, podFolderi, fajlovi in os.walk('.'):
    print('Folder: ', putanjaFoldera)
    print('Potfolder: ', podFolderi)
    print('Fajlovi: ', fajlovi)