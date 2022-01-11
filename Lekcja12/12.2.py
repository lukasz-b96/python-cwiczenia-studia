import unittest
import random


def binarne_rek(L, left, right, y):
    if right >= left:
        mid = left + (right - left) // 2
        if L[mid] == y:
            return mid
        elif L[mid] > y:
            return binarne_rek(L, left, mid - 1, y)
        else:
            return binarne_rek(L, mid + 1, right, y)

    else:
        return -1


class TestSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_100_10(self):
        n = 100
        k = 10
        data = sorted([random.randint(0, k) for i in range(n)])
        search = data[random.randint(0, n)]

    def test_1000_100(self):
        n = 1000
        k = 100
        data = sorted([random.randint(0, k) for i in range(n)])
        search = data[random.randint(0, n)]

    def test_100_1000(self):
        n = 100
        k = 1000
        data = sorted([random.randint(0, k) for i in range(n)])
        search = data[random.randint(0, n)]


if __name__ == "__main__":
    unittest.main()
