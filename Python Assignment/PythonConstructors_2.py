class ParentClass:
    def __init__(self, arg1="default_value1", arg2="default_value2"):
        self.arg1 = arg1
        self.arg2 = arg2
        print("Parent class constructor called")

class ChildClass(ParentClass):
    def __init__(self, arg1="new_value1", arg2="new_value2", arg3="new_value3"):
        super().__init__(arg1, arg2) # calling parent class constructor
        self.arg3 = arg3
        print("Child class constructor called")

# creating an object of ChildClass
child = ChildClass(arg1="override_value1", arg3="override_value3")

# accessing the attributes of the ChildClass object
print("arg1: ", child.arg1)
print("arg2: ", child.arg2)
print("arg3: ", child.arg3)
