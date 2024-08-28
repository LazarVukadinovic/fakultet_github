import datetime, time

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(f'Broj sekundi: {delta.total_seconds()}')

trenutno_vreme = datetime.datetime.now()
deset_data = datetime.timedelta(days=10)
novo_vreme = trenutno_vreme + deset_data
print(novo_vreme, '\n')

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)