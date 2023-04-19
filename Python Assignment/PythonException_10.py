class ClassNotFoundException(Exception):
    pass

def find_class(classname):
    if classname == "MyClass":
        return MyClass()
    else:
        raise ClassNotFoundException("Class not found: " + classname)

class MyClass:
    def __init__(self):
        print("MyClass object created.")

try:
    obj = find_class("NoExistingClass")
except ClassNotFoundException as e:
    print(e)
