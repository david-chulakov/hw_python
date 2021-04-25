# Первый способ
def x_elevate_to_degree_y_1(arg_1: int, arg_2: int) -> float:
    """ Функция возведения числа x в степень y

    arg_1: Положительное целое число
    arg_2: Отрицательное целое число
    """

    return arg_1 ** arg_2


# Второй способ
def x_elevate_to_degree_y_2(arg_1: int, arg_2: int) -> float:
    """ Функция возведения числа x в степень y

    arg_1: Положительное целое число
    arg_2: Отрицательное целое число
    """
    if arg_1 == 0:
        return 0

    if arg_2 < 0:
        arg_1 = 1 / arg_1
        arg_2 = - arg_2

    res = 1

    while arg_2 > 0:
        res = res * arg_1
        arg_2 -= 1

    return round(res, 2)


if __name__ == '__main__':
    arg_one = int(input("Введите положительное целое число "))
    arg_two = int(input("Введите отрицательное целое число "))
    print("Первым способом")
    print(x_elevate_to_degree_y_1(arg_one, arg_two))
    print("Вторым способом")
    print(x_elevate_to_degree_y_2(arg_one, arg_two))