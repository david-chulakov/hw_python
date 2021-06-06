# Реализовать формирование списка, используя функцию range() и возможности
# генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce
from operator import mul  # оператор умножения


def some_maths(some_list: list) -> int:
    """ Функция, считающая произведение всех элемeнтов списка

    some_list: список чисел
    """

    return reduce(mul, some_list)


if __name__ == "__main__":
    my_list = [num for num in range(100, 1001) if num % 2 == 0]
    print(some_maths(my_list))

