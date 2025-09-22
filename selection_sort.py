array = [2, 4, 8, 5, 1]
n = len(array)
for i in range(n - 1):
    min_index = i
    for j in range(range(i + 1, n)):
        if array[j] < array[min_index]:
            min_index = j
    min_val = array.pop(min_index)
    array.insert(i, min_val)
