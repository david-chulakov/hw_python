# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

def count_lines(file_name: str) -> int:
    """ Функия, считает кол-во строк в текстовом файле

    file_name: имя файла
    """

    counter = 0
    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{file_name}.txt", "r") as f_obj:
        while f_obj.readline() != "":
            counter += 1

    return counter


if __name__ == '__main__':
    my_file = "text_for_hw_2"
    print(count_lines(my_file))