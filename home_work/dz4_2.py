# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.

# Пример использования На входе:


# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:


# 19

arr = [2, 4, 10, 4, 2]
max1 = 0
j = 0
for i in range(1, len(arr) - 1):
        j = arr[i] + arr[i + 1]  + arr[i - 1] 
        if max1 < j:
            max1 = j
print(max1)
# max2 = 0
# m1 = arr[0] + arr[1]
# m2 = arr[-1] + arr[-2]

# if m1 > m2:
#     max2 = m1
# else:
#     max2 = m2

# if max1 > max2:
#     print(max1)
# else:
#     print(max2)



 











