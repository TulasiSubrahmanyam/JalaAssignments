from MyClass import MyClass

from DifferentPackageClass import DifferentPackageClass
from childClass import ChildClass
from otherClass import OtherClass


# create instances of the classes
my_class = MyClass()
other_class = OtherClass()
different_package_class = DifferentPackageClass()
child_class = ChildClass()

# access protected members
print(my_class._protected_field)  # prints "I am protected"
my_class._protected_method()  # prints "This is a protected method"

other_class.access_protected()  # prints "I am protected" and "This is a protected method"
different_package_class.access_protected_from_different_package()  # prints "I am protected" and "This is a protected method"
child_class.access_protected_from_child()  # prints "I am protected" and "This is a protected method"
