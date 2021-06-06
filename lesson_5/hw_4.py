# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок
# строк должен записываться в новый текстовый файл.

def little_translator(file_name: str):
    """

    :param file_name: название файла без расширения
    :return: создает другой файл, с переводом
    """


    data = {
        "One": 'один',
        "Two": 'два',
        "Three": 'три',
        "Four": 'четыре'
    }

    temp_list = []
    result = ''

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{file_name}.txt", 'r', encoding='utf8') as f_obj:
        for line in f_obj.readlines():
            temp_list = line.split()
            result += data[temp_list[0]] + ' - ' + temp_list[2] + '\n'

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\result_hw_4.txt", "w") as w_obj:
        w_obj.write(result)

    return None


if __name__ == "__main__":
    little_translator("text_for_hw_4")