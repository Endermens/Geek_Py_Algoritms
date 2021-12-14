print('орфиметические операции')
print('чтобы выйти выберите в доступных операциях - 0\n')

arithmetic_operation = None

while arithmetic_operation != '0':
    a = int(input('\nведите первую цифру: '))
    b = int(input('ведите вторую цифру: '))
    arithmetic_operation = str(input("доступные операции:  '+', '-', '*', '/' "))
    if arithmetic_operation == '+':
        print(f'{a + b}')
    elif arithmetic_operation == '-':
        print(f'{a - b}')
    elif arithmetic_operation == '*':
        print(f'{a * b}')

    elif arithmetic_operation == '/':
        if b == 0:
            print('делить на ноль нельзя')
        else:
            print(f'{a / b}')

    elif arithmetic_operation == '0':
        print('\nдосвидания')
    else:
        print('error')