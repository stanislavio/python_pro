import threading


def calculate_sublist_sum(sublist, result_lock):
    sub_sum = sum(sublist)
    with result_lock:
        results.append(sub_sum)


big_list = list(range(1, 10001))

num_threads = 4


sublist_size = len(big_list) // num_threads
sublists = [big_list[i:i + sublist_size] for i in range(0, len(big_list), sublist_size)]

results = []


result_lock = threading.Lock()


threads = []
for sublist in sublists:
    thread = threading.Thread(target=calculate_sublist_sum, args=(sublist, result_lock))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


total_sum = sum(results)

print("Загальна сума:", total_sum)
