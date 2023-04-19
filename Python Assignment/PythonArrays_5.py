#removing specific element from an array
def remove_element(arr, element):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] != element:
            new_arr.append(arr[i])
    return new_arr
arr=[1,4,5,6,3,8]
value=2
print(remove_element(arr,value))
