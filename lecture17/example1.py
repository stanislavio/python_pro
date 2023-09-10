from multiprocessing import Process


def my_function():
    # Код, який буде виконуватися в новому процесі
    pass


if __name__ == "__main__":
    process = Process(target=my_function)
    process.start()
    process.join()

