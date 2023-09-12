# Клас продукту, який ми будуємо
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"


# Абстрактний будівельник
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        pass

    def build_ram(self):
        pass

    def build_storage(self):
        pass

    def get_computer(self):
        return self.computer


# Конкретний будівельник для геймерського ПК
class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i7"

    def build_ram(self):
        self.computer.ram = "16GB DDR4"

    def build_storage(self):
        self.computer.storage = "1TB SSD"


# Конкретний будівельник для офісного ПК
class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5"

    def build_ram(self):
        self.computer.ram = "8GB DDR4"

    def build_storage(self):
        self.computer.storage = "512GB SSD"


# Директор, який відповідає за конструювання комп'ютера
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()


# Використання
gaming_builder = GamingComputerBuilder()
office_builder = OfficeComputerBuilder()

gaming_director = Director(gaming_builder)
office_director = Director(office_builder)

gaming_director.construct_computer()
office_director.construct_computer()

gaming_computer = gaming_builder.get_computer()
office_computer = office_builder.get_computer()

print("Gaming Computer:", gaming_computer)
print("Office Computer:", office_computer)
