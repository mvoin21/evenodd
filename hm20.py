# nmbrs = input('Введите числа через запятую: ') 

def cnt():
    nmbrs = input('Введите числа через запятую: ')
    even = []
    odd = []
    list_num = nmbrs.split(',')
    for item in list_num:
        if int(item) % 2 == 0 or int(item) == 0:
            even.append(item)
        else:
            odd.append(item)
    print('Четных чисел:', len(even))
    print('Нечетных чисел:', len(odd))

cnt()
