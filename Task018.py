# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:* 5    1 2 3 4 5     6     -> 5

input_list = []
list_num = int(input("Введите количество элементов в массиве, N:  "))


for i in range(list_num):
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

input_x = int(input("Задайте/Введите число, X:  "))

def found_nearest_num(input_list, input_x):
    found_x = input_list[0]
    for i in input_list:
        if abs(i - input_x) < abs(found_x - input_x):
            found_x = i
    return found_x
print(f'Ближайшее число к Заданному: {found_nearest_num(input_list, input_x)}')


# abs function возвращает абсолютное значение числа


#find_x = input_x
#for i in range(len(input_list)):
#    if input_list[i] < input_x:
#        find_x = -find_x
#    else:
#        find_x = find_x + 0
#    if input_list[i] >= input_x and input_list[i] - input_x <= find_x - input_x:
#        find_x = input_list[i]
#    elif input_list[i] <= input_x and find_x - input_x <= input_list[i] - input_x:
#        find_x = input_list[i]
#print(f'Ближайшее число к Заданному: {find_x}')