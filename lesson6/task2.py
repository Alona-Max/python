# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    _asphalt_per_sq_meter_1cm = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см

    def __init__(self, length_meters, width_meters):
        self.__length = length_meters
        self.__width = width_meters

    def get_asphalt_mass_ton(self, thickness_centimeters):
        return self.__length * self.__width * self._asphalt_per_sq_meter_1cm * thickness_centimeters / 1000


road1 = Road(5000, 20)
print(road1.get_asphalt_mass_ton(5))
