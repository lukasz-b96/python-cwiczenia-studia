import unittest


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):  # podglądamy stos
        return str(self.items)

    def is_empty(selfs):
        return not self.items

    def is_full(self):  # nigdy nie jest pełny
        return False

    def push(self, item):
        if self.is_full():
            raise OverflowError("Brak miejsca na stosie")
        self.items.append(item)  # dodajemy na koniec

    def pop(self):  # zwraca element
        if self.is_empty():
            raise ValueError("Brak elementów na stosie")
        return self.items.pop()  # zabieram od końca

    class TestStack(unittest.TestCase):
        def setUp(self):
            self.stack = Stack()

        def test_str(self):
            self.assertEqual(str(self.stack), "[]")

        def test_eq(self):
            self.assertEqual(self.stack, Stack())

        def test_is_empty(self):
            self.assertEqual(self.stack.is_empty(), True)

        def test_is_full(self):
            self.assertEqual(self.stack.is_full(), False)

        def test_pop(self):
            with self.assertRaises(ValueError):
                Stack().pop()
            self.stack.push(12)
            self.assertEqual(self.stack.pop(), 22)

        def test_push(self):
            self.stack.push(11)
            self.stack.push(22)
            self.stack.push(33)
            self.assertEqual(self.stack, Stack([11, 22, 33]))

        def tearDown(self):
            pass


if __name__ == "__main__":
    unittest.main()
