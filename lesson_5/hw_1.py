# Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

def create_file(name: str):
    """ Функция открывает его и записывает строки до пустой строки, если файла нет, то создаёт его

    name: имя файла
    """

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{name}.txt", "w+") as f_obj:
        while True:
            line = input()
            if line == "":
                break
            f_obj.write(line)

    return None


if __name__ == "__main__":
    name = input("Введите название файла")
    create_file(name)