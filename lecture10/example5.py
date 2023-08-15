from abc import abstractmethod, ABC


class LightBulb1:

    is_on: bool = False

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Switch1:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        if self.bulb.is_on:
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()


class Switchable(ABC):

    is_on: bool = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()
