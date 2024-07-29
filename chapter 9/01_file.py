'''
    The random-access memory is volatile, and all its contents are lost once a program
    terminates. In order to persist the data forever, we use files.


    -> A file is data stored in a storage device. A python program can talk to the file by reading
    content from it and writing content to it.
    
    
    
    --------------TYPE OF FILES--------------------
        
    There are 2 types of files:

        1. Text files (.txt, .c, etc)
        2. Binary files (.jpg, .dat, etc)

    Python has a lot of functions for reading, updating, and deleting files.



'''


# File Open
f = open("01_file.txt")

data = f.read()
print(data)

# File close
f.close()