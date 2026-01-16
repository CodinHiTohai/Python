# Create a class MathUtils with:

# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."
class mathutils:
    def __init__(self):
        pass
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def description(cls):
        print("this is a utility class for math operations ")
# a=mathutils
# print(a.add(4,5))
# a.description()
mathutils.description()
mathutils.add(5,4)