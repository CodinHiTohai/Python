def decorater(func):
    def wrapper():
        print("iam going to executing....")
        func()
        print("i have execute this function")
    return wrapper


    

@decorater
def say_hello():
    print("hello")
say_hello()

say_hello()
# f=decorater(say_hello)
# f()
