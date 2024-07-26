# Can you change the values inside a list which is contained in set S?     s = {8, 7, 12, "Harry", [1,2]}


s = {8, 7, 12, "Harry", [1,2]}  

'''

    You cannot change the values inside a list that is contained in a set because you cannot include a list in a set in the first place. This is due to the fact that sets in Python require all of their elements to be hashable, and lists are not hashable because they are mutable.

    # Resone why we can't able to update the list in set :
        -> we can't able to include list in a set 
        -> if it happen we can't able to do it by indexing 
        -> Lists are mutable
        -> Sets require hashable elements
        -> Unhashable elements
    

'''