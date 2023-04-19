class MyClass:
    myStaticVariable=42
my_object=MyClass()
print(my_object.myStaticVariable)

#change the static value
my_object.myStaticVariable=10
print(my_object.myStaticVariable)