# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_entry = int(input('Время в секундах'))

hours = user_entry // 3600  # converting into Hours whole part
minutes = user_entry % 3600 // 60
rem_sec = user_entry % 3600 % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, rem_sec))
