# Write a program to calculate the factorial of a given number using for loop.


number = int( input("Enter the number :  "))
fact = 1 

for i in range(1 , number+1 ):
    fact *= i 
    i += 1 
print( f"The factorial of {number} : {fact}")