#using double Quotes
firstMethod="Hello,World This is first Methos"
print(firstMethod)

#second way single Quotes
seconMethod='Hello ,Word'
print(seconMethod)

#using triple quotes

third_method="""This is a multi-line string."""
print(third_method)

#string formating first method
s1='Hello'
s2="world"
print(s1+", "+s2)

#string formating second method
name="John"
age=30
result='My name is {} and I am {} years old.'.format(name,age)
print(result)
#string formating third method
name="Jhon"
age=30
print(f'My name is {name} and I am {age} years old.')