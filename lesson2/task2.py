# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el = int(input('Enter the number of elements'))
my_list = []
for k in range(el):
    my_list.append(input(f"element {k}:"))
    # ['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5]
print(my_list)
for i in range(0, (len(my_list)//2)*2, 2):  # start, stop, step
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)
