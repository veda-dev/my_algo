def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubble_sort_recursive(arr, i, j):
    if j == len(arr):
        i = i + 1
        j = i
    if i == len(arr):
        return arr
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        return bubble_sort_recursive(arr, i, j+1)
    else:
        return bubble_sort_recursive(arr, i, j+1)


# my_array = [6, 5, 7, 9, 2, 1, 4]
# print(bubble_sort(my_array))
my_array2 = [6, 5, 7, 9, 2, 1, 4]
print(bubble_sort_recursive(my_array2, 0, 0))