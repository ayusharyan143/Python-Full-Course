'''

    -> A function is a group of statements performing a specific task.

    -> When a program gets bigger in size and its complexity grows, it gets difficult for a

    -> program to keep track on which piece of code is doing what!

    -> A function can be reused by the programmer in a given program any number of




    -------------FUNCTION DEFINITION-----------

    The part containing the exact set of instructions which are executed during the function
    call.



    -------------FUNCTION SYNTAX-----------

        def func1():
            print('hello')



'''




# FUNCTION: 

def findAverage():
    a = int( input("Enter you number 1 : "))
    b = int( input("Enter you number 2 : "))
    c = int( input("Enter you number 3 : "))
    
    average = ( a + b + c ) / 3 ; 
    
    print("Average of Number: " , average )
    
    
    
# FUNCTION CALL :This function can be called any number of times, anywhere in the program.

findAverage()
