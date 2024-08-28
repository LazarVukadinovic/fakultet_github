import shutil, os
os.chdir(os.path.join('vezbe', 'vezbe4'))

for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
