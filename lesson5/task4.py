# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("task4.txt", "r") as org_f, open("task4-rus.txt", "w") as rus_f:
    for line in org_f.readlines():
        row = line.split()
        if row[0] == 'One':
            row[0] = 'Один'
        elif row[0] == 'Two':
            row[0] = 'Два'
        elif row[0] == 'Three':
            row[0] = 'Три'
        elif row[0] == 'Four':
            row[0] = 'Четыре'
        rus_f.write(' '.join(row)+'\n')  # this adds additional blank line at the end of file, dont know how to avoid it
        print(row)
        
# Resulting file:
# Один — 1
# Два — 2
# Три — 3
# Четыре — 4
# (blank)
