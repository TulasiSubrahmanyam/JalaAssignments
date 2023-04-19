# get the input string from the user
string = input("Enter a string: ")
string_convert = string.lower()


# reverse the string
reverse_string = string_convert[::-1]

# check if the string is a palindrome
if string_convert == reverse_string:
    print(string_convert, "is a palindrome")
else:
    print(string_convert, "is not a palindrome")
