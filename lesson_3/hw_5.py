res = 0
flag = True  # переменная для выхода из программы

def sum_of_list(list_num: list) -> int:
    """ Функия суммирует элементы списка

    list_num - список цифр
    """
    for num in list_num:

        if num.isdigit() == False:
            global flag
            flag = False  # Если в списке специальный символ то флажок становится False
            break
        else:
            global res
            res += int(num)

    return res


if __name__ == '__main__':
    while True:
        some_list = input("Вводите числа через пробел ").split()
        print(sum_of_list(some_list))
        if flag == False: # Выход из программы
            break