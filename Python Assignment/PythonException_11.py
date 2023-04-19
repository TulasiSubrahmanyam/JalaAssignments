try:
    file = open("non_existing_file.txt", "r")
except IOError as e:
    print("Error:", e)
