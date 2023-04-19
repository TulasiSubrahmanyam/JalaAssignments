def compare_numbers(num1, num2):
    """
    This function compares two numbers using relational operators.

    Args:
    - num1: the first number (int or float)
    - num2: the second number (int or float)

    Returns:
    - a string indicating the result of the comparison
    """
    if num1 < num2:
        return f"{num1} is less than {num2}"
    elif num1 <= num2:
        return f"{num1} is less than or equal to {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 >= num2:
        return f"{num1} is greater than or equal to {num2}"
    else:
        return "The numbers are not comparable"
# compare two numbers
num1 = 5
num2 = 7
result = compare_numbers(num1, num2)
print(result)

# compare two other numbers
num3 = 3.14
num4 = 3.14
result = compare_numbers(num3, num4)
print(result)
