# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open("task5.txt", "w") as f:
    for i in range(10):
        f.write(str(random.randrange(1000))+' ')
with open("task5.txt", "r") as f:
    print(sum(map(int, f.readline().split())))

