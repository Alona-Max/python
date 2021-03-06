# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

sales = float(input("Введите выручку фирмы "))
expenses = float(input("Введите издержки фирмы "))
profit = sales - expenses  # прибыль
if sales > expenses:
    print('Прибыль фирмы составляет: {}. Рентабельность выручки составила {:.2f} % '  # trying different ways to format
          .format(profit, 100*profit/sales))
    employees = int(input('Введите количество сотрудников фирмы '))
    print(f'Прибыль, в расчете на одного сторудника сотавила {profit / employees:.2f}')
else:
    print('Фирма работает в убыток')
