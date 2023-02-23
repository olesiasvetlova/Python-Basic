class Transport:
    """
    Class describing a transport vehicle.
    """
    def __init__(self, license_plate: str, num_wheels: int, engine_power: float, max_speed: float):
        self.license_plate = license_plate
        self.num_wheels = num_wheels
        self.engine_power = engine_power
        self.max_speed = max_speed

    def move(self):
        print(f"The vehicle is moving.")

    def stop(self):
        print("The vehicle has stopped.")


class Bicycle(Transport):
    """
    Class describing a bicycle.
    """
    def __init__(self, license_plate: str, num_wheels: int, engine_power: float, max_speed: float):
        super().__init__(license_plate, num_wheels, engine_power, max_speed)

    def ride(self):
        print("The bicycle is being ridden.")


class Motorcycle(Bicycle):
    """
    Class describing a motorcycle.
    """
    def __init__(self, license_plate: str, num_wheels: int, engine_power: float, max_speed: float):
        super().__init__(license_plate, num_wheels, engine_power, max_speed)

    def ride_fast(self):
        print("The motorcycle is being ridden fast.")


class Car(Transport):
    """
    Class describing a car.
    """
    def __init__(self, license_plate: str, num_wheels: int, engine_power: float, max_speed: float, num_doors: int):
        super().__init__(license_plate, num_wheels, engine_power, max_speed)
        self.num_doors = num_doors

    def honk(self):
        print("The car is honking.")


class Truck(Car):
    """
    Class describing a truck.
    """
    def __init__(self, license_plate: str, num_wheels: int, engine_power: float, max_speed: float, num_doors: int,
                 cargo_capacity: float):
        super().__init__(license_plate, num_wheels, engine_power, max_speed, num_doors)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        print("The truck is being loaded with cargo.")


class Bus(Transport):
    """
    Class describing a bus.
    """
    def __init__(self, license_plate: str, num_wheels: int, engine_power: float, max_speed: float, num_seats: int):
        super().__init__(license_plate, num_wheels, engine_power, max_speed)
        self.num_seats = num_seats

    def board_passengers(self):
        print("Passengers are boarding the bus.")


my_transport = Transport("AB1234", 4, 100.0, 120.0)
my_transport.move()
my_transport.stop()
my_bicycle = Bicycle("BC5678", 2, 0.0, 25.0)
my_bicycle.move()
my_bicycle.ride()
my_motorcycle = Motorcycle("CD9012", 2, 50.0, 150.0)
my_motorcycle.move()
my_motorcycle.ride()
my_motorcycle.ride_fast()
my_car = Car("EF3456", 4, 200.0, 180.0, 4)
my_car.move()
my_car.honk()
my_truck = Truck("GH7890", 6, 300.0, 150.0, 2, 5000.0)
my_truck.move()
my_truck.load_cargo()
my_bus = Bus("IJ2345", 6, 150.0, 100.0, 50)
my_bus.move()
my_bus.board_passengers()