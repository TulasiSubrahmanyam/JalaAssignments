def check_equality(num1,num2):
     """
    This function checks if two numbers are equal.

    Args:
    - num1: the first number (int or float)
    - num2: the second number (int or float)

    Returns:
    - True if the two numbers are equal, False otherwise (bool)
    """
     if num1==num2:
        return True
     else:
         return False

num1=5
num2=6
print(check_equality(num1,num2))     
a=4
b=4
print(check_equality(a,b))