'''

    -------------------  __INIT__() CONSTRUCTOR-----------------------

    -> In Python, a constructor is a special method used to initialize objects of a class. It's defined using the __init__ method. 


    * __init__() is a special method which is first run as soon as the object is created.
    
    * __init__() method is also known as constructor.
    
    
    * It takes ‘self’ argument and can also take further arguments



'''





class Dog:
    
    # ( __init__ ) dunder method which is automatically called when you create an instance of the class .
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 
    
myDog = Dog("Buddy" , 3)

print(  myDog.name )
print( myDog.age )