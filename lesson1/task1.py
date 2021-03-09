# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

my_name = 'Алена'  # variable string
my_country = 'Canada'
my_age = 30  # int variable
km_away = 8.194  # float variable
print('Привет! Меня зовут {} и я живу в стране {} мне около {}-ти лет ))'.format(my_name, my_country, my_age))
print('Я нахожусь в ' + str(km_away) + ' км от Москвы')  # trying both ways to print out the text

my_friend_name = input('А как тебя зовут? (напечатай, пожалуйста, свое имя и нажми Enter)')
print('Привет! ' + my_friend_name)

my_friend_age = int(input('А сколько тебе лет?'))
if my_friend_age <= 0:
    input('Хмм...ну может тогда внутренний возраст ;) ?')

my_friend_country = input('В каком городе ты живешь?')

print('{}! Приятно познакомиться! До встречи в {} хехе...))'.format(my_friend_name, my_friend_country))
