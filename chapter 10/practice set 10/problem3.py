# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


class MyClass:
    a = 2   #class attribute 
    

# Create an instance of MyClass
obj = MyClass()
    
    
print(f"Initial value of MyClass.a: {MyClass.a}")  
print(f"Initial value of obj.a: {obj.a}")  



# Instance attribute Set 'a' directly using 'object.a = 0'
obj.a = 0


# prints the class attributes
print(f"Value of MyClass.a after setting obj.a: {MyClass.a}") 


# prints the instance attribute bcz instance attribute is present
print(f"Value of obj.a after setting obj.a: {obj.a}")