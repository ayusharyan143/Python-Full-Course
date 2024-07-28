# Write a python function to print multiplication table of a given number.



def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number: "))
print_multiplication_table(num)
