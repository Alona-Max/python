# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_input = int(input('Введите число  '))
n = str(user_input)
nn = n + n
nnn = n + n + n
total = int(n) + int(nn) + int(nnn)

print(n, nn, nnn)
print(total)
