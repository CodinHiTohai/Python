# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".


def decorator(func):
    def wrapper():
        print("function is being called")
        func()
    return wrapper

@decorator
def say_hello():
    print("hello")
say_hello()