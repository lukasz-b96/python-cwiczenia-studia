import random


class RandomQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        if self.is_full():
            raise OverflowError("Brak miejsca w kolejce")
        self.items.append(item)

    def remove(self):  # zwraca losowy element"""
        if self.is_empty():
            raise ValueError("Brak elementów w kolejce")
        number = random.randint(0, len(self.items) - 1)
        self.items[number], self.items[-1] = self.items[-1], self.items[number]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):  # czyszczenie listy
        self.items = []
