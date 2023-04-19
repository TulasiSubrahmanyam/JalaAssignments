class MyClass:
    my_static_variable = 42

    @classmethod
    def change_static_variable(cls, new_value):
        cls.my_static_variable = new_value

print(MyClass.my_static_variable) # prints 42

MyClass.change_static_variable(10) # pass 10 as a parameter
print(MyClass.my_static_variable) # prints 10
