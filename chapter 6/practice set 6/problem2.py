#  Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.




marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))


# check total percentage 

total_percentage = ( marks1 + marks2 + marks3 ) * 100 / 300 ; 

if( total_percentage >= 40  and marks1>= 33 and marks2 >= 33 and marks3 >= 33 ):
    print("You are pass : ", total_percentage)
else:
    print("You failed, try again next year! : ", total_percentage)
    








