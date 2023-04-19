# Open the file stream in binary mode
with open('newFile.txt', 'rb') as file:

    # Set the file pointer to a particular index
    file.seek(10)

    # Read a chunk of data from the file
    data = file.read(1024)

    # Print the data to the console
    print(data)
