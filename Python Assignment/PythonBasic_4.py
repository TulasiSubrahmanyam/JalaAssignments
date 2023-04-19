# global variable
my_var = "global"

# function that defines a local variable with the same name as the global variable
def my_func():
    my_var = "local"
    print("Inside function: ", my_var)

# call the function and print both the global and local variables
my_func()
print("Outside function: ", my_var)
