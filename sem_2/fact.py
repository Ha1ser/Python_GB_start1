# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while


# n = int(input("Введите значение: "))
# i = 1
# j = 1
# while i <= n:
#     if n == 0:
#         print(1)
#     else:
#         j = j * i
#         i = i + 1
# print(j)

# 2 способ
n = int(input())
i = 1
res = 1
while i <= n:
    if n == 0:
        print(1)
        break
    res = res * i
    i = i + 1
print(res) 
