class NoSuchFieldException(Exception):
    pass

class MyClass:
    def __init__(self):
        self.field = "value"

try:
    my_obj = MyClass()
    field_value = my_obj.non_existing_field
    #print(field_value)
except AttributeError:
    raise NoSuchFieldException("Field not found.")
