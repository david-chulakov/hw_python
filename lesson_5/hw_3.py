# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.

def some_func():
    """ Функция выводит фамилии тех, у кого оклад меньше 20000, и считает средний оклад
    """
    counter = 0
    salary = 0
    with open(fr"C:\Users\Daweed\Desktop\GeekBrains\2. Основы python\hw_python\lesson_5\text_for_hw_3.txt", "r", encoding="utf8") as f_obj:
        for line in f_obj.readlines():
            person = line.split()
            if int(person[1]) < 20000:
                print(person[0])
            counter += 1
            salary += int(person[1])
    print(f"Средний оклад = {salary / counter}")
    return None

some_func()