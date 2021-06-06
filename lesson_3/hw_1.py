def division(arg_one: int, arg_two: int) -> str:
    """Функция деления первого числа на второе

    arg_one : Первое число(числитель)
    arg_two : Второе число(знаменатель)
    """

    try:
        result = arg_one / arg_two
    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return result


if __name__ == "__main__":
    arg_one = int(input("Введите целый числитель "))
    arg_two = int(input("Введите целый знаменатель "))

    print(division(arg_one, arg_two))
