
def bubble_sort(arr):
    for _ in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted array:", bubble_sort(arr))
