
s = {1,2,3,4,'Ayush'}
print(s)


# add() : Adds an element to the set.

s.add('mahi')
print(s)


# remove() : Removes the specified element from the set. Raises a KeyError if the element is not found.
s.remove(2)
print(s)


# discard() : Removes the specified element from the set if it is present. Does nothing if the element is not found.
s.discard(3)
print(s)


# pop() : Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

s.pop()
print(s)


# clear() : Removes all elements from the set.
s.clear()
print(s)


# union() : Returns a new set with elements from the set and all others.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)



# intersection() ; Returns a new set with elements common to the set and all others.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)


# difference() : Returns a new set with elements in the set that are not in the others.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)




# symmetric_difference() : Returns a new set with elements in either the set or the others but not in both.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)





# issubset() : Checks if the set is a subset of another set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
result = set1.issubset(set2)
print(result)





# issuperset() : Checks if the set is a superset of another set.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
result = set1.issuperset(set2)
print(result)




# isdisjoint() : Checks if two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)


