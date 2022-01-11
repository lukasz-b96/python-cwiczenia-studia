import random
import unittest
import numpy as np


def linear(n: int, k: int, list_to_search: list, number_to_find: int) -> int:
    indexs = [indx for indx, x in enumerate(
        list_to_search) if x == number_to_find]
    return indexs


class TestSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_100_10(self):
        n = 100
        k = 10
        number_to_find = random.randint(0, k - 1)
        list_to_search = [random.randint(0, k - 1) for i in range(n)]
        self.assertEqual(
            (linear(n, k, list_to_search, number_to_find)),
            list(np.where(np.array(list_to_search) == number_to_find)[0])
        )

        def test_1000_100(self):
            n = 1000
            k = 100
            number_to_find = random.randint(0, k - 1)
            list_to_search = [random.randint(0, k - 1) for i in range(n)]
            self.assertEqual(
                (linear(n, k, list_to_search, number_to_find)),
                list(np.where(np.array(list_to_search) == number_to_find)[0])
            )


if __name__ == "__main__":
    unittest.main()
