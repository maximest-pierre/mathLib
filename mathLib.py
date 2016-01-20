
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib(n):

    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b

    return a

def multiplication(x):

    for i in range(0,x + 1):
        print (i * x)

def multiplicationTable():
    for i in range(0,10):
        print(" ")
        for(j) in range(0,10):

            print (i*j,end=" ")

