
class MyType:

    def __init__(self, some_list: list):
        self.some_list = some_list


def _print(
        value: str,
        times: int = 1,
        some_value: list[MyType | None] = None
) -> list[MyType | None]:

    for index in range(times):
        print(value)

    print(some_value)

    return some_value


_print('12', some_value=[MyType([1, 2, 3])])
