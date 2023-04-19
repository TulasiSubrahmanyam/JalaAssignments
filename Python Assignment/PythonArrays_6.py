def copy_array(source_arr):
    # create a new array with the same length as source_arr
    dest_arr = [0] * len(source_arr)
    
    # copy the elements of source_arr to dest_arr
    for i in range(len(source_arr)):
        dest_arr[i] = source_arr[i]
    
    return dest_arr
arr1 = [1, 2, 3, 4, 5]
arr2 = copy_array(arr1)

print("arr1: ", arr1) # output: [1, 2, 3, 4, 5]
print("arr2: ", arr2) # output: [1, 2, 3, 4, 5]

arr1[0] = 0

print("arr1: ", arr1) # output: [0, 2, 3, 4, 5]
print("arr2: ", arr2) # output: [1, 2, 3, 4, 5]
