# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
# словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

def filtr(some_string: str) -> int:
    """ Функция удаляет скобки и оставляет кол-во занятий

    :param some_string: кол-во занятий и обозначение(лек, сем, лаб)
    :return: кол-во занятий
    """
    return int(re.sub("[(\D)]", "", some_string))


def file_to_dict(file_name: str) -> dict:
    """ Функия, считывает файл и возвращает словарь

    :param file_name: название файла(без расширения)
    :return: словарь, с названием предметов и кол-вом занятий
    """
    result = {}

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{file_name}.txt", "r",
              encoding="utf8") as f_obj:
        for line in f_obj.readlines():
            summary = 0
            temp_list = line.split(":")  # делим на две части, чтобы взять название предмета
            num_of_lessons = temp_list[1].split(',')  # делим на кол-во занятий
            for lesson in num_of_lessons:
                summary += filtr(lesson)
            result.update({temp_list[0]: summary})

    return result


if __name__ == "__main__":
    print(file_to_dict("text_for_hw_6"))