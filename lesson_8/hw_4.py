#  Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#  который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#  В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
#  уникальные для каждого типа оргтехники.
#
#  Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
#  определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
#  других данных, можно использовать любую подходящую структуру, например словарь.

#  Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
#  для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.



class Warehouse:

    warehouse = {}

    @classmethod
    def show_equipment(cls):
        return cls.warehouse


    @classmethod
    def add_equip(cls, *args):
        cls.warehouse.update(*args)
        return f"Успешно привезли на склад"

    @classmethod
    def delete_equip(cls, name):
        del cls.warehouse[name]
        return f"{name} увезли со склада"


class Equipment():

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_to_warehouse(self):
        Warehouse.add_equip({self.name: {"цена": self.price, 'кол-во': {self.quantity}}})
        return f"{self.name} привезли на склад"


class Printer(Equipment):

    def to_print(self):
        num_of_lists = int(input("Введите кол-во листов: "))
        return f"Распечатал {num_of_lists} листов"

class Scanner(Equipment):

    def to_scan(self):
        num_of_lists = int(input("Введите кол-во листов: "))
        return f"Отсканировал {num_of_lists} листов"

class Xerox(Equipment):
    def to_xerox(self):
        num_of_lists = int(input("Введите кол-во листов: "))
        return f"Копирую {num_of_lists} листов"


ware = Warehouse()
xerox = Xerox("Ксерокс", 5000, "50 шт.")
printer = Printer("Принтер", 2500, "25 шт.")
print(xerox.to_xerox())
print(xerox.add_to_warehouse())

print(printer.to_print())
print(printer.add_to_warehouse())

print(ware.show_equipment())
print(ware.delete_equip('Принтер'))
print(ware.show_equipment())
