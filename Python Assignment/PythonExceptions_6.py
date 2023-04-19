class MyException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyException("This is my custom exception")
except MyException as e:
    print("An error occurred:", e.message)
