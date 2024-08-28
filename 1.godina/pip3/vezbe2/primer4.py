def decUHex(broj, hexDict):
    hex = []
    while broj>0:
        ostatak = broj % 16
        broj //= 16
        hex.insert(0, hexDict.get(ostatak))
    return ''.join(hex)

# recnik sa HEX ciframa
hexDict = {i: str(i) for i in range(16)}
hexDict.update({10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})

broj = int(input("Unesite broj: "))

print(decUHex(broj, hexDict))