# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    def __init__(self, valid_part: int, imaginary_part: int):
        """ Конструктор класса

        :param valid_part: действительная часть
        :param imaginary_part: мнимая часть без мнимой единицы
        """
        self.valid_part = valid_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f"{self.valid_part} + {self.imaginary_part}i"

    def __add__(self, other):
        return Complex(self.valid_part + other.valid_part, self.imaginary_part + other.imaginary_part)

    def __sub__(self, other):
        return Complex(self.valid_part - other.valid_part, self.imaginary_part - other.imaginary_part)

    def __mul__(self, other):
        return Complex(self.valid_part * other.valid_part - self.imaginary_part * other.imaginary_part,
                       self.valid_part * other.imaginary_part - self.imaginary_part * other.valid_part)


complex1 = Complex(5, 4)
complex2 = Complex(3, 2)
print(complex1)
print(complex2 + complex1)
print(complex1 - complex2)
print(complex1 * complex2)