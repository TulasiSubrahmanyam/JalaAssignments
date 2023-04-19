class MyClass:
    def __init__(self, public_var, _protected_var, __private_var):
        self.public_var = public_var
        self._protected_var = _protected_var
        self.__private_var = __private_var

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

# creating an object of MyClass and accessing its variables and methods
obj = MyClass("public_value", "protected_value", "private_value")
print("public_var: ", obj.public_var)
print("_protected_var: ", obj._protected_var)
# accessing __private_var directly will result in an AttributeError
print("Calling public_method:")
obj.public_method()
print("Calling _protected_method:")
obj._protected_method()
# calling __private_method directly will result in an AttributeError
print("Calling __private_method:")
obj._MyClass__private_method()
