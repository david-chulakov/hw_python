# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):

    def draw(self):
        return "Пишу ручкой"


class Pencil(Stationery):

    def draw(self):
        return "Рисую карандашом"


class Handle(Stationery):

    def draw(self):
        return "Маркирую важные темы"


start = Stationery('Начинаем')
print(start.draw())

bic = Pen("Ручка")
print(bic.title)
print(bic.draw())

karandash = Pencil('Карандаш')
print(karandash.title)
print(karandash.draw())

marker = Handle('Маркер')
print(marker.title)
print(marker.draw())
