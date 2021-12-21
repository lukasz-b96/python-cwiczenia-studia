import unittest


class Queue:
    def __init__(self, elems=None):
        if elems is None:
            elems = []
        self.items = elems

    def __str__(self):  # podglądanie kolejki
        return str(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def is_empty(self):
        return not self.items

    def is_full(self):  # nigdy nie jest pusta
        return False

    def put(self, data):
        if self.is_full():
            raise OverflowError("Brak miejsca w kolejce")
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise ValueError("Brak elementów w kolejce")
        return self.items.pop(0)  # mało wydajne!


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_str(self):
        self.assertEqual(str(self.queue), "[]")

    def test_eq(self):
        self.assertEqual(self.queue, Queue())

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.queue.is_full(), False)

    def test_pop(self):
        with self.assertRaises(ValueError):
            Queue().get()
        self.queue.put(22)
        self.assertEqual(self.queue.get(), 22)

    def test_push(self):
        self.queue.put(11)
        self.queue.put(22)
        self.queue.put(33)
        self.assertEqual(self.queue, Queue([11, 22, 33]))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
