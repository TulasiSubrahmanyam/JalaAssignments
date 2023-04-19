def find_duplicates(arr):
    # create an empty set to store unique values
    unique = set()

    # create an empty list to store duplicate values
    duplicates = []

    # iterate over each element in the array
    for element in arr:
        # if the element is already in the unique set, it's a duplicate
        if element in unique:
            duplicates.append(element)
        else:
            unique.add(element)

    # return the list of duplicate values
    return duplicates
arr=[1,2,3,4,5,3,2,5,6,3]
print(find_duplicates(arr))