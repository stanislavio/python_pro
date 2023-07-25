import csv

with open('example.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        print(row)

import pandas as pd

data = pd.read_csv('example.csv', delimiter='/')
print(data)

try:
    file = open('example.csv', 'w')
    ...
except FileExistsError:
    raise FileExistsError
except FileNotFoundError:
    raise FileNotFoundError
finally:
    file.close()