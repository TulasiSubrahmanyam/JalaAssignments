# get the input number from the user
num = int(input("Enter a number: "))

# determine the number of digits
num_digits = len(str(num))

# calculate the sum of the digits raised to the power of the number of digits
sum = 0
for digit in str(num):
    sum += int(digit) ** num_digits

# check if the sum is equal to the original number
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
