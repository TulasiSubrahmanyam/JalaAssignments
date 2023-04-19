try:
    with open("non-existing-file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
