# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# closest_num = None      # none значит пусто
# min_diff = float('inf')   # float('inf') обозначает бесконечность

# for num in list_1:
#     diff = abs(num - k)
#     if diff < min_diff:
#         min_diff = diff
#         closest_num = num

# print(closest_num)


# или

list_1 = [9, 2, 3, 4, 4, 7]
k = 6
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
