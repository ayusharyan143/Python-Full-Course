# Write a program to print multiplication table of n using for loops in reversed order



# method: 1 

number = int( input("Enter a Number: "))

for i in range( 10 , 0 , -1  ):
    print( f"{number} X {i} =  {number*i}" )





# method: 2 

number = int( input("Enter a Number: "))

for i in range( 1 , 11 ):
    print( f"{number} X {11-i} =  {number*(11-i)}" )


