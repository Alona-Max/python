# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"{self.name} {self.color} машина поехала\n")

    def stop(self):
        self.speed = 0
        print(f"{self.name} машина остановилась\n")

    def turn(self, direction):
        if direction in {"left", "right", "forward", "backward", "u-turn"}:
            print(f"{self.name} машина повернула {direction}")
        else:
            print(f"{self.name} машина не может выполнить этот маневр")

    def show_speed(self):
        print(f"{self.name} машина движется со скоростью {self.speed}\n")


class TownCar(Car):
    __speed_limit = 60

    def show_speed(self):
        print(f"{self.name} машина движется со скоростью {self.speed}")
        if self.speed > self.__speed_limit:
            print(f"{self.name} превышение лимита скорости на {self.speed - self.__speed_limit}\n")


class SportCar(Car):
    pass


class WorkCar(Car):
    __speed_limit = 40

    def show_speed(self):
        print(f"{self.name} {self.color } движется со скоростью {self.speed}")
        if self.speed > self.__speed_limit:
            print(f"{self.name} превышение лимита скорости на {self.speed - self.__speed_limit}\n")


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)
        print('Police')


lamby = SportCar('silver', 'Lamborgini 2020')
lamby.go(120)
lamby.show_speed()
toyota = TownCar('white', 'Toyota Corolla 2015')
toyota.go(65)
toyota.show_speed()
dodge = PoliceCar('black', 'Dodge Charger 2019')
dodge.go(135)
tonka = WorkCar('orange', 'Tonka 2015')
tonka.go(45)
tonka.show_speed()
tonka.turn('right')
tonka.turn('yup')
tonka.stop()
toyota.turn('left')
lamby.turn('u-turn')
dodge.turn('u-turn')
lamby.stop()
dodge.stop()


