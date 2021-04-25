def sum_of_2_max_elements(arg_one, arg_two, arg_three):
    """ Функция суммирования двух наибольших элементов из 3 чисел

    arg_one - число
    arg_two - число
    arg_three - число
    """

    if arg_one >= arg_two >= arg_three or arg_two >= arg_one >= arg_three:
        return arg_one + arg_two
    elif arg_one >= arg_three >= arg_two or arg_three >= arg_one >= arg_two:
        return arg_one + arg_three
    elif arg_two >= arg_three >= arg_one or arg_three >= arg_two >= arg_one:
        return arg_two + arg_three


if __name__ == '__main__':
    arg_1 = float(input("Введите первый элемент "))
    arg_2 = float(input("Введите второй элемент "))
    arg_3 = float(input("Введите третий элемент "))
    print(sum_of_2_max_elements(arg_1, arg_2, arg_3))