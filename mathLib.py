import numpy as np
#calculate the fibonacci sequence for n with the help of recursive
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
#calculate the fibonacci sequence for n
def fib(n):

    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b

    return a

#Show the multiplication of n for the range of 0 to n
def multiplication(x):

    for i in range(0,x + 1):
        print (i * x)

#Show the multiplication table for 0 to n
def multiplicationTable(n):

    for i in range(0,n + 1):

        print(" ")

        for(j) in range(0,n + 1):

            print (i*j,end=" ")

#Convert a cartesian cordonnate to polar
def cartesianToPolar(x,y):

    r = np.sqrt(x**2 + y**2)
    angle = np.arctan(y,x)

    return (r, angle)

#Convert a polar cordonnate to Cartesian
def polarToCartesian(r, angle):

    x = r * np.cos(angle)
    y = r * np.sin(angle)

    return (x, y)

#Return the hypothenuse of a triangle
def pythagore(a,b):
    c = np.sqrt(a**2 + b**2)
    return c

#return the result of the equation leave zero to  if there is nothing to solve return zero
def lawOfSines(a,A,b,B):
    if(a == 0):
        a = (np.sin(A)*b) / np.sin(B)

        return a

    if(b == 0):

        b= (a * np.sin(B)) / np.sin(A)

        return b

    if(A == 0):

        A = np.arcsin( b / (np.sin(B) * a) )

        return A

    if(B == 0):

        B = np.arcsin(a / (np.sin(A) * b))

        return B

    return 0