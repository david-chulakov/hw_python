# Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.


def new_list(some_list:list) -> list:
    """ Функция которая проходит список и оставляет только
    те элементы, которое больше предыдущего

    some_list: список элементов
    """
    result = []

    for i in range(len(some_list) - 1):
        if int(some_list[i]) < int(some_list[i+1]):
            result.append(int(some_list[i+1]))

    return result


if __name__ == "__main__":
    user_list = input("Вводите числа через пробел: ").split()
    print(new_list(user_list))