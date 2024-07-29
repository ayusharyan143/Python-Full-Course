# Create a class “Programmer” for storing information of few programmers working at Microsoft


class Programmer: 
    company = "Microsoft"  

    def __init__(self, name, id, salary):
        self.name = name 
        self.id = id 
        self.salary = salary 


a = Programmer("Ayush" , 1 , 3000000)
print(f"Name: {a.name}    ID: {a.id}    Salary: {a.salary}")


r = Programmer("Rohan" , 2 , 3000000)
print(f"Name: {r.name}    ID: {r.id}    Salary: {r.salary}")

