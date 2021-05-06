# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self, direction):
        return f"{self.name} повернула {direction}"

    def show_speed(self):
        return f"{self.speed} км/ч"


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"{self.speed} км/ч. Скорость превышена, есть опасность поймать столб"
        else:
            return f"{self.speed} км/ч"


class SportCar(Car):

    def start_drift(self):
        return f"{self.name} Начал валить боком"

    def stop(self):
        return f"{self.name} Дал столба, жду эвакуатор"

    def wash(self):
        return "Помыл своего коня"


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"{self.speed} км/ч. Скорость превышена"
        else:
            return f"{self.speed} км/ч"

    def go(self):
        return "Еду на работу, стою в пробке"


class PoliceCar(Car):

    def go(self):
        return "Мчу на вызов"


police777 = PoliceCar(100, 'white', 'ww_polo', True)
print(police777.go())
print(police777.is_police)

fiat = WorkCar(50, 'yellow', 'fiat')
print(fiat.show_speed())

buggati = SportCar(380, 'blue', 'buggati')
print(buggati.go())
print(buggati.show_speed())
print(buggati.stop())

solaris = TownCar(59, 'white', 'hyundai')
print(solaris.go())
print(solaris.turn('направо'))
print(solaris.turn('налево'))
print(solaris.show_speed())
print(solaris.stop())