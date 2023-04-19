class MyException(Exception):
    def __init__(self, message):
        self.message = message

raise MyException("This is my custom exception message")
