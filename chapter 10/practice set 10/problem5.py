# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways



class Train:
    def __init__( self , name , fare , total_seats ):
        self.name = name
        self.fare = fare
        self.total_seats = total_seats
        self.booked_seats = 0
        
        
    def book_ticket(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Ticket booked successfully!")
        else:
            print("Sorry, no more seats available.")

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        return f"Available seats: {available_seats}"

    def get_fare_info(self):
        return f"Fare per ticket: {self.fare} INR"
        
        
        
train = Train("Rajdhani Express", 1500, 2)

print(train.get_status())        
print(train.get_fare_info())     

train.book_ticket()              
print(train.get_status())        

train.book_ticket()              
print(train.get_status())        

train.book_ticket()     