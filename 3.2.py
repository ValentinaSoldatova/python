def customer(name, surname, year, city, email, phone):
    return print(f'Имя: {name} Фамилия: {surname} Год рождения: {year}  Город проживания: {city} Email: {email} Телефон: {phone}')

customer(
    name= input("Введите имя "),
    surname = input("Введите фамилию "),
    year = int(input("Введите год рождения ")),
    city = input("Введите город проживания "),
    email = input("Введите e-mail "),
    phone = int(input("Введите номер телефона ")),
)

