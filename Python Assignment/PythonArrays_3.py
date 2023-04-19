# define an array of numbers
numbers = [10, 20, 30, 40, 50]

# function to find the index of an element in an array
def find_index(arr, value):
    # loop through each element in the array
    for i in range(len(arr)):
        # check if the current element is equal to the value
        if arr[i] == value:
            # return the index of the element
            return i
    # if the element is not found, return -1
    return -1

# find the index of 30 in the array
index = find_index(numbers, 30)

# print the index
print("Index of 30:", index)
