from abc import ABC, abstractmethod
from dataclasses import dataclass


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimiter(self):
        return 24


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length**2


# Не можна створити об'єкт абстрактного класу
# shape = Shape()
circle = Circle(5)
square = Square(4)

print(circle.area())
print(square.area())

print(circle.perimiter())


@dataclass
class BaseCar(ABC):

    wheels: int = None
    motor_v: float = None
    weight: float = None

    def get_wheels(self):
        return self.wheels

    @abstractmethod
    def get_speed(self):
        pass


class SportCar(BaseCar):

    def get_speed(self):
        return 100 * self.weight / self.motor_v


class SHCar(BaseCar):

    def get_speed(self):
        return 10 * self.weight / self.motor_v

    def get_wheels(self):
        return self.wheels * 2


class TrashCar(BaseCar):

    def get_speed(self):
        return 1 * self.weight / self.motor_v


def get_info(car: BaseCar):
    return {
        'wheels': car.wheels,
        'speed': car.get_speed()
    }


if __name__ == '__main__':

    lamborgini = SportCar(wheels=4, motor_v=5, weight=700)
    traktor = SHCar(wheels=8, motor_v=16, weight=5000)

    print(get_info(car=lamborgini))
    print(get_info(car=traktor))

    trash_car = TrashCar(wheels=4, motor_v=5, weight=700)
    print(get_info(trash_car))
