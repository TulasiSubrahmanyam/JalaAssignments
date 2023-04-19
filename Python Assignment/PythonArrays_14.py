def find_second_largest(arr):
    # Check if the array has at least two elements
    if len(arr) < 2:
        return None
    
    # Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Find the second largest element in the array
    second_largest = sorted_arr[1]
    
    # Return the second_largest
    return second_largest
arr=[1,2,3,4,5,3,8,7]
print(find_second_largest(arr))