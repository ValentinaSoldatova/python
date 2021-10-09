revenue= (int(input("Введите сумму выручки: ")))
costs= (int(input("Вdедите сумму издержек: ")))
if revenue > costs:
    print(f"Ваша компания в прибыли.Рентабельность составляет {revenue/ costs}")
    employee= (int(input("Введите количество сотрудников: ")))
    print(f"Прибыль на одного сотрудника составляет {revenue/ employee}")
else:
    print("Увы, ваше финансовое состояние требует коррекции")