# 1. append 

friends = [ "Apple" , "orange" , "banana" , 5 , 90.76 , False , "Ayush" , "nanu" ]

print(friends)

friends.append("mamta")

print(friends , '\n')



# 2. sort

l1 = [12,34,0,1,3,54,67,78,98,56,31] 
print("Before Sorting: " ,l1)
l1.sort()
print("After Sorting: " ,l1 , '\n')





# 2. reverse

print("Before Reverse: " ,l1)
l1.reverse()
print("After Reverse: " ,l1 , '\n')






# 2. insert

print("Before Insert: " ,l1 )
l1.insert( 3,9999999 )
l1.insert( 6,6666666 )
print("After Insert: " ,l1 , '\n')






# 2. pop

print("Before Pop: " ,l1 )
value = l1.pop( 6 )
print("After Pop: " ,l1 )
print("value of pop element : " , value ,  '\n')









# 2. remove

print("Before Remove: " ,l1 )
l1.remove( 9999999 )
print("After Remove: " ,l1 )













