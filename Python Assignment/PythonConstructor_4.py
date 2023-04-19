class MyClass:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self._arg2 = arg2
        self.__arg3 = arg3

    def display_attributes(self):
        print("arg1 =", self.arg1)
        print("arg2 =", self._arg2)
        print("arg3 =", self.__arg3)

# creating an object of MyClass and accessing its attributes
obj = MyClass("value1", "value2", "value3")
obj.display_attributes()
