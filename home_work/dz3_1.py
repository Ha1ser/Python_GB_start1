# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1


list_1 = [4, 1, 2, 3, 4, 5, 4, 4, 4]
k = 4
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)

# или 
list_1 = [4, 1, 2, 3, 4, 5, 4, 4, 4]
k = 4
count = 0
for i in list_1:
    if k == i:
        count += 1
print(count)

