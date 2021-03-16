#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func():
    x = int(input('X'))
    y = int(input('Y'))
    return x / y


try:
    z = my_func()
    print(z)
except ZeroDivisionError:
    print('Division by zero')
