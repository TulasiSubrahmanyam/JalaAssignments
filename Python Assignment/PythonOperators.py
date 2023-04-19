def arithmetic_operator(num1, num2, operator):
    """
    This function performs arithmetic operations on two numbers using the specified operator.

    Args:
    - num1: the first number (float or int)
    - num2: the second number (float or int)
    - operator: the arithmetic operator to use (+, -, *, /)

    Returns:
    - the result of the arithmetic operation (float or int)
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        return None

    return result
# perform addition
print(arithmetic_operator(3, 4, '+')) # expected output: 7

# perform subtraction
print(arithmetic_operator(5.5, 2.5, '-')) # expected output: 3.0

# perform multiplication
print(arithmetic_operator(6, 7, '*')) # expected output: 42

# perform division
print(arithmetic_operator(10, 3, '/')) # expected output: 3.3333333333333335

# handle invalid operator
print(arithmetic_operator(2, 3, '%')) # expected output: Invalid operator, None
