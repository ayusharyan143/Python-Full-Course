
# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

l = [ 1 , "Ayush" , "This" , False , "mahi" , 3.5 , 23.343 , 9 , "nanu"]

i = 0 

while( i < len(l) ):
    print( l[i] )
    i += 1 

print("\n code end using while loop \n")


# ---------------------------same code using for loop---------------------


for i in range( 0 , len(l) ):
    print( l[i] )
    i += 1 
    