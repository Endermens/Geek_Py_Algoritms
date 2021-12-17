import random

num_list = [random.randint(1, 100) for _ in range(10)]
min_el = num_list[1]
pre_min = num_list[0]

for num in num_list:
    if num <= min_el:
        pre_min = min_el
        min_el = num
    # если минимальный элемент находится вначале
    elif num <= pre_min:
        pre_min = num

print(f'В массиве: \n{num_list} '
      f'\nминимальные элементы: {min_el} и {pre_min}')