# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")
    
# second_func(var_1=10, var_2=20, var_3=30)


def f_user(name, l_name, yob, city, email, phone):
    print(f"name {name}, l_name {l_name}, yob {yob}, city {city}, email {email}, phone {phone}")


f_user(l_name='Ivanov', name='Ivan', yob='1997', city='Ivanovo', phone='902-785-6745', email='ii@ivanov.ru')


