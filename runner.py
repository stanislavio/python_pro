
# Секція для вбудованих пакетів
import math

# Секція для інстальованих пакетів
import pandas as pd

# Секція для локальних пакетів
from utils.helper import add, minus


a = int(input('Input a: '))

b = int(input('Input b: '))


print(math.pow(a, b))
print(add(a, b))
print(minus(a, b))

# print(minus(a, b))

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])

print(df[2][0])


def calculate():

    return 0
