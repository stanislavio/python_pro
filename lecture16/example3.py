import threading
import math


def calculate_square_root(number, results):
    result = math.sqrt(number)
    results.append((number, result))


numbers = [16, 25, 36, 49, 64, 81]

results = []

threads = []

for num in numbers:
    thread = threading.Thread(target=calculate_square_root, args=(num, results))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

for number, result in results:
    print(f"Квадратний корінь з {number} = {result}")


print("Усі потоки завершили роботу")
