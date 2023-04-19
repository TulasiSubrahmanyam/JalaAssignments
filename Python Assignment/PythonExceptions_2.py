try:
    result = 10 / 0
    print(result)
except ArithmeticError:
    print("Error: division by zero")
