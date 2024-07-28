# Write a program using functions to find greatest of three numbers.

def findGreatest(a , b, c):
    if( a>b and a>c ):
        return a 
    elif( b>a and b>c ):
        return b 
    else:
        return c 
    
    

a = int(input("Enter Number a : "))
b = int(input("Enter Number b : "))
c = int(input("Enter Number c : "))


print( f"Greatest No. is : {findGreatest(a,b,c)} " )