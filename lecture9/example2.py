
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print('Method New')
        print(cls._instance)
        print(id(cls._instance))
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print('Method New')
            print(cls._instance)
            print(id(cls._instance))
            print('---------------------')
        return cls._instance


obj1 = Singleton('host', 'database', 'user', 'password')
obj2 = Singleton()

print(f'These objs is similar = {obj1 is obj2}')


class S:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super.__new__(cls)

        return cls.__instance



obj1 = S()
obj2 = S()

print(f'These objs is similar = {obj1 is obj2}')