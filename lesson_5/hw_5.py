# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

def create_file(name: str, numbers: list):
    """ Функция создает или открывает файл и записывает в него числа через пробел

    :param name: Название файла
    :param numbers: список чисел
    :return: None
    """

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{name}.txt", "w",
              encoding="utf8") as f_obj:
        for num in numbers:
            f_obj.write(num + ' ')

    return None

def read_and_sum(name: str) -> int:
    """ Функция читает и возвращает сумму чисел в файле

    :param name: название файла
    :return: сумма чисел записанных через пробел в файле
    """
    sum = 0
    file_str = ''
    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{name}.txt", "r",
              encoding="utf8") as f_obj:
        for line in f_obj.readlines():
            file_str += line

        for num in file_str.split():
            sum += int(num)

    return sum


if __name__ == "__main__":
    file_name = input("Введите название файла(без расширения): ")
    user_numbers = input("Введите числа через пробел: ").split()
    create_file(file_name, user_numbers)
    print("Сумма чисел:", read_and_sum(file_name))