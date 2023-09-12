class GraphicComponent:
    def draw(self):
        pass


class Line(GraphicComponent):
    def draw(self):
        print("Drawing a line")


class Rectangle(GraphicComponent):
    def draw(self):
        print("Drawing a rectangle")


class Group(GraphicComponent):
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def draw(self):
        print("Drawing a group:")
        for component in self.components:
            component.draw()


line1 = Line()
line2 = Line()
rectangle = Rectangle()

group = Group()
group.add(line1)
group.add(line2)
group.add(rectangle)

group.draw()
