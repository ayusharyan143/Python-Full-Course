'''

    --------------------CLASS ATTRIBUTES--------------------------

    An attribute that belongs to the class rather than a particular object.



    
    --------------------INSTANCE ATTRIBUTES--------------------------

    An attribute that belongs to the Instance (object). Assuming the class from the previous 

'''





class Employee:
    name = "Ayush"
    language = "Python"     # This is a class attribute
    company = "Google"
    salary = 1200000
    
    



ayush = Employee()   # Object Instatiation
ayush.language = "JavaScript"   # This is an instance attribute

print(ayush.language , ayush.salary )



    