def is_greater_than9(x):
    if x>9:
        return True
    else:
        return False
a=[1,2,44,22,33,88,3,7]
new=list(filter(is_greater_than9,a))
print(new)