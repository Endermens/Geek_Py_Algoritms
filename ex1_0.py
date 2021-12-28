# part 1 ex 3
import sys
""" 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки. """

print('ведите координаты точек, принимаються только целые числа')
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

#Ax + By + C = 0 ; Ax + By + C = 0
a = y1 - y2
b = x2 - x1
c = x1 * y2 - x2 * y1
if a == 0 and b == 0:
    print('Точки совпадают')
elif a == 0:
    print(f'Уравнение прямой:\n'
          f'{b}y + {c} = 0')
elif b == 0:
    print(f'Уравнение прямой:\n'
          f'{a}x + {c} = 0')
else:
    print(f'Уравнение прямой:\n'
          f'{a}x + {b}y + {c} = 0')

print(sys.getsizeof(x1))
print(sys.getsizeof(y1))
print(sys.getsizeof(x2))
print(sys.getsizeof(y2))
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

# Python 3.10.0 (tags/v3.10.0:b494f59
# (x1) = 0, bite 24 (ноль весит 24 байта серьйозно ?!)
# (y1) = 1, bite 28
# (x2) = 2, bite 28
# (y2) = 3, bite 28
# (a)  bite 28
# (b)  bite 28
# (c)  bite 28
# программа задествовала 192 байта на значения
