# Write a python function to remove a given word from a list ad strip it at the same time.


def remove_and_strip( l , word ):
    n = []

    for item in l :
        if( item != word ):
            n.append(item.strip(word))
    return n 


l = ["Ayush" , "Rohan" , "Shubham" , "an"]

print( remove_and_strip( l , "an"))
