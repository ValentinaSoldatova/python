sum = 0

with open("5_text.txt") as file:
    lines = file.readlines()
    for line in lines:
        last_name, salary = line.split()
        sum += int(salary)
        if int(salary) < 20000:
            print('У сотрудника оклад менее 20 тыс рублей: ', last_name)

print(f"средний доход сотрудников:", sum / len(lines))
