# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.


str1 = 'a a a b c a a d c d d'.split()
slov1 = {}
for i in str1:
    if i in slov1:
        print(f'{i}_{slov1[i]}', end=' ')
        slov1[i] += 1
    else:
        print(i, end = " ") # вывод в одной строке
        slov1[i] = 1
print(slov1)

# или

# str1 = 'a a a b c a a d c d d'.split()
# slov1 = {}
# for i in str1:
#     if i in slov1:
#         print(f'{i}_{slov1[i]}', end=' ')
#         #slov1[i] += 1
#     else:
#         print(i, end = " ") # вывод в одной строке
#         #slov1[i] = 1
#     slov1[i] = slov1.get(i, 0) + 1

# print(slov1.get('a', 999))

