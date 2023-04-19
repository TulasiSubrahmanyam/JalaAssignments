from MyClass import MyClass

class DifferentPackageClass:
    def access_protected_from_different_package(self):
        obj = MyClass()
        print(obj._protected_field)
        obj._protected_method()
