
'''
    ---------------THE BREAK STATEMENT--------------

        'break' is used to come out of the loop when encountered. It instructs the program to –
        exit the loop now.

'''


print("----------------------------Break---------------------------------")

for i in range (0,80):
    print(i) 
    if i==7:
        break








'''

    ---------------THE CONTINUE STATEMENT--------------

        'continue' is used to stop the current iteration of the loop and continue with the next
        one. It instructs the Program to “skip this iteration”.

'''



print("----------------------------Continue---------------------------------")

for i in range(4):
    print("printing")
    if i == 2: 
        continue
    print(i)








'''

    ---------------THE PASS STATEMENT--------------

        pass is a null statement in python.
        It instructs to “do nothing”

'''



print("----------------------------Pass---------------------------------")

l = [1,7,8]
for item in l:
    pass