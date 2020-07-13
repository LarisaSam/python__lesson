var01 = 10 + 20
print(var01)

var02 = "some text....."
print(var02)

var03 = 50
var04 = var03 + var01
print(var04)

count_min = int(input("Введите минимальное число диапазона>>>"))
count_max = int(input("Введите максимальное число диапазона>>>"))
print("Диапазон чисел:")
while count_max >= count_min:
    print(count_min)
    count_min += 1


username = input("Введите Ваше имя>>>")
user_surname = input("Введите Вашу фамилию")
print(username, user_surname)
