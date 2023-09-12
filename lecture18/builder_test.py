

class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"

    def add_cpu(self, data: str):
        self.cpu = data
        return self

    def add_ram(self, data):
        self.ram = data
        return self

    def add_storage(self, data):
        self.storage = data
        return self


# computer = Computer()
#
# computer = computer.add_ram('1sdbf').add_storage('badsjfjadl').add_cpu('dsblfjds')
#
# print(computer)

computer1 = Computer()

computer1.add_cpu('dfndp').add_storage('badsjfjadl').add_ram('dsblfjds')

print(computer1)
