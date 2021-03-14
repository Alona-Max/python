# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Method 1


def my_func(x, y):
    return x**y


print(my_func(5, -3))


# Method 2
def my_func1(x, y):
    divider = x
    for i in range(1, abs(y)):
        divider *= x
    return 1/divider


print(my_func1(5, -3))
