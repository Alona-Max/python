# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self,
                 name,
                 surname,
                 position,
                 wage,
                 bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict()
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


employee_list = list()
employee_list.append(Position("Boris", "Maksimenko", "DBA", 120000, 23000))
employee_list.append(Position("Polina", "Maksimenko", "Web developer", 99900, 8700))
employee_list.append(Position("Taisiya", "Maksimenko", "Youtuber", 10000, 230500))
employee_list.append(Position("Danila", "Maksimenko", "QA", 90000, 23400))

for wr in employee_list:
    print(wr.get_full_name(), wr.get_total_income())
