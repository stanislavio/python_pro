from multiprocessing import Pool


def my_function(x):
    return x * x


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        result = pool.map(my_function, [1, 2, 3, 4])
    print(result)
