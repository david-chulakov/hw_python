# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

def file_to_json(file_name: str):
    """ Функция считывает файл и создает или записывает в json файл

    :param file_name: название файла без расширения
    :return: создает json файл
    """

    profit_dict = {}
    damages_dict = {}
    all_profits = 0
    average_dict = {}

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\{file_name}.txt", "r",
              encoding="utf8") as f_obj:
        counter = 0
        for line in f_obj.readlines():
            temp_line = line.split()
            money = int(temp_line[2]) - int(temp_line[3])
            if money > 0:
                profit_dict.update({temp_line[0]: money})
                all_profits += money
                counter += 1
            else:
                damages_dict.update({temp_line[0]: -money})

        average_dict.update({"average_profit": all_profits / counter})

    result_list = [profit_dict, damages_dict, average_dict]

    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\result_hw_7.json", "w") as w_obj:
        json.dump(result_list, w_obj)

    return None


if __name__ == "__main__":
    file_to_json("text_for_hw_7")
