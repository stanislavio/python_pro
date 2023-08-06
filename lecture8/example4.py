
a = []


def func(l=[]):  # s21378921dw
    print(id(l))
    l.append(1)
    return l


print(func())
print(func())
print(func())
print(func())
print(func())
