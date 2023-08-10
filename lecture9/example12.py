def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(5):
    print(i)
# Output:
# 5
# 4
# 3
# 2
# 1

gen = countdown(5)

print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

numbers = list(gen)
print(numbers)