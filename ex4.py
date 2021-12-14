length = int(input('Введите длину последовательности: '))
my_sum = 0
for i in range(length):
    my_sum += 1 / (-2) ** i
print(f'Сумма последовательности = {my_sum}')