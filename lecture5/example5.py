import collections

numbers = [1, 1, 1, 3, 4, 3, 3, 5, 4]

counter = collections.Counter(numbers)

print(counter)

print(counter[6])

print(counter.total())
