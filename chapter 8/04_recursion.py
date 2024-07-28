'''
    -> Recursion is a function which calls itself.

    -> It is used to directly use a mathematical formula as function.


    ------------EXAMPLE-------------

    factorial(0) = 1 
    factorial(1) = 1 
    factorial(2) = 2 X 1 
    factorial(3) = 3 X 2 X 1  
    factorial(4) = 4 X 3 X 2 X 1 
    factorial(5) = 5 X 4 X 3 X 2 X 1 
    factorial(n) = n X ( n-1 ) X ............ X 3 X 2 X 1 

    factorial(n) = n * factorial( n-1 )

'''



def factorial(n):
    
    # base condition which doesn’t call the function any further
    if( n==1 or n==0 ):
        return 1 
    return n * factorial( n-1 )     # function calling itself


n = int(input("Enter a Number: "))

print(f"Factorial of {n}: {factorial(n) } ")