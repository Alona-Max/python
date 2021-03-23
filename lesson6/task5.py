# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки: ', self.title)


class Pen(Stationary):
    def draw(self):
        print(f"Запуск отрисовки Ручкой: {self.title}")


class Pencil(Stationary):
    def draw(self):
        print(f"Запуск отрисовки Карандашом: {self.title}")


class Handle(Stationary):
    def draw(self):
        print(f"Запуск отрисовки Маркером: {self.title}")


st = Stationary("Отрисовка №1")
pencil = Pencil("Портрет карандашом")
pen = Pen("Зарисовка ручкой")
marker = Handle("Пейзаж маркером")


st.draw()
pen.draw()
pencil.draw()
marker.draw()
