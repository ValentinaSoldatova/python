a= int(input("Сколько вы пробежали в 1-ый день,в км: "))
b= int(input("Какого результата вы планируете достигнуть,в км: "))
run_days= 1
run_km= a
while run_km < b:
    a += a* 0.1
    run_days +=1
    run_km= run_km +a
    print(f"Ваш результат будет достигнут на %.d день" % run_days)

