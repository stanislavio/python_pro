from abc import ABC, abstractmethod


class Bird:
    def fly(self):
        pass


class Ostrich1(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")


def make_bird_fly1(bird):
    bird.fly()  # Ostrich викине Exception


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass


class Ostrich(Bird):
    def fly(self):
        return False


def make_bird_fly(bird):
    if bird.fly():
        print("Flying")
    else:
        print("Can't fly")