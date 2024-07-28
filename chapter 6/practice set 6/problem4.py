# Write a program to find whether a given username contains less than 10 characters or not.



username = input("Enter username: ")

if( len(username) < 10 ):
    print("yes, username contains less than 10 characters")
else:
    print("username contains more than or equal to 10 characters")