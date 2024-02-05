# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать. 

def quit_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quit_sort(less) + [pivot] + quit_sort(greater)

print(quit_sort([14, 5, 9, 1, 3, 4, 5, 6]))

