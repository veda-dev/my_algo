def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    return arr


my_array = [6, 5, 7, 9, 2, 1, 4]
print(bubble_sort(my_array))