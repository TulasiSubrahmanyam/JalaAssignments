def min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    return (min_val, max_val)
arr = [3, 5, 1, 7, 9, 2, 8, 4, 6]
min_val, max_val = min_max(arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
