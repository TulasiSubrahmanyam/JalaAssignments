filename = input("Enter the file name: ")
text = input("Enter the text to write to the file: ")

with open(filename, 'w') as file:
    file.write(text)

print("Text written to", filename)

