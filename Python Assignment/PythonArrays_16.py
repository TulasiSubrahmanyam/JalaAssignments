def get_difference(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Compute the difference and return it
    return max_val - min_val
arr = [1, 2, 3, 4, 5]
diff = get_difference(arr)
print(diff)
