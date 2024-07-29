# Write a class “Calculator” capable of finding square, cube and square root of a number.



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
        

        
calc = Calculator(5)

print(f"Square of {calc.number}: {calc.square()}")
print(f"Cube of {calc.number}: {calc.cube()}")
print(f"Square root of {calc.number}: {calc.squareRoot()}")