import os
os.chdir('vezbe/vezbe3')

if(not os.path.isdir('kopije')):
    os.mkdir('kopije')

for file in os.listdir('.'):
    if(os.path.isfile(file)):
        #cita text iz fajla
        file_read = open(file, 'r')
        text = file_read.read()
        file_read.close()

        file_write = open(os.path.join('kopije', file), 'w')
        file_write.write(text)
        file_write.close()