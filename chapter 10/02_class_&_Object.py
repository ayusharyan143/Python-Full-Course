'''

    ----------------------CLASS---------------------

    -> A class is a blueprint for creating object



    -> Syntax:
        class Employee: # Class name is written in pascal case
        # Methods & Variables 






    ----------------------OBJECT---------------------
    
    -> An object is an instantiation of a class. When class is defined, a template (info) is
    defined. Memory is allocated only after object instantiation.
    
    
    ->Objects of a given class can invoke the methods available to it without revealing the
    implementation details to the user. - Abstractions & Encapsulation!

        
    
'''




# class created
class Employee:
    name = "Ayush"
    language = "Python"
    salary = 120000
    
    
# object
ayush = Employee()
print( "Name: " , ayush.name  )
print( "Language: " , ayush.language  )



rohan = Employee()
print( "Name: " , rohan.name  )
print( "Language: " , rohan.language  )

