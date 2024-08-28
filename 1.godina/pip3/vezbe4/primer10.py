import zipfile, os
os.chdir('vezbe/vezbe4')

zipovani_fajl = zipfile.ZipFile('fajl.zip', "w")
zipovani_fajl.write('data1.txt', compress_type=zipfile.ZIP_DEFLATED)
zipovani_fajl.write('data2.txt', compress_type=zipfile.ZIP_DEFLATED)
zipovani_fajl.close()

zipovani_fajl = zipfile.ZipFile('fajl.zip')
zipovani_fajl.extractall(os.path.join('.', 'output', 'folder'))

zipovani_fajl.extract('data2.txt', os.path.join('output', 'podaci'))
zipovani_fajl.close()
