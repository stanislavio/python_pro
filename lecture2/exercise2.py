
a = int(input())  # 1
b = int(input())  # 1
c = int(input())  # 0

result = None

if a > b:
    result = a
else:
    result = b

if result < c:
    result = c

print(f'Max value = {result}')
