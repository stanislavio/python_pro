

def outer():
    result = 0

    def inner(y):
        nonlocal result
        result = result + y
        return result

    return inner


func = outer()

print(func(12))
print(func(3))



def sum_closure():
    result = 0  # 5 8

    def inner_sum(y):
        nonlocal result
        result = result + y
        return result
    return inner_sum


func = sum_closure()
#print(func(5))
#print(func(3))
#print(func(10))


def make_average_closure():
    total = 0
    count = 0

    def calculate_average(num):
        nonlocal total
        nonlocal count
        total += num
        count += 1
        return total / count

    return calculate_average


def odd_number_generator():
    index = 1

    def inner():
        nonlocal index
        result = index
        index += 2
        return result
    return inner


odd_gen = odd_number_generator()
for i in range(5):
    print(odd_gen())
