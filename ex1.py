div_dict = dict.fromkeys(range(2, 10), 0)
for num in range(2, 100):
    for i in range(2, 10):
        if num % i == 0:
            div_dict[i] += 1

for key in div_dict:
    print(f'{key} кратно {div_dict[key]} чисел')
