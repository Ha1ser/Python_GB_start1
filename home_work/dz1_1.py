# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

n = int(input("Введите 3 значное число: "))
n_1 = n // 100
n_2 = (n // 10) % 10
n_3 = n % 10
print(n_1 + n_2 + n_3)








