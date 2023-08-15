from abc import abstractmethod, ABC


class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class SuperWorker(Worker):
    def work(self):
        pass

    def eat(self):
        pass

class Manager:
    def manage(self, worker):
        worker.work()
        worker.eat()


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        pass

    def eat(self):
        pass

class SuperWorker(Workable):
    def work(self):
        pass

class Manager:
    def manage(self, worker):
        worker.work()

