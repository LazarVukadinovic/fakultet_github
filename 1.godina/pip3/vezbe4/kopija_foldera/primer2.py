import shutil, os
os.chdir(os.path.join('vezbe', 'vezbe4'))

path_copies = os.path.join('.', 'kopija_foldera')
path_to_copy = os.path.join('.')

shutil.copytree(path_to_copy, path_copies)