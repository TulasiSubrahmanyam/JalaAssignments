class MyClass:
    def __init__(self):
        self.private_field = "I am private"

    def private_method(self):
        print("This is a private method")

    def print_fields(self):
        print(self.private_field)

    def call_private_method(self):
        self.private_method()


class SubClass(MyClass):
    def access_private_field(self):
        print(self.private_field)

    def call_private_method_from_subclass(self):
        super().private_method()

if __name__ == '__main__':
    obj = MyClass()
    obj.print_fields()  # Output: "I am private"
    obj.call_private_method()  # Output: "This is a private method"

    sub_obj = SubClass()
    sub_obj.access_private_field()  # Output: "I am private"
    sub_obj.call_private_method_from_subclass()  # Output: "This is a private method"
