import os

# Specify the path to the file
file_path = 'newFile.txt'

# Check if the file has read access permission
if os.access(file_path, os.R_OK):
    print('File has read access permission')
else:
    print('File does not have read access permission')

# Check if the file has write access permission
if os.access(file_path, os.W_OK):
    print('File has write access permission')
else:
    print('File does not have write access permission')
