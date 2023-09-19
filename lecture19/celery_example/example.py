from random import randint

from tasks import add

for i in range(10):
    result = add.delay(randint(1, 100) * i, randint(1, 100) * i)
    print(result.get())
