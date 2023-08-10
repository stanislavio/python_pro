from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield
    finally:
        print("Exiting the context")


with my_context_manager():
    print("Doing something inside the context")
# Виведе:
# Entering the context
# Doing something inside the context
# Exiting the context
