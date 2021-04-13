# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

count = 0
summa = 0
with open("task3.txt") as f:
    # opens existing file for reading. File content:
    # Ivanov 21050
    # Sidorov 19100
    # Petrov 23500
    # Petrovna 30300
    for line in f.readlines():
        row = line.split()
        row[1] = int(row[1])
        summa += row[1]
        count += 1
        if row[1] < 20000:
            print('Оклад менее 20 тыс у', row[0], row[1])

print('Средний доход ', summa / count)
