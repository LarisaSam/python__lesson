receipt = int(input("Введите сумму выручки>>>"))
costs = int(input("Введите сумму издержек>>"))

result = receipt - costs

if result > 0:
    print("Финансовый результат - прибыль", result, "руб.")

    profitability = result / receipt
    print("Рентабельность:", round(profitability*100, 2), "%")

    number_employees = int(input("Ввведите численность сотрудников>>>"))
    result_employee = result / number_employees

    print("Прибыль в расчете на одного сотрудника:", round(result_employee, 2), 'руб.')

if result < 0:
    print('Финансовый результат - убыток', result, 'руб.')