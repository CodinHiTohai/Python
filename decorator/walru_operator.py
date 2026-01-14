# def very_slow():
#     print("hello govind....")
#     print("hello govind....")
#     print("hello govind....")
#     print("hello govind....")
#     print("hello govind....")
#     print("hello govind....")
#     print("hello govind....")
#     print("hello govind....")
#     return 110
# if(very_slow()>13):
#     print(very_slow)
# else:
#     print("this is the slow")
# Without walrus operator
data = input("Enter a value (or 'quit' to exit): ")
while data != "quit":
    print(f"You entered: {data}")
    data = input("Enter a value (or 'quit' to exit): ")

# With walrus operator
while (data := input("Enter a value (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {data}")