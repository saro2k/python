#def add():
#    a = int(input("Enter the number:"))
#    b = int(input("enter the number:"))
#    return a + b

#print(add())


def add(a, b):
    return (a + b)


a = int(input("Enter the number:"))
b = int(input("enter the number:"))
print(add(a, b))
print(add(10, 10))


def addEm(x, y, z):
    print(x + y + z)


x, y, z = 1, 2, 3
print(addEm(x, y, z), end=" ")
