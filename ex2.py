import random

first_list = [random.randint(0, 100) for _ in range(10)]
second_list = [i for i, item in enumerate(first_list) if item % 2 == 0]

print(f'Для массива: \n{first_list}\nИндексы четных элементов: \n{second_list}')
