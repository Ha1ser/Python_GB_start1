# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

num = 4
num1 = 0
num2 = 1
num3 = 0
size = 1
while num3 < num:

    num3 = num2 + num1
    num1 = num2
    num2 = num3
    size += 1
    if num3 > num:
        size = -1
print(size)










