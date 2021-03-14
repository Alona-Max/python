# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_input = str(input('Enter few words different length'))

for l, word in enumerate(user_input.split(' ')):
    print(l+1, word[:10])


