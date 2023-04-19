# Create a dictionary of student IDs and names
students = {
    101: "John Doe",
    102: "Jane Smith",
    103: "Bob Johnson",
    104: "Alice Williams",
    105: "Tom Brown"
}

# Add a new student to the dictionary
students[106] = "Sara Garcia"

# Update the name of an existing student
students[103] = "Robert Johnson"

# Access a value in the dictionary
print("Student with ID 104:", students[104])

# Create a nested dictionary of student details
details = {
    101: {"name": "John Doe", "age": 20, "gender": "M"},
    102: {"name": "Jane Smith", "age": 22, "gender": "F"},
    103: {"name": "Bob Johnson", "age": 21, "gender": "M"},
    104: {"name": "Alice Williams", "age": 23, "gender": "F"},
    105: {"name": "Tom Brown", "age": 19, "gender": "M"}
}

# Access a value in the nested dictionary
print("Details of student with ID 102:", details[102])

# Print the keys present in the dictionary
print("Keys in the students dictionary:", list(students.keys()))

# Delete a value from the dictionary
del students[106]
print("After deleting student with ID 106:", students)
