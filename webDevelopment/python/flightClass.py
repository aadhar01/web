class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
        
    def add_passengers(self, passenger_name):
        if not self.open_seats():
            return False
        self.passengers.append(passenger_name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(3)

people = ["Harry", "Ron", "Hermoine", "Ginny"]

for person in people:
    if flight.add_passengers(person):
        print(f"flight for the {person} have been booked")
    else:
        print(f"Sorry, {person} flight is fully booked")
