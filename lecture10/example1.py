
# Without Single responsibility principle
class Employee1:
    def calculate_pay(self):
        pass

    def save_to_database(self):
        pass


# With Single responsibility principle
class Employee:
    def calculate_pay(self):
        pass


class Database:
    def save_employee(self, employee):
        pass
