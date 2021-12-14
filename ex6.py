import random

print('отгадай число от 0 до 100')
random_number = random.randrange(0, 101)
print(random_number)
print(type(random_number))
my_number = 0
my_try = 10
while my_try != 0 and my_number != random_number:
    my_number = int(input("\nэто число: "))
    if my_number == random_number:
        print(f"вы угадали это {my_number}")
    elif my_number < random_number:
        print("нет, берите выше")
        my_try -= 1
        print(f"у вас осталось  {my_try} попыток")
    elif my_number > random_number:
        print("нет, берите поменьше")
        my_try -= 1
        print(f"у вас осталось  {my_try} попыток")
    else:
        print('booba!')