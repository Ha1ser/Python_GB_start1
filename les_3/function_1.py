# Задача
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.
# Решение:
# 1. Необходимо создать функцию:
# def sumNumbers(n):


    #1
# def sumNumbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     print(sum)

# sumNumbers(5) 



    #2
# def sumNumbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i 
#     return sum

# print(sumNumbers(5))
 
# или

# def sumNumbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i 
#     return sum

# a = (sumNumbers(5))
# print(a) 


def sumNumbers(n, y = "qwerty"): # передаём аргумент и вызываем его
    print(y)
    sum = 0
    for i in range(1, n+1):
        sum += i 
    return sum

a = (sumNumbers(5, y = "ffff"))
print(a) 
 
