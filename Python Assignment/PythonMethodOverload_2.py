from multipledispatch import dispatch

@dispatch(str)
def print_message(message):
    print(f"Message: {message}")

@dispatch(str, bool)
def print_message(message, flag):
    message_with_flag = f"{message} - Flag: {flag}"
    print(message_with_flag)
print_message("Hello, world!")  # prints "Message: Hello, world!"
print_message("Hello, world!", True)  # prints "Hello, world! - Flag: True"
