def increment_decrement(num, operator):
    """
    This function increments or decrements the given number by 1 using the specified operator.

    Args:
    - num: the number to increment or decrement (int or float)
    - operator: the operator to use for the operation (either '+' or '-')

    Returns:
    - the result of the increment or decrement operation (int or float)
    """
    if operator == '+':
        num += 1
    elif operator == '-':
        num -= 1
    else:
        print("Invalid operator")
        return None

    return num
# increment a number
num = 5
num = increment_decrement(num, '+')
print(num) # expected output: 6

# decrement a number
num2=5
num2 = increment_decrement(num2, '-')
print(num2) # expected output: 5
# handle invalid operator
num = increment_decrement(num, '*') # expected output: Invalid operator, None