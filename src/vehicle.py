from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maintenance_status = None
        self.__rental_price = None 

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage
    
    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery Percentage . Enter valid percentage...")

    def get_rental_price(self):
        return self.__rental_price
    
    def set_rental_price(self, rental_price):
        if rental_price < 0:
            print("Rental Price should be positive")
        self.__rental_price = rental_price
    
    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def set_maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status

    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return self.vehicle_id == other.vehicle_id
    
    def display(self):
        print(f"Vehicle Id : {self.vehicle_id}")
        print(f"Model : {self.model}")
        print(f"Battery Percentage : {self.__battery_percentage}%")

    def __str__(self):
        return f"Vehicle ID : {self.vehicle_id} \nModel : {self.model}\n Battery_percentage : {self.__battery_percentage}%"
    

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5.0 + (0.50 * distance)

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance):
        return 1.0 + (0.15 * distance)

    