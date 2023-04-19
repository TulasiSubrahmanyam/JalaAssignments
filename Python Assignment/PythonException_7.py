try:
    file = open("example.txt", "r")
    file_contents = file.read()
    print(file_contents)
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File closed")
