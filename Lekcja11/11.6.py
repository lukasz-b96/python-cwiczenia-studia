from m_11_1 import *

import unittest


def partition(numbers, start, end):
    mid = start + (end - start) // 2
    pivot = numbers[mid]

    while start <= end:
        while numbers[start] < pivot:
            start += 1
        while numbers[end] > pivot:
            end -= 1
        if start <= end:
            numbers[start], numbers[end] = numbers[end], numbers[start]
            start += 1
            end -= 1
    return start


def quick_sort(numbers):
    start = 0
    end = len(numbers) - 1
    stack = [start, end]

    while len(stack) > 0:
        end = stack.pop()
        start = stack.pop()

        pivot_index = partition(numbers, start, end)

        if pivot_index - 1 > start:
            stack.append(start)
            stack.append(pivot_index - 1)

        if pivot_index < end:
            stack.append(pivot_index)
            stack.append(end)
    return stack


class TestSort(unittest.TestCase):
    def setUp(self):
        self.max = 30

    def test_module_a(self):
        numbers = module_a(self.max)
        to_test = numbers.copy()
        quick_sort(numbers)
        self.assertEqual(numbers, sorted(to_test))

    def test_module_b(self):
        numbers = module_b(self.max)
        to_test = numbers.copy()
        quick_sort(numbers)
        self.assertEqual(numbers, sorted(to_test))

    def test_module_c(self):
        numbers = module_c(self.max)
        to_test = numbers.copy()
        quick_sort(numbers)
        self.assertEqual(numbers, sorted(to_test))

    def test_module_d(self):
        numbers = module_d(self.max)
        to_test = numbers.copy()
        quick_sort(numbers)
        self.assertEqual(numbers, sorted(to_test))

    def test_module_e(self):
        numbers = module_e(self.max)
        to_test = numbers.copy()
        quick_sort(numbers)
        self.assertEqual(numbers, sorted(to_test))


if __name__ == "__main__":

    unittest.main()
