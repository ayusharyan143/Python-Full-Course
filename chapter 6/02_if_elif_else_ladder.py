

a = int( input("Enter your age: "))

if( a >= 18 ):
    print("Congrats...!!")
    print("You are eligible for Driving Licence ")

elif( a < 0 ):
    print("You are entering an invalid age ")

elif( a == 0 ):
    print("You are entering 0 which is not a valid age ")

else:
    print("You are Not eligible for Driving Licence ")