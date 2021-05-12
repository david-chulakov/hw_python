# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        # self.day = day
        # self.month = month
        # self.year = year
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.date)}'


today = Date('15 - 3 - 2005')
print(today)
print(Date.valid(12, 8, 2022))
print(today.valid(11, 13, 2011))
print(Date.extract('11 - 05 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(1, 11, 2000))

