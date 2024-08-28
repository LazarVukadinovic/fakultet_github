import time, datetime

start_time = datetime.datetime(2024, 5, 22, 20, 34, 0)
while datetime.datetime.now() < start_time:
    time.sleep(1)

print("Program pokrenut")