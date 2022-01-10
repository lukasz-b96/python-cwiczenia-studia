# 12.1

import random
import unittest


def linear(n: int, k: int, list_to_search: list, number_to_find: int) -> int:
    amount = sum(1 for x in list_to_search if x == number_to_find)
    return amount


class TestSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_100_10(self):
        n = 100
        k = 10
        number_to_find = random.randint(0, k - 1)
        list_to_search = [random.randint(0, k - 1) for i in range(n)]
        self.assertEqual(
            linear(n, k, list_to_search, number_to_find),
            list_to_search.count(number_to_find),
        )

    def test_1000_100(self):
        n = 1000
        k = 100
        number_to_find = random.randint(0, k - 1)
        list_to_search = [random.randint(0, k - 1) for i in range(n)]
        self.assertEqual(
            linear(n, k, list_to_search, number_to_find),
            list_to_search.count(number_to_find),
        )

    def test_10_100(self):
        n = 10
        k = 100
        number_to_find = random.randint(0, k - 1)
        list_to_search = [random.randint(0, k - 1) for i in range(n)]
        self.assertEqual(
            linear(n, k, list_to_search, number_to_find),
            list_to_search.count(number_to_find),
        )

    def test_100_1000(self):
        n = 100
        k = 1000
        number_to_find = random.randint(0, k - 1)
        list_to_search = [random.randint(0, k - 1) for i in range(n)]
        self.assertEqual(
            linear(n, k, list_to_search, number_to_find),
            list_to_search.count(number_to_find),
        )

    def test_random(self):
        n = random.randint(0, 1000)
        k = random.randint(0, 1000)
        number_to_find = random.randint(0, k - 1)
        list_to_search = [random.randint(0, k - 1) for i in range(n)]
        self.assertEqual(
            linear(n, k, list_to_search, number_to_find),
            list_to_search.count(number_to_find),
        )


if __name__ == "__main__":
    unittest.main()
