try:
    # Code that might raise exceptions
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    # Catch a value error if the user enters an invalid input
    print("Invalid input, please enter a number.")
except ZeroDivisionError:
    # Catch a zero division error if the user enters 0 as the second number
    print("Cannot divide by zero.")
except Exception as e:
    # Catch any other exceptions that are not caught by the previous catch blocks
    print("An error occurred:", e)
