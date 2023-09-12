class SortStrategy:
    def sort(self, data):
        pass


class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)


class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data, reverse=True)


class SortContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def perform_sort(self, data):
        return self.strategy.sort(data)


data = [5, 1, 3, 7, 2, 8, 4, 6]

bubble_sort = BubbleSort()
context = SortContext(bubble_sort)
result = context.perform_sort(data)
print("Result:", result)

quick_sort = QuickSort()
context.set_strategy(quick_sort)
result = context.perform_sort(data)
print("Result:", result)
