# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, rate, bonus = argv
salary = int(hours)*int(rate) + int(bonus)

print("script: ", script_name)
print("выработка в часах: ", hours)
print("ставка в час: ", rate)
print("премия: ", bonus)
print("расчет заработной платы: ", salary)
