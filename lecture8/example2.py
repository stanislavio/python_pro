
from dataclasses import dataclass


class SquareWithoutDataclass:

    def __init__(self, position: tuple[int, int], color: str = 'red'):
        self.position = position
        self.color = color


@dataclass
class Square:

    position: tuple[int, int]
    color: str = 'red'


s = Square(position=(1, 1))
s1 = Square(position=(1, 1))

sw = SquareWithoutDataclass(position=(1, 1))
sw1 = SquareWithoutDataclass(position=(1, 1))

print(s == s1)
print(sw == sw1)
