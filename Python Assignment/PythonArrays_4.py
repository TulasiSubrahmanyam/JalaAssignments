def contains_value(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return True
    return False
arr1=[1,3,4,5,6,7]
value=5
print(contains_value(arr1,value))