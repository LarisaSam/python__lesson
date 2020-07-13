n = int(input("Введите целое положительное число>>>"))
num_max = n % 10
n = n // 10
while n > 0:
    if n % 10 > num_max:
        num_max = n % 10
    n = n // 10
print("Самая большая цифра в числе:", num_max)
