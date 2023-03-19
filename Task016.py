# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# *Пример:* 5     1 2 3 4 5      3     -> 1

input_list = []
list_num = int(input("Введите количество элементов в массиве, N:  "))

for i in range(list_num):
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

find_x = int(input("Введите число, X:  "))

count = 0
# start = time.pert_counter()
for i in range(list_num):
    if input_list[i] == find_x:
        count += 1
print(count)
# end = time.pert_counter()
# print(end - start)

# start = time.pert_counter()
print(input_list.count(find_x))
# end = time.pert_counter()
# print(end - start)
