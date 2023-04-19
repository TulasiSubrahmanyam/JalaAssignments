array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

common_values = []

for value in array1:
    if value in array2 and value not in common_values:
        common_values.append(value)

print("Common values between the arrays:", common_values)
