import re
import os
import shutil
import send2trash
import zipfile
os.chdir('vezbe/vezbe4')

pattern = r'^[A-Z][^_]*\.[a-z]{3}$'
regex = re.compile(pattern)

if not os.path.isdir('dir2'):
    os.mkdir('dir2')

path = os.path.join('.', 'dir1')
for filename in os.listdir(path):
    if regex.search(filename):
        shutil.copy(os.path.join(path, filename), os.path.join('.', 'dir2'))

path = os.path.join('.', 'dir2')
zipovani_fajl = zipfile.ZipFile('dir2.zip', 'w')
for filename in os.listdir(path):
    zipovani_fajl.write(os.path.join(path, filename), filename, compress_type=zipfile.ZIP_DEFLATED)
zipovani_fajl.close()

for filename in os.listdir(path):
    fajl = os.path.join(path, filename)
    if os.path.getsize(fajl) > 100_000:
        os.remove(fajl)
    else:
        send2trash.send2trash(fajl)