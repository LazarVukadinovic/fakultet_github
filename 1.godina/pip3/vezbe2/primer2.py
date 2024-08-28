
a = map(int, input('Unesi elemente skupa 1: ').split())
b = map(int, input('Unesi elemente skupa 2: ').split())

a = set(a)
b = set(b)

print(a, b)

print('Presek: ', a & b) # a.intersection(b)
print('Unija: ', a | b) # a.union(b)
print('Razlika: ', a - b) # a.difference(b)
print('Simetricna razlika: ', a ^ b)