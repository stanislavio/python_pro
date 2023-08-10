from contextlib import contextmanager


class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

    def do_something(self):
        print("Doing something inside the context")


# with MyContextManager() as cm:
#     cm.do_something()
# Output:
# Entering the context
# Doing something inside the context
# Exiting the context


class FileReader:

    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        print('Enter method')
        self.file = open(self.filename, 'r')
        print(self.filename, self.file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        self.file.close()

    def get_file_body(self):
        raise Exception('File does not exist')
        return self.file.read()


# with FileReader('example.txt') as reader:
#     print(reader.get_file_body())
#
# print('Exit was done')


@contextmanager
def file_reader(filename: str):
    print('Entering')
    file = None
    try:
        file = open(filename, 'r')
        yield file
    except Exception as err:
        print(err)
        if file:
            file.close()


with file_reader('example2234.txt') as file:
    print(file.read())
