import re

my_string = "Hello, world!"
match = re.search("world", my_string)
if match:
    print("Match found")
else:
    print("Match not found")
import re
#another way ^ is starting and$ is ending of string
my_string = "Hello, world!"
match = re.search("^Hello.*world!$", my_string)
if match:
    print("Match found")
else:
    print("Match not found")


#another way using find method
my_string = "Hello, world!"
substring = "world"
index = my_string.find(substring)
if index != -1:
    print("Match found")
else:
    print("Match not found")

