my_number = input('ведите натураальное число: ')
odd = 0
even = 0
for num in my_number:
    if int(num) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'В числе {my_number}: {odd} нечетных и {even} четных цифр')