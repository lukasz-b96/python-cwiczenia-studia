import random
import statistics as st
import unittest


def random_list(minimum: int, maximum: int, amount):
    data_list = [random.randint(minimum, maximum) for a in range(amount)]
    return data_list


def my_median(val):  # O(nlog(n))
    val.sort()
    mid = len(val) // 2
    res = (val[mid] + val[~mid]) / 2
    return res


def quickselect_median(l, piv=random.choice):  # O(n)
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, piv)
    else:
        return 0.5 * (
            quickselect(l, len(l) / 2 - 1, piv) + quickselect(l, len(l) / 2, piv)
        )


def quickselect(l, k, piv):  # O(n)
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = piv(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, piv)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), piv)


class TestSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_0(self):
        to_test = random_list(-100, 100, 100)
        self.assertEqual(my_median(to_test), st.median(to_test))

    def test_1(self):
        to_test = random_list(-1000, 1000, 1000)
        self.assertEqual(my_median(to_test), st.median(to_test))

    def test_2(self):
        to_test = random_list(-100, 100, 100)
        self.assertEqual(quickselect_median(to_test), st.median(to_test))

    def test_3(self):
        to_test = random_list(-1000, 1000, 1000)
        self.assertEqual(quickselect_median(to_test), st.median(to_test))


if __name__ == "__main__":
    unittest.main()
