def fibonacci(n):
    if(n==0 or n==1):
        return n
    return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(6))
#this is how work 
#for fib(6)
# fibonacci(4)+fibonacci(5)
#     3+5
# fibonacci(4):1+2=3
# fibonacci(2) (0+1)+fibonacci(3)+2
# fibonacci(2):   
                
# fibonacci(0)+fibonacci(1)=0+1

# fibonacci(3):
# fibonacci(1)+fibonacci(2)
# fibonacci(2):
# fibonacci(0)+fibonacci(1):0+1


# fibonacci(5):=5
# fibonacci(3)+fibonacci(4)=3;
# fibonacci(3):
# fibonacci(1)+fibonacci(2)=2
