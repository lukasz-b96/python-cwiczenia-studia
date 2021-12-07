import random
import math


def calc_pi(n=100):

    circle = 0


    for i in range(0, n):
        x2 = random.uniform(-1, 1)
        y2 = random.uniform(-1, 1)
        if math.sqrt(x2 ** 2 + y2 ** 2) < 1.0:
            circle += 1

    pi = (float(circle) / n) * 4
    return pi

print(calc_pi())