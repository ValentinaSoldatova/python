my_string= input("Введите строку: ")
words= my_string.split()

for index, word in enumerate(words, 1):
    print(index, word[:10])