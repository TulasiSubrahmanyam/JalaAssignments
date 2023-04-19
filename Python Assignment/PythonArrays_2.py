def average_array(arr):
    sum = 0
    n = len(arr)
    for i in arr:
        sum += i
    avg = sum / n
    return avg
my_array = [1, 2, 3, 4, 5]
print(average_array(my_array))  # Output: 3.0
