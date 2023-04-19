def check_array(arr):
    # Check if both 12 and 23 are in the array
    if 12 in arr and 23 in arr:
        return True
    else:
        return False
arr = [1, 12, 3, 4, 23, 5]
result = check_array(arr)
print(result)
