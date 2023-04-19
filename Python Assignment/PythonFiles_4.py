# Open the file stream in binary mode
with open('newFile.txt', 'rb') as file:

    # Read the entire file into a bytes object
    file_data = file.read()

    # Get the total length of the file in bytes
    total_length = len(file_data)

    # Get a random position within the file
    random_position = total_length // 2

    # Read a chunk of data from the random position
    data = file_data[random_position:random_position + 1024]

    # Get the first line of the file
    first_line = file_data.split(b'\n')[0]

    # Print the results
    print(f'Total length of the file: {total_length} bytes')
    print(f'Data read from the middle of the file: {data}')
    print(f'First line of the file: {first_line}')
