import shutil, os
os.chdir(os.path.join('vezbe', 'vezbe4'))

path = os.path.join('.', 'primer1')
if not os.path.exists(path):
    os.mkdir(path)

path_original = os.path.join('.', 'original.txt')
path_to_copy = os.path.join(path, 'copy.txt')
shutil.copy(path_original, path_to_copy)