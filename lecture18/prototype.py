import copy


class Order:
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"Order: {', '.join(self.items)}"

    def clone(self):
        return copy.deepcopy(self)


# Створюємо початкове замовлення
initial_order = Order(["Pizza", "Burger", "Fries"])
print(initial_order)


# Клієнт хоче повторити замовлення
new_order = initial_order.clone()
new_order.add_item("Cola")
print(new_order)

# Клієнт хоче ще одну копію замовлення, але без піци
order_without_pizza = initial_order.clone()
order_without_pizza.remove_item("Pizza")
print(order_without_pizza)

