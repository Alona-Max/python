# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.


import time
from itertools import cycle


class TrafficLight:
    _colors = [{"name": "red", "ansi": "\033[1;37;41m", "delay": 7},
               {"name": "yellow", "ansi": "\033[1;37;43m", "delay": 2},
               {"name": "green", "ansi": "\033[1;37;42m", "delay": 7}]

    def __init__(self):
        self._color = "red"

    def running(self):
        for c in cycle(self._colors):
            self._color = c["name"]
            print(c["ansi"] + c["name"])
            time.sleep(c["delay"])


traffic = TrafficLight()
traffic.running()
