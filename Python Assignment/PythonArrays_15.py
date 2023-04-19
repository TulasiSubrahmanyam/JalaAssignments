def count_even_odd(arr):
    # Initialize the counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Loop through the array
    for num in arr:
        # If the element is even, increment the even_count counter
        if num % 2 == 0:
            even_count += 1
        # If the element is odd, increment the odd_count counter
        else:
            odd_count += 1
    
    # Print the results
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)
arr = [1, 2, 3, 4, 5]
count_even_odd(arr)
