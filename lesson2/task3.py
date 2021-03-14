# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

#  List
seasons = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
winter = ['12', '1', '2']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
fall = ['9', '10', '11']

while True:
    user_input = int(input('Enter the month number from 1 to 12 '))
    if 0 < user_input < 13:
        break

print(seasons[user_input])

#####################################################################################################
# Dictionary
seasons = {1: 'winter', 2: 'winter', 12: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
           7: 'summer', 8: 'summer', 9: 'fall', 10: 'fall', 11: 'fall'}
while True:
    user_input = int(input('Enter the month number from 1 to 12 '))
    if 0 < user_input < 13:
        break
if user_input in seasons:
    print(seasons.get(user_input))
