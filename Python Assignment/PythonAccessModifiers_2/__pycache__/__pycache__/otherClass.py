from MyClass import MyClass

class OtherClass:
    def access_protected(self):
        obj = MyClass()
        print(obj._protected_field)
        obj._protected_method()
