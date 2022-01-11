import random


def module_a(maximum: int) -> list:
    data_list = [a for a in range(maximum)]
    random.shuffle(data_list)
    return data_list


def module_b(maximum: int) -> list:
    data_list = [a for a in range(maximum)]
    for i in range(1, maximum):
        j = random.randint(i - 1, i)
        data_list[i], data_list[j] = data_list[j], data_list[i]
    return data_list


def module_c(maximum: int) -> list:
    data_list = module_b(maximum)
    data_list.reverse()
    return data_list


def module_d(maximum: int) -> list:
    data_list = []
    for i in range(maximum):
        data_list.append(random.gauss(0, 1))
    return data_list


def module_e(maximum: int) -> list:
    data_list = []
    for i in range(maximum):
        data_list.append(random.randint(0, maximum // 2))
    random.shuffle(data_list)
    return data_list


"""
number = 15
for a in [module_a, module_b, module_c, module_d, module_e]:
    print(a(number))
"""
