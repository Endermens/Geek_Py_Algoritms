# patr 3 ex 3
import random, sys

num_list = [random.randint(0, 100) for _ in range(10)]
print(*num_list)
min_el = num_list[0]
max_el = num_list[1]

print(sys.getsizeof(num_list), "<num_list> старт")
print(sys.getsizeof(min_el), "<min_el> старт")
print(sys.getsizeof(max_el), "<max_el> старт")

for i, item in enumerate(num_list):
    if item <= min_el:
        min_el = item
        min_idx = i
        print(sys.getsizeof(i), "<i> if item <= min_el")
        print(sys.getsizeof(item), "<item>")
    if item >= max_el:
        max_el = item
        max_idx = i
        print(sys.getsizeof(i), "<i> if item >= max_el")
        print(sys.getsizeof(item), "<item>")

num_list[min_idx] = max_el
num_list[max_idx] = min_el
print(sys.getsizeof(num_list), "<num_list> финал")

print('Переставим максимальный и минимальный элементы:\n', *num_list)

# результаты
# 184 <num_list> старт
# 28 <min_el> старт
# 28 <max_el> старт
# 24 <i> if item <= min_el
# 28 <item>
# 24 <i> if item >= max_el
# 28 <item>
# 28 <i> if item <= min_el
# 28 <item>
# 28 <i> if item >= max_el
# 28 <item>
# 28 <i> if item >= max_el
# 28 <item>
# 28 <i> if item <= min_el
# 28 <item>
# 28 <i> if item <= min_el
# 28 <item>
# 184 <num_list> финал
# 296 байтов использовалось, если всеже i и item использовали каждый раз новую ячейку в памяти то
# затребовалось намного больше...
