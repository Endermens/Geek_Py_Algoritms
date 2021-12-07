print("Введите два 3-х значныхчисла ")

firts_number = int(input('\nпервое трехзнаачноечисло: '))
second_number = int(input('второе трехзнаачноечисло: '))

while firts_number < 100 or second_number < 100 or firts_number > 999 or second_number > 999:
    print('попробуйте еще  ввести числа раз')
    firts_number = int(input('\nпервое трехзнаачноечисло: '))
    second_number = int(input('второе трехзнаачноечисло: '))

print(firts_number * second_number)
