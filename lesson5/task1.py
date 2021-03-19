# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# Not sure how to add .txt to the file with this approach
# tested it with filename like test.txt  -- it create .txt file

filename = input("Create New or Open file: ")
print('Enter data, press Enter to finish')
with open(filename, "w") as f:  # create file with filename or opens existing and delete all from it
    f.write(input())  # accepts user input to write to the file, Enter finishes input


# creating .txt file

# with open("file.txt", "w") as f:  # creates file.txt or opens existing one(delete all from it)
#     f.write(input())  # writes user input to the file until user hit Enter
