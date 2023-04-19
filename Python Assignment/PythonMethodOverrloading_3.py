class Example:
    def print_message(self, message: str):
        print(f"Message: {message}")

    def print_message(self, message: int):
        print(f"Number: {message}")
example = Example()

example.print_message("Hello, world!")  # prints "Message: Hello, world!"
example.print_message(42)  # prints "Number: 42"
