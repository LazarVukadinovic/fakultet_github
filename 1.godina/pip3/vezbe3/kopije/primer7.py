import os

os.chdir('vezbe/vezbe3')    #za startni direktorijum

total_size = 0
for filename in os.listdir('.'):
    total_size += os.path.getsize(os.path.join('.', filename))

print(total_size)