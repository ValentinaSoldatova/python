my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

with open("5.4_f.txt") as file_read, open('5.4_f_new.txt','w', encoding= 'utf-8') as file_write:
    for line in file_read.readlines():
        text_number, number = line.rstrip().split(' - ')
        file_write.write(f'{my_dict[text_number]} - {number}\n')


