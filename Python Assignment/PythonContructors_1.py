class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        elif arg2 is None:
            self.arg1 = arg1
            print(f"One argument constructor called with arg1 = {arg1}")
        else:
            self.arg1 = arg1
            self.arg2 = arg2
            print(f"Two argument constructor called with arg1 = {arg1} and arg2 = {arg2}")
# Calling the default constructor
obj1 = MyClass()

# Calling the one-argument constructor
obj2 = MyClass("Hello")

# Calling the two-argument constructor
obj3 = MyClass("Hello", 123)
