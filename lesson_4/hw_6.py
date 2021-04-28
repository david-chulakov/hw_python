# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle


def iterator_1(start_num: int):
    """ Итератор, генерирующий числа начиная с указанного

    start_num: число, с которого начнется генерация чисел
    """

    for num in count(start_num):
        print(num)
        if num >= 20:  # Чтобы цикл не был бесконечным (выход из цикла)
            break

    return None


def iterator_2(some_list: list):
    """ Итератор, повторяющий элементы некоторого списка, определенного заранее

    some_list: список элементов
    """
    counter = 0  # Использую счётчик для выхода из цикла
    for num in cycle(some_list):
        if counter >= 20:
            break
        print(num)
        counter += 1

    return None


if __name__ == "__main__":
    start = int(input("Введите число, с которого начнет первый итератор: "))
    iterator_1(start)
    user_list = input("Вводите элементы через пробел ").split()
    iterator_2(user_list)

