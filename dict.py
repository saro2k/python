D = {0: 'saravanan', 1: "saro"}
for i in D:
    print(i, D[i])
#dict not a order
D[2] = 'hello'
print(D)
del D[2]
print(D)
E = {3: 'help', 4: 'rain'}
D.update(E)
print(D)
print(D.keys())
print(D.values())
print(D.items())
print('saro' in D.values())

dict1 = {1: 'one', 2: 'two'}
Lst = list(dict1)
print(Lst)