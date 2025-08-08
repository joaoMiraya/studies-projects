class Queue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if not self.isEmpty():
             return self.elements.pop(0)
        else:
            return None

    def size(self):
        return len(self.elements)
    
    def list_elements(self):
        return self.elements
    
    def find_element(self, identifier):
        for index, airplane in enumerate(self.elements):
            if airplane.flight_code == identifier:
                return index + 1
        return None
    
    def get_first_element(self):
        if not self.isEmpty():
            return self.elements[0]
        return None
    
class Airplane:
    def __init__(self, model, enterprise, origin, destination, passengers, flight_code):
        self.model = model
        self.enterprise = enterprise
        self.origin = origin
        self.destination = destination
        self.passengers = passengers
        self.flight_code = flight_code

    def __str__(self):
        return (f"Flight Code: {self.flight_code}\n"
                f"Model: {self.model}\n"
                f"Enterprise: {self.enterprise}\n"
                f"Origin: {self.origin}\n"
                f"Destination: {self.destination}\n"
                f"Passengers: {self.passengers}")

class Airport(Queue):
    def __init__(self):
        super().__init__()

    def seed(self, total_airplanes):
        for i in range(total_airplanes):
            airplane = Airplane(
                model=f"Model-{i+1}",
                enterprise=f"Enterprise-{i+1}",
                origin=f"Origin-{i+1}",
                destination=f"Destination-{i+1}",
                passengers=i + 50,
                flight_code=f"FLY-{i+1}"
            )
            self.add_airplane(airplane)

    def add_airplane(self, airplane):
        self.enqueue(airplane)

    def takeoff(self):
        if not self.isEmpty():
            airplane = self.dequeue()
            print(f"Airplane {airplane.flight_code} is taking off.")
        else:
            print("No airplanes in the queue to take off.")
    
    def total_airplanes(self):
        return self.size()
    
    def list_airplanes(self):
        if self.isEmpty():
            print("No airplanes in the queue.")
        else:
            for airplane in self.list_elements():
                print(airplane)
                print("--------------------------------")


    def next_to_takeoff(self):
        airplane = self.get_first_element()
        if airplane:
            print(f"Next to take off:\n\n{airplane}")
        else:
            print("No airplanes in the queue.")

    def find_airplane_position(self, flight_code):
        position = self.find_element(flight_code)
        if position:
            print(f"Airplane {flight_code} is at position {position} in the queue.")
        else:
            print(f"Airplane {flight_code} not found in the queue.")
    
def main():
    airport = Airport()
    airport.seed(5)

    while True:
        print("\nAirport Management System")
        print("1. Add Airplane to Queue")
        print("2. Take Off Airplane")
        print("3. Show Total Airplanes in Queue")
        print("4. List All Airplanes in Queue")
        print("5. Show Next Airplane to Take Off")
        print("6. Find Airplane Position by Flight Code")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            model = input("Enter airplane model: ")
            enterprise = input("Enter airline enterprise: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            passengers = int(input("Enter number of passengers: "))
            flight_code = input("Enter flight code: ")
            airplane = Airplane(model, enterprise, origin, destination, passengers, flight_code)
            airport.add_airplane(airplane)
            print(f"Airplane {flight_code} added to the queue.")
        
        elif choice == '2':
            airport.takeoff()
        
        elif choice == '3':
            total = airport.total_airplanes()
            print(f"Total airplanes in queue: {total}")
        
        elif choice == '4':
            airport.list_airplanes()
        
        elif choice == '5':
            airport.next_to_takeoff()
        
        elif choice == '6':
            flight_code = input("Enter flight code to find position: ")
            airport.find_airplane_position(flight_code)
        
        elif choice == '7':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()