def factorial2(num):
    fact = 1
    if num == 0:
        fact = 1
    else:
        x = range(1, num+1)
        for n in x:
            fact = fact * n
    return fact


print(factorial2(-9))


# def factorial(number):
#     if number <= 0:
#         return 0
#
#     result = 1
#     for item in range(1, number + 1):
#         result *= item
#     return result
