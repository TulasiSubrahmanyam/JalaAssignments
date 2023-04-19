from MyClass import MyClass

class ChildClass(MyClass):
    def access_protected_from_child(self):
        print(self._protected_field)
        self._protected_method()
