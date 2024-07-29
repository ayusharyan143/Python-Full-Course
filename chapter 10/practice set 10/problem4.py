# Add a static method in problem 2, to greet the user with hello.






import math


class Calculator:
    def __init__(self , number):
        self.number = number 
        
    def square(self):
        return self.number ** 2 
    
    def cube(self):
        return self.number ** 3 

    def squareRoot(self):
        return math.sqrt( self.number)
    
    
    @staticmethod
    def greet():
        print("Hello World!")

        

        
calc = Calculator(5)

print(f"Square of {calc.number}: {calc.square()}")
print(f"Cube of {calc.number}: {calc.cube()}")
print(f"Square root of {calc.number}: {calc.squareRoot()}")

calc.greet()