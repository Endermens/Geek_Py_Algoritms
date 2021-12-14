num = 1
max_sum = 0
while num != 0:
    num = int(input('\nВведите целое число. Чтобы выйти введите 0.\n\tnum = '))
    digit_sum = 0
    n = num
    while num % 10 != 0 or num // 10 != 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = n
print(f'\tУ числа {max_num} сумма цифр = {max_sum}')