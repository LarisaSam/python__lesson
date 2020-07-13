num_second = int(input("Введите время в секундах"))

hour = num_second // 3600
min = (num_second - hour * 3600) // 60
sec = (num_second - hour * 3600) % 60

print(f'Введенное время - часы:минуты:секунды:{hour}:{min}:{sec}')
