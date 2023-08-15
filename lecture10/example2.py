from abc import abstractmethod, ABC


class Rectangle1:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator1:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width * shape.height
            # Якщо з'явиться новий тип фігури, код потрібно буде модифікувати.


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()

