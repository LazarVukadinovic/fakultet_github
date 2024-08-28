import shutil, os
os.chdir(os.path.join('vezbe', 'vezbe4'))

path_file = os.path.join('.', 'primer1')
shutil.rmtree(path_file)        #brise sve iz foldera i njega
os.rmdir(path_file)             #ako je folder prazan brise ga
os.unlink(path_file)