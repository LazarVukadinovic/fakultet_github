import shutil, os, send2trash
os.chdir(os.path.join('vezbe', 'vezbe4'))

file = open('recycle_bin.txt', 'w')
file.close()

for filename in os.listdir():
    if filename.endswith('.txt'):
        send2trash.send2trash(filename)