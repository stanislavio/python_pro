

class A:

    def func(self):
        print('Hello from A')


class B(A):
    ...


class C:

    def func(self):
        print('Hello from C')


class D(B, C):
    ...


obj = D()
print(D.__mro__)
obj.func()
