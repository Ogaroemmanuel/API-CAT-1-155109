class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, num_seats):
        super().__init__(registration_number, make, model)
        self.num_seats = num_seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{type(vehicle).__name__} with registration number {vehicle.registration_number} added to the fleet.")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            print("Vehicles in the fleet:")
            for vehicle in self.vehicles:
                if isinstance(vehicle, Car):
                    print(f"Type: Car, Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Seats: {vehicle.num_seats}")
                elif isinstance(vehicle, Truck):
                    print(f"Type: Truck, Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Cargo Capacity: {vehicle.cargo_capacity}")
                elif isinstance(vehicle, Motorcycle):
                    print(f"Type: Motorcycle, Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                if isinstance(vehicle, Car):
                    print(f"Type: Car, Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Seats: {vehicle.num_seats}")
                elif isinstance(vehicle, Truck):
                    print(f"Type: Truck, Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Cargo Capacity: {vehicle.cargo_capacity}")
                elif isinstance(vehicle, Motorcycle):
                    print(f"Type: Motorcycle, Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}")
                return
        print(f"Vehicle with registration number {registration_number} not found in the fleet.")

# Example 
fleet = Fleet()

car = Car("ABC123", "Toyota", "Corolla", 5)
truck = Truck("XYZ456", "Isuzu", "Elf", 2000)
motorcycle = Motorcycle("PQR789", "Honda", "CBR600RR", 599)

fleet.add_vehicle(car)
fleet.add_vehicle(truck)
fleet.add_vehicle(motorcycle)

fleet.display_vehicles()
fleet.search_vehicle("XYZ456")
fleet.search_vehicle("DEF123")