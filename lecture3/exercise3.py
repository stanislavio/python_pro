
numbers = list(map(lambda x: int(x.strip()), input().split(',')))

print(numbers)

avg_lambda = lambda args: sum(args) / len(args)


def avg(args):
    return sum(args) / len(args)

print(avg(numbers))
