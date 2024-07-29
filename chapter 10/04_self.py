
'''
 
    ---------------------SELF PARAMETER---------------------
    
    -> self refers to the instance of the class. It is automatically passed with a function call
    from an object





    ---------------------STATIC METHOD---------------------

    ->Sometimes we need a function that does not use the self-parameter. 
 
'''
 
 

class Employee:
    name = "Ayush"
    language = "Python"     # This is a class attribute
    company = "Google"
    salary = 1200000
    
    
    def getInfo(self):
        print( f"The langauge is { self.language }. The salary is {self.salary} ")

    @staticmethod   # you can also use @staticmethod insted of self  
    def greet():
        print("Good Morning!")

    

ayush = Employee()   # Object Instatiation

ayush.greet()
ayush.getInfo()



    