tup = (1, 2, 3)
print(len(tup))
print(max(tup))
print(min(tup))
tup = tuple([1, 2, 3, 4])
print(tup)
for i in tup:
    print(i)
#tuple is a immutable

Tup = (10, 60)
print(max(Tup))
Tup.append([70])
print(Tup)