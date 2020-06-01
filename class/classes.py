class Flight:
    counter = 1
    def __init__(self, origin, destination, duration):
        # Flight Detail
        self.origin = origin
        self.destination = destination
        self.duration = duration

        # Keep track of passengers
        self.passengers = []

        # Keep track of id number
        self.id = Flight.counter
        Flight.counter += 1

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount 

    def add_passengers(self, p):
        self.passengers.append(p)
        self.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name

f1 = Flight(origin="New York", destination="Paris", duration=540)

p1 = Passenger("Thura")
p2 = Passenger("Hein Htet")
p3 = Passenger("Wai Yan")

f1.delay(20)

f1.add_passengers(p1)
f1.add_passengers(p2)
f1.add_passengers(p3)

f1.print_info()