import concurrent.futures
import time


def some_task(parameter):
    result = parameter * 2
    print(result)
    time.sleep(1)
    return result


# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     parameters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     futures = [executor.submit(some_task, param) for param in parameters]
#
#     results = [future.result() for future in futures]
#
# print("Результати:", results)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

threads = 4

size = len(a) // threads

sublists = [a[i:i + size] for i in range(0, len(a), size)]

print(sublists)
