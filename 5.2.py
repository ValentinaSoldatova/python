with open("my_text.txt", "r", encoding= 'utf-8') as f:
    cont = f.read()
    print(f'Файл содержит: \n{cont}')
    f.seek(0)
    lines = f.readlines()
    print(f'Количество строк: {len(lines)}')
    f.seek(0)
    for i in range(len(lines)):
        line = f.readline()
        words = line.split()
        print(f'Количество слов в  {i + 1}-ой строке: {len(words)}')



