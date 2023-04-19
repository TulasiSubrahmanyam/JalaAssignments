def remove_duplicates(arr):
    # Use the set data type to remove duplicates
    unique_set = set(arr)

    # Convert the set back to a list and return it
    return list(unique_set)
arr = [1, 2, 3, 4, 3, 5, 1, 6]
print(remove_duplicates(arr))