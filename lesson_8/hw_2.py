# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class Division_by_zero:

    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    def divide(self):
        try:
            return self.divider / self.denominator
        except:
            return "Деление на ноль недопустимо"


div = Division_by_zero(10, 0)
print(div.divide())
