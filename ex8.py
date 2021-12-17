# M = 5
# N = 4
# a = []
# for i in range(N):
#     b = []
#     s = 0
#     print("%d-я строка:" % i)
#     for j in range(M-1):
#         n = int(input())
#         s += n
#         b.append(n)
#     b.append(s)
#     a.append(b)
#
# for i in a:
#     print(i)

matrix = [[] for _ in range(4)]

for line in matrix:
    line_sum = 0
    for i in range(4):
        num = int(input('Введите значение: '))
        line.append(num)
        line_sum += num
    line.append(line_sum)

for line in matrix:
    for num in line:
        print(f'\t{num:>5}', end='')
    print()