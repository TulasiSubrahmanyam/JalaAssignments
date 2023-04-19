def insert_element(arr, element, position):
    """
    Inserts an element at a specific position in the array.

    Parameters:
    arr (list): The input array.
    element (int or any): The element to be inserted in the array.
    position (int): The index at which the element should be inserted.

    Returns:
    list: The updated array with the new element inserted.
    """

    # check if position is valid
    if position < 0 or position > len(arr):
        print("Invalid position")
        return arr
    
    # insert the element at the specified position
    arr.insert(position, element)
    
    return arr
arr = [1, 2, 3, 4, 5]
element = 6
position = 2

print("Original array:", arr)

arr = insert_element(arr, element, position)

print("Updated array:", arr)
