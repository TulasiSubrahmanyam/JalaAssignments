def find_smaller_larger(num1, num2):
   
    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1
    return (smaller, larger)
# find the smaller and larger number
num1 = 5
num2 = 7
result = find_smaller_larger(num1, num2)
print(f"The smaller number is {result[0]} and the larger number is {result[1]}")

# find the smaller and larger number of two other numbers
num3 = 3.14
num4 = 2.71
result = find_smaller_larger(num3, num4)
print(f"The smaller number is {result[0]} and the larger number is {result[1]}")
