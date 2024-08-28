import shutil, os
os.chdir(os.path.join('vezbe', 'vezbe4'))

path_move = os.path.join('.', 'premesti')
if not os.path.exists(path_move):
    os.mkdir(path_move)

path_org = os.path.join('.', 'original.txt')
shutil.move(path_org, path_move)