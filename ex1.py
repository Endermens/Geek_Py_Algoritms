# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

## дефолд вариант
# print("укажите количество предприятий")
#
# c_factory = int(input("количество: "))
# factory_name = []
# profit = []
# for i in range(1, (c_factory + 1)):
#     factory_name.append(input(f"\nназвание {i}-го предприятия:\t"))
#     factory_profit = int(input(f"ведите прибыль за 4-е квартала {i}-го завода: "))
#     profit.append(factory_profit)
# year_profit = sum(profit)//len(profit)
# print(f"средняя прибыль предприятий за год состовляет: {year_profit} $\n")
#
# more = []
# less = []
# for i in range(c_factory):
#     if profit[i] >= year_profit:
#         more.append([f"{i+1}-е предприятие",profit[i]])
#     else:
#         less.append([f"{i+1}-е предприятие", profit[i]])
#
# print("предприятия чьих доход выше среднего")
# if len(more) != 0:
#     for i in range(len(more)):
#         print(*more[i], sep = ': ')
# else:
#     print("...")
# print('_' * 60, '\n')
# print("предприятия чьих доход ниже среднего")
# if len(less) != 0:
#     for i in range(len(less)):
#         print(*less[i], sep = ': ')
# else:
#     print("...")


## вариант с приминением collections
from collections import namedtuple
from statistics import mean

New_Company = namedtuple('Company_Name', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компани: '))):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg > avg:
        print(i.name)
