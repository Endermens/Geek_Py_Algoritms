my_number = input("введите любое натуральноео число:  ")
num_list = []
counter = {}
for num in my_number:
    num_list.append(int(num))

for elem in my_number:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)