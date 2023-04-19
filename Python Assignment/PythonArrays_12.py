def remove_duplicates(arr):
    # Create an empty list to store the unique elements
    unique_arr = []

    # Loop through the array
    for elem in arr:
        # If the element is not already in the unique_arr, add it
        if elem not in unique_arr:
            unique_arr.append(elem)

    # Return the unique_arr
    return unique_arr
arr=[1,2,3,4,3,2,4,5,4,3]
print(remove_duplicates(arr))