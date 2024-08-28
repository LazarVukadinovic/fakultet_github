import datetime

print(f"Danasnji datum je {datetime.datetime.now()}")
datum1 = datetime.datetime(2024, 5, 22, 20, 18, 0)
print(datum1.year)

datum2 = datetime.datetime.fromtimestamp(1800000000)
print(datum2)