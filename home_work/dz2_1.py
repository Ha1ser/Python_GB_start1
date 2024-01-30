# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:

# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

# Пример использования На входе:
# coins = [0, 1, 0, 1, 1, 0]

# На выходе:
# 3

coins = [0, 1, 0, 1, 1, 0]

# flips = 0

# heads_count = coins.count(1)

# if heads_count > len(coins) / 2:
#     flips = len(coins) - heads_count
# else:
#     flips = heads_count

# print(flips)


# или 
n0 = 0 
n1 = 0
for i in coins:
    if i == 0:
        n0 += 1
    else:
        n1 += 1
if n0 > n1:
    print(n1)
else:
    print(n0)