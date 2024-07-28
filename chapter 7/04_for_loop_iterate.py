
# The range() function in python is used to generate a sequence of number.
# range(start, stop, step_size)
# step_size is usually not used with range()





print("----------------------------range(start, stop, step_size) function---------------------------------")

l = [1,2,3,4,5,3,6,7,3]

for i in range( 0 , len(l) , 2 ):
    print(l[i])






print("----------------------------Iterate in List---------------------------------")

l = [1,2,3,4,5,3,6,7,3]

for i in l :
    print(i)
    
    
    
print("----------------------------Iterate in Tuple---------------------------------")

t = (6, 54 , 2423, 43345)

for i in t:
    print(i)
    
    
    
print("----------------------------Iterate in String---------------------------------")

s = "Ayush"

for i in s:
    print(i)