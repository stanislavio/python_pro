

class Vehicle(object):

    def __init__(self, weight, color, places):
        self.weight = weight
        self.color = color
        self.places = places

    def info(self):
        return {
            'weight': self.weight,
            'color': self.color,
            'places': self.places
        }


class Car(Vehicle):

    def __init__(self, *args, marka, year):
        super().__init__(*args)
        self.marka = marka
        self.year = year
        self.__price = None
        self.__win = None

    def __hash__(self):
        return

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, win):
        self.__win = win

    def set_win(self, win):
        self.__win = win

    def info(self):
        result = super().info()
        result.update({
            'marka': self.marka,
            'year': self.year,
            'price': self.__price,
            'win': self.__win
        })
        return result

    def __str__(self):
        return f'Car({self.marka}, {self.year})'

    def __call__(self, *args, **kwargs):
        ...

    def __add__(self, other):
        if isinstance(other, Car):
            return Car(
                self.weight + other.weight,
                f'{self.color} + {other.color}',
                self.places + other.places,
                marka=f'{self.marka} + {other.marka}',
                year=self.year + other.year
            )
        raise Exception('Unsupported additional operation!')


bmw = Car(1500, 'red', 4, marka='BMW', year=2020)
mercedes = Car(1700, 'yellow', 5, marka='Mercedes', year=2021)

new_car = bmw + mercedes

print(new_car)
print(new_car.info())

print(bmw.__dict__)


def func():
    return 'Hello'
