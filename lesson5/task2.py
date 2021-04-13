# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

line_count = 0
word_count = 0
with open("task2.txt", "r") as file:

    for line in file.readlines():
        # line = line.split("\n")
        line_count += 1
        ln_wrd_cnt = len(line.split())
        word_count += ln_wrd_cnt
        print(ln_wrd_cnt)  # number of words in each line of text

print("The number of lines in the file")
print(line_count)  # number of lines in the file including blanks
print("The number of words")
print(word_count)  # number of words in the file
