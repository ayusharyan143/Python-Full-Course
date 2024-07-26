# If the names of 2 friends are same; what will happen to the program in problem 6?



d = {}

name = input("Enter Friends name: ")
lang = input("Enter Language name: ")
d.update( {name : lang } )

name = input("Enter Friends name: ")
lang = input("Enter Language name: ")
d.update( {name : lang } )

name = input("Enter Friends name: ")
lang = input("Enter Language name: ")
d.update( {name : lang } )

name = input("Enter Friends name: ")
lang = input("Enter Language name: ")
d.update( {name : lang } )

print(d)


# it will update the value  for same value bcz key should be unique it will not create another key of same name, but you can make value many time with same value 