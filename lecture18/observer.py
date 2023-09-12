class Observer:
    def update(self, temperature, humidity, pressure):
        pass


class WeatherData:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}°C and {self.humidity}% humidity")


weather_data = WeatherData()

current_display = CurrentConditionsDisplay()
weather_data.register_observer(current_display)

weather_data.set_measurements(25, 65, 1013)
weather_data.set_measurements(25, 65, 1013)
weather_data.set_measurements(25, 65, 1013)
